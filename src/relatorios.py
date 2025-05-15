def gerar_relatorio_simples(dados):
    produtos = dados["produtos"]
    print("\n📦 Produtos Cadastrados:")
    print(produtos[["ID Produto", "Nome Produto", "Categoria"]].head())

    clientes = dados["clientes"]
    print("\n👤 Clientes Cadastrados:")
    print(clientes[["ID Cliente", "Nome Cliente"]].head())
