import pandas as pd

def valor_total_venda_por_categoria(dados):
    produtos = dados["Cadastro Produtos"]
    transacoes = dados["Transações Vendas"]

    transacoes["VALOR ITEM"] = transacoes["VALOR ITEM"].astype(str).replace('[R$ ]', '', regex=True).str.replace('.', '').str.replace(',', '.').astype(float)

    merged = transacoes.merge(produtos, on="ID PRODUTO")
    print("Colunas disponíveis após merge:", merged.columns)

    resultado = merged.groupby("CATEGORIA")["VALOR ITEM"].sum().reset_index().sort_values(by="VALOR ITEM", ascending=False)
    return resultado


def margem_dos_produtos(dados):
    estoque = dados["Cadastro de Estoque"]
    transacoes = dados["Transações Vendas"]
    produtos = dados["Cadastro Produtos"]

    # Convertendo os valores corretamente
    transacoes["VALOR ITEM"] = transacoes["VALOR ITEM"].astype(str).replace('[R$ ]', '', regex=True).str.replace('.', '').str.replace(',', '.').astype(float)
    estoque["VALOR ESTOQUE"] = estoque["VALOR ESTOQUE"].astype(str).replace('[R$ ]', '', regex=True).str.replace('.', '').str.replace(',', '.').astype(float)

    # Realizando merge correto entre produtos e estoque antes de unir com transações
    produtos_estoque = produtos.merge(estoque, on="ID ESTOQUE", how="left")
    merged = transacoes.merge(produtos_estoque, on="ID PRODUTO", how="left")

    # Calculando a margem corretamente
    merged["margem"] = merged["VALOR ITEM"] - (merged["VALOR ESTOQUE"] / merged["QTD ESTOQUE"])

    resultado = merged.groupby("ID PRODUTO")["margem"].mean().reset_index().sort_values(by="margem", ascending=False)
    return resultado


def ranking_clientes_por_qtd_mes(dados):
    transacoes = dados["Transações Vendas"]
    clientes = dados["Cadastro Clientes"]

    transacoes["DATA NOTA"] = pd.to_datetime(transacoes["DATA NOTA"])
    transacoes["AnoMes"] = transacoes["DATA NOTA"].dt.to_period("M")

    merged = transacoes.merge(clientes, on="ID CLIENTE")
    resultado = (
        merged.groupby(["AnoMes", "NOME CLIENTE"])["QTD ITEM"]
        .sum()
        .reset_index()
        .sort_values(by=["AnoMes", "QTD ITEM"], ascending=[True, False])
    )
    return resultado


def ranking_fornecedores_estoque_mes(dados):
    estoque = dados["Cadastro de Estoque"]
    fornecedores = dados["Cadastro Fornecedores"]

    estoque["DATA ESTOQUE"] = pd.to_datetime(estoque["DATA ESTOQUE"])
    estoque["AnoMes"] = estoque["DATA ESTOQUE"].dt.to_period("M")

    merged = estoque.merge(fornecedores, on="ID FORNECEDOR")
    resultado = (
        merged.groupby(["AnoMes", "NOME FORNECEDOR"])["QTD ESTOQUE"]
        .sum()
        .reset_index()
        .sort_values(by=["AnoMes", "QTD ESTOQUE"], ascending=[True, False])
    )
    return resultado


def ranking_produtos_qtd_vendida_mes(dados):
    transacoes = dados["Transações Vendas"]

    transacoes["DATA NOTA"] = pd.to_datetime(transacoes["DATA NOTA"])
    transacoes["AnoMes"] = transacoes["DATA NOTA"].dt.to_period("M")

    resultado = (
        transacoes.groupby(["AnoMes", "ID PRODUTO"])["QTD ITEM"]
        .sum()
        .reset_index()
        .sort_values(by=["AnoMes", "QTD ITEM"], ascending=[True, False])
    )
    return resultado


def ranking_produtos_valor_venda_mes(dados):
    transacoes = dados["Transações Vendas"]

    transacoes["DATA NOTA"] = pd.to_datetime(transacoes["DATA NOTA"])
    transacoes["AnoMes"] = transacoes["DATA NOTA"].dt.to_period("M")
    transacoes["VALOR ITEM"] = transacoes["VALOR ITEM"].astype(str).replace('[R$ ]', '', regex=True).str.replace('.', '').str.replace(',', '.').astype(float)

    resultado = (
        transacoes.groupby(["AnoMes", "ID PRODUTO"])["VALOR ITEM"]
        .sum()
        .reset_index()
        .sort_values(by=["AnoMes", "VALOR ITEM"], ascending=[True, False])
    )
    return resultado


def media_valor_venda_categoria_mes(dados):
    produtos = dados["Cadastro Produtos"]
    transacoes = dados["Transações Vendas"]

    transacoes["DATA NOTA"] = pd.to_datetime(transacoes["DATA NOTA"])
    transacoes["AnoMes"] = transacoes["DATA NOTA"].dt.to_period("M")
    transacoes["VALOR ITEM"] = transacoes["VALOR ITEM"].astype(str).replace('[R$ ]', '', regex=True).str.replace('.', '').str.replace(',', '.').astype(float)

    merged = transacoes.merge(produtos, on="ID PRODUTO")
    resultado = (
        merged.groupby(["AnoMes", "CATEGORIA"])["VALOR ITEM"]
        .mean()
        .reset_index()
        .sort_values(by=["AnoMes", "VALOR ITEM"], ascending=[True, False])
    )
    return resultado


def ranking_margem_por_categoria(dados):
    produtos = dados["Cadastro Produtos"]
    transacoes = dados["Transações Vendas"]
    estoque = dados["Cadastro de Estoque"]

    transacoes["VALOR ITEM"] = transacoes["VALOR ITEM"].astype(str).replace('[R$ ]', '', regex=True).str.replace('.', '').str.replace(',', '.').astype(float)
    estoque["VALOR ESTOQUE"] = estoque["VALOR ESTOQUE"].astype(str).replace('[R$ ]', '', regex=True).str.replace('.', '').str.replace(',', '.').astype(float)

    merged = transacoes.merge(produtos, on="ID PRODUTO").merge(estoque, on="ID ESTOQUE", how="left")
    merged["margem"] = merged["VALOR ITEM"] - (merged["VALOR ESTOQUE"] / merged["QTD ESTOQUE"])

    resultado = (
        merged.groupby("CATEGORIA")["margem"]
        .mean()
        .reset_index()
        .sort_values(by="margem", ascending=False)
    )
    return resultado


def produtos_por_cliente(dados):
    transacoes = dados["Transações Vendas"]
    clientes = dados["Cadastro Clientes"]
    produtos = dados["Cadastro Produtos"]

    merged = transacoes.merge(clientes, on="ID CLIENTE").merge(produtos, on="ID PRODUTO")
    resultado = (
        merged.groupby("NOME CLIENTE")["NOME PRODUTO"]
        .unique()
        .reset_index()
        .rename(columns={"NOME PRODUTO": "Produtos Comprados"})
    )
    return resultado


def ranking_produtos_qtd_estoque(dados):
    estoque = dados["Cadastro de Estoque"]
    produtos = dados["Cadastro Produtos"]

    merged = estoque.merge(produtos, on="ID ESTOQUE")
    resultado = (
        merged.groupby("NOME PRODUTO")["QTD ESTOQUE"]
        .sum()
        .reset_index()
        .sort_values(by="QTD ESTOQUE", ascending=False)
    )
    return resultado
