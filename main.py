import os  # Módulo para manipulação de caminhos e operações do sistema operacional
import pandas as pd  # Biblioteca para análise e manipulação de dados (DataFrames)
import tkinter as tk  # Biblioteca para criação de interfaces gráficas (GUI)
from tkinter import scrolledtext  # Widget de texto com barra de rolagem para Tkinter

# Importa função para carregar dados do Excel
from src.load_data import carregar_dados

# Importa funções de cálculo e análise de dados do módulo src.calculos
from src.calculos import (
    valor_total_venda_por_categoria,        # Calcula o valor total de vendas por categoria de produto
    margem_dos_produtos,                    # Calcula a margem de lucro dos produtos
    ranking_clientes_por_qtd_mes,           # Gera ranking de clientes por quantidade comprada por mês
    ranking_fornecedores_estoque_mes,       # Gera ranking de fornecedores por estoque/mês
    ranking_produtos_qtd_vendida_mes,       # Ranking de produtos por quantidade vendida/mês
    ranking_produtos_valor_venda_mes,       # Ranking de produtos por valor de venda/mês
    media_valor_venda_categoria_mes,        # Média do valor de venda por categoria/mês
    ranking_margem_por_categoria,           # Ranking de margem de lucro por categoria
    produtos_por_cliente,                   # Lista produtos comprados por cliente
    ranking_produtos_qtd_estoque            # Ranking de produtos por quantidade em estoque
)

