import pandas as pd

# Função principal para carregar dados de um arquivo Excel com múltiplas abas relevantes
def carregar_dados(caminho_arquivo="data/Case_Infomaz_Base_de_Dados.xlsx"):
    """
    Carrega os dados das diferentes abas da planilha Excel.

    Parâmetros:
        caminho_arquivo (str): Caminho relativo ou absoluto do arquivo Excel.

    Retorna:
        dict: Dicionário contendo DataFrames das abas:
            - Guia
            - Cadastro Produtos
            - Cadastro Clientes
            - Cadastro de Estoque
            - Cadastro Fornecedores
            - Transações Vendas
    """
    try:
        # Lista com os nomes das abas que serão carregadas do arquivo Excel
        abas_relevantes = [
            "Guia",
            "Cadastro Produtos",
            "Cadastro Clientes",
            "Cadastro de Estoque",
            "Cadastro Fornecedores",
            "Transações Vendas"
        ]

        # Carrega as abas especificadas como um dicionário de DataFrames usando pandas
        dados = pd.read_excel(caminho_arquivo, sheet_name=abas_relevantes, engine="openpyxl")

        print("Dados carregados com sucesso!")  # Mensagem útil para debug

        return dados  # Retorna o dicionário de DataFrames

    except FileNotFoundError:
        # Tratamento de erro caso o arquivo não seja encontrado
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
        raise

    except ValueError as e:
        # Tratamento de erro caso haja problema ao carregar as abas
        print(f"Erro ao carregar dados: {e}")
        raise
