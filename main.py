import os
import pandas as pd
import tkinter as tk
from tkinter import scrolledtext
from src.load_data import carregar_dados
from src.calculos import (
    valor_total_venda_por_categoria,
    margem_dos_produtos,
    ranking_clientes_por_qtd_mes,
    ranking_fornecedores_estoque_mes,
    ranking_produtos_qtd_vendida_mes,
    ranking_produtos_valor_venda_mes,
    media_valor_venda_categoria_mes,
    ranking_margem_por_categoria,
    produtos_por_cliente,
    ranking_produtos_qtd_estoque
)

class AppGUI:
    def __init__(self, root, dados):
        self.root = root
        self.root.title("Sistema de Análise Infomaz")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)
        self.root.configure(bg="#2e2e2e")  # Fundo escuro

        self.btn_style = {
            "bg": "#4a4a4a",
            "fg": "white",
            "activebackground": "#666",
            "font": ("Arial", 12),
            "width": 30,
            "relief": tk.RAISED,
            "bd": 2
        }

        self.label_style = {
            "bg": "#2e2e2e",
            "fg": "white",
            "font": ("Arial", 16, "bold")
        }

        self.dados = dados
        self.criar_menu_principal()

    def limpar_janela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def criar_menu_principal(self):
        self.limpar_janela()
        frame = tk.Frame(self.root, bg="#2e2e2e")
        frame.pack(expand=True)

        tk.Label(frame, text="MENU PRINCIPAL", **self.label_style).pack(pady=20)

        tk.Button(frame, text="Acessar Dados", command=self.menu_dados, **self.btn_style).pack(pady=10)
        tk.Button(frame, text="Cálculos", command=self.menu_calculos, **self.btn_style).pack(pady=10)
        tk.Button(frame, text="Sair", command=self.root.quit, **self.btn_style).pack(pady=10)

    def menu_dados(self):
        self.limpar_janela()
        frame = tk.Frame(self.root, bg="#2e2e2e")
        frame.pack(expand=True)

        tk.Label(frame, text="ACESSAR DADOS", **self.label_style).pack(pady=10)

        opcoes = [
            ("Cadastro Produtos", "Cadastro Produtos"),
            ("Cadastro Clientes", "Cadastro Clientes"),
            ("Cadastro de Estoque", "Cadastro de Estoque"),
            ("Cadastro Fornecedores", "Cadastro Fornecedores"),
            ("Transações Vendas", "Transações Vendas"),
        ]

        for texto, aba in opcoes:
            tk.Button(frame, text=texto, command=lambda a=aba: self.mostrar_dataframe(a, voltar_para="dados"), **self.btn_style).pack(pady=5)

        tk.Button(frame, text="Home", command=self.criar_menu_principal, **self.btn_style).pack(pady=20)

    def menu_calculos(self):
        self.limpar_janela()
        frame = tk.Frame(self.root, bg="#2e2e2e")
        frame.pack(expand=True)

        tk.Label(frame, text="CÁLCULOS", **self.label_style).pack(pady=10)

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

        for texto, funcao in botoes:
            tk.Button(frame, text=texto, command=lambda f=funcao: self.mostrar_resultado(f), **{**self.btn_style, "width": 50}).pack(pady=4)

        tk.Button(frame, text="Home", command=self.criar_menu_principal, **{**self.btn_style, "width": 50}).pack(pady=20)


    def mostrar_dataframe(self, aba, voltar_para="dados"):
        self.limpar_janela()
        df = self.dados[aba]
        self.exibir_texto(df.to_string(), voltar_para)

    def mostrar_resultado(self, funcao):
        self.limpar_janela()
        resultado = funcao(self.dados)
        self.exibir_texto(resultado.to_string(), voltar_para="calculos")

    def exibir_texto(self, texto, voltar_para="dados"):
        frame = tk.Frame(self.root, bg="#2e2e2e")
        frame.pack(fill='both', expand=True)

        text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, font=("Courier", 10), bg="#1e1e1e", fg="white", insertbackground="white")
        text_area.insert(tk.END, texto)
        text_area.config(state=tk.DISABLED)
        text_area.pack(fill='both', expand=True, padx=20, pady=20)

        if voltar_para == "calculos":
            tk.Button(frame, text="Voltar", command=self.menu_calculos, **self.btn_style).pack(pady=10)
        else:
            tk.Button(frame, text="Voltar", command=self.menu_dados, **self.btn_style).pack(pady=10)

def main():
    caminho_arquivo = os.path.join("data", "Case_Infomaz_Base_de_Dados.xlsx")
    dados = carregar_dados(caminho_arquivo)

    root = tk.Tk()
    app = AppGUI(root, dados)
    root.mainloop()

if __name__ == "__main__":
    main()
