def gerar_relatorio_simples(dados):
    """
    Gera um relatório simples exibindo informações básicas sobre produtos e clientes.

    Parâmetros:
        dados (dict): Um dicionário contendo DataFrames com as chaves "produtos" e "clientes".
            - "produtos": DataFrame com colunas "ID Produto", "Nome Produto" e "Categoria".
            - "clientes": DataFrame com colunas "ID Cliente" e "Nome Cliente".

    Instruções:
        - O relatório imprime no console os primeiros registros dos produtos e clientes cadastrados.
        - Apenas as colunas principais são exibidas para cada categoria.
    """
    produtos = dados["produtos"]
    print("\n📦 Produtos Cadastrados:")
    print(produtos[["ID Produto", "Nome Produto", "Categoria"]].head())

    clientes = dados["clientes"]
    print("\n👤 Clientes Cadastrados:")
    print(clientes[["ID Cliente", "Nome Cliente"]].head())