class AppGUI:
    """
    Classe principal da interface gráfica do sistema de análise Infomaz.
    Gerencia menus, exibição de dados e resultados de cálculos.
    """
    def __init__(self, root, dados):
        # Inicializa a janela principal e configurações visuais
        self.root = root
        self.root.title("Sistema de Análise Infomaz")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)
        self.root.configure(bg="#2e2e2e")  # Fundo escuro

        # Estilo dos botões
        self.btn_style = {
            "bg": "#4a4a4a",
            "fg": "white",
            "activebackground": "#666",
            "font": ("Arial", 12),
            "width": 30,
            "relief": tk.RAISED,
            "bd": 2
        }

        # Estilo dos rótulos (labels)
        self.label_style = {
            "bg": "#2e2e2e",
            "fg": "white",
            "font": ("Arial", 16, "bold")
        }

        self.dados = dados  # Dicionário com DataFrames carregados do Excel
        self.criar_menu_principal()  # Exibe o menu principal ao iniciar

    def limpar_janela(self):
        """
        Remove todos os widgets da janela principal.
        Usado para trocar de tela/aba.
        """
        for widget in self.root.winfo_children():
            widget.destroy()

    def criar_menu_principal(self):
        """
        Cria e exibe o menu principal da aplicação.
        """
        self.limpar_janela()
        frame = tk.Frame(self.root, bg="#2e2e2e")
        frame.pack(expand=True)

        tk.Label(frame, text="MENU PRINCIPAL", **self.label_style).pack(pady=20)

        # Botões para acessar dados, cálculos ou sair
        tk.Button(frame, text="Acessar Dados", command=self.menu_dados, **self.btn_style).pack(pady=10)
        tk.Button(frame, text="Cálculos", command=self.menu_calculos, **self.btn_style).pack(pady=10)
        tk.Button(frame, text="Sair", command=self.root.quit, **self.btn_style).pack(pady=10)

    def menu_dados(self):
        """
        Exibe o menu para acessar diferentes conjuntos de dados.
        """
        self.limpar_janela()
        frame = tk.Frame(self.root, bg="#2e2e2e")
        frame.pack(expand=True)

        tk.Label(frame, text="ACESSAR DADOS", **self.label_style).pack(pady=10)

        # Opções de abas/dados disponíveis
        opcoes = [
            ("Cadastro Produtos", "Cadastro Produtos"),
            ("Cadastro Clientes", "Cadastro Clientes"),
            ("Cadastro de Estoque", "Cadastro de Estoque"),
            ("Cadastro Fornecedores", "Cadastro Fornecedores"),
            ("Transações Vendas", "Transações Vendas"),
        ]

        # Cria botões para cada conjunto de dados
        for texto, aba in opcoes:
            tk.Button(
                frame, text=texto,
                command=lambda a=aba: self.mostrar_dataframe(a, voltar_para="dados"),
                **self.btn_style
            ).pack(pady=5)

        tk.Button(frame, text="Home", command=self.criar_menu_principal, **self.btn_style).pack(pady=20)

    def menu_calculos(self):
        """
        Exibe o menu com as opções de cálculos e análises.
        """
        self.limpar_janela()
        frame = tk.Frame(self.root, bg="#2e2e2e")
        frame.pack(expand=True)

        tk.Label(frame, text="CÁLCULOS", **self.label_style).pack(pady=10)

        # Lista de botões para cada função de cálculo
        botoes = [
            ("Valor total de venda por categoria", valor_total_venda_por_categoria),
            ("Margem dos produtos", margem_dos_produtos),
            ("Ranking clientes por qtd comprada por mês", ranking_clientes_por_qtd_mes),
            ("Ranking fornecedores por estoque/mês", ranking_fornecedores_estoque_mes),
            ("Ranking produtos por qtd vendida/mês", ranking_produtos_qtd_vendida_mes),
            ("Ranking produtos por valor venda/mês", ranking_produtos_valor_venda_mes),
            ("Média valor venda por categoria/mês", media_valor_venda_categoria_mes),
            ("Ranking margem lucro por categoria", ranking_margem_por_categoria),
            ("Produtos comprados por cliente", produtos_por_cliente),
            ("Ranking produtos por estoque", ranking_produtos_qtd_estoque),
        ]

        # Cria botões para cada cálculo
        for texto, funcao in botoes:
            tk.Button(
                frame, text=texto,
                command=lambda f=funcao: self.mostrar_resultado(f),
                **{**self.btn_style, "width": 50}
            ).pack(pady=4)

        tk.Button(frame, text="Home", command=self.criar_menu_principal, **{**self.btn_style, "width": 50}).pack(pady=20)

    def mostrar_dataframe(self, aba, voltar_para="dados"):
        """
        Exibe o DataFrame correspondente à aba selecionada.
        """
        self.limpar_janela()
        df = self.dados[aba]  # Seleciona o DataFrame pelo nome da aba
        self.exibir_texto(df.to_string(), voltar_para)

    def mostrar_resultado(self, funcao):
        """
        Executa a função de cálculo e exibe o resultado.
        """
        self.limpar_janela()
        resultado = funcao(self.dados)  # Executa a função de análise
        self.exibir_texto(resultado.to_string(), voltar_para="calculos")

    def exibir_texto(self, texto, voltar_para="dados"):
        """
        Exibe texto (dados ou resultados) em uma área rolável.
        """
        frame = tk.Frame(self.root, bg="#2e2e2e")
        frame.pack(fill='both', expand=True)

        # Área de texto rolável para exibir DataFrames ou resultados
        text_area = scrolledtext.ScrolledText(
            frame, wrap=tk.WORD, font=("Courier", 10),
            bg="#1e1e1e", fg="white", insertbackground="white"
        )
        text_area.insert(tk.END, texto)
        text_area.config(state=tk.DISABLED)
        text_area.pack(fill='both', expand=True, padx=20, pady=20)

        # Botão para voltar ao menu anterior
        if voltar_para == "calculos":
            tk.Button(frame, text="Voltar", command=self.menu_calculos, **self.btn_style).pack(pady=10)
        else:
            tk.Button(frame, text="Voltar", command=self.menu_dados, **self.btn_style).pack(pady=10)

def main():
    """
    Função principal: carrega os dados e inicia a interface gráfica.
    """
    caminho_arquivo = os.path.join("data", "Case_Infomaz_Base_de_Dados.xlsx")  # Caminho do arquivo Excel
    dados = carregar_dados(caminho_arquivo)  # Carrega os dados em DataFrames

    root = tk.Tk()  # Cria janela principal do Tkinter
    app = AppGUI(root, dados)  # Inicializa a aplicação GUI
    root.mainloop()  # Inicia o loop principal da interface

if __name__ == "__main__":
    main()  # Executa a aplicação se o arquivo for executado diretamente
