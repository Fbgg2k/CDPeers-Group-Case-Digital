import pandas as pd

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
        # Definir as abas que devem ser carregadas
        abas_relevantes = [
            "Guia",
            "Cadastro Produtos",
            "Cadastro Clientes",
            "Cadastro de Estoque",
            "Cadastro Fornecedores",
            "Transações Vendas"
        ]

        # Carregar todas as abas como um dicionário de DataFrames
        dados = pd.read_excel(caminho_arquivo, sheet_name=abas_relevantes, engine="openpyxl")

        print("Dados carregados com sucesso!")  # Mensagem útil para debug

        return dados

    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
        raise

    except ValueError as e:
        print(f"Erro ao carregar dados: {e}")
        raise
