# CDPeers-Group-Case-Digital

## Desafio de Análise de Dados - Infomaz

## Contexto

A Infomaz, uma empresa especializada em artigos eletrônicos e de informática, tem observado mudanças no comportamento de compra de seus clientes. Nos últimos meses, houve uma variação significativa nas vendas de algumas categorias de produtos, e a empresa precisa entender melhor esses padrões para otimizar seu estoque, melhorar a relação com fornecedores e maximizar seus lucros.

Nosso cliente quer responder à seguinte questão:

> **Quais produtos e categorias apresentam maior e menor rentabilidade, e como podemos otimizar nossas estratégias de fornecimento e precificação para maximizar os lucros?**

## Entrega

- **Data limite:** 16/05/2025 23:59
- A próxima reunião será agendada e comunicada pela equipe de recrutamento.
- No dia marcado, cada grupo terá 20 minutos para responder aos desafios anteriores com base nas métricas calculadas e apresentar uma exposição de 10 minutos para os avaliadores.
- As respostas devem ser obrigatoriamente desenvolvidas em uma linguagem de programação à escolha do participante.
- Os códigos desenvolvidos devem ser enviados por e-mail dentro do prazo de 3 dias.
- Não é necessário enviar uma apresentação em PPT.

## Métricas a serem calculadas

1. **Valor total de venda dos produtos por categoria**  
    Utilize as tabelas `CADASTRO_PRODUTOS` e `TRANSACOES_VENDAS`.

2. **Margem dos produtos**  
    Calcule subtraindo o valor unitário pelo valor de venda. Utilize as tabelas `CADASTRO_ESTOQUE` e `TRANSACOES_VENDAS`.

3. **Ranking de clientes por quantidade de produtos comprados por mês**  
    Utilize as tabelas `CADASTRO_CLIENTES` e `TRANSACOES_VENDAS`.

4. **Ranking de fornecedores por quantidade de estoque disponível por mês**  
    Utilize as tabelas `CADASTRO_FORNECEDORES` e `CADASTRO_ESTOQUE`.

5. **Ranking de produtos por quantidade de venda por mês**  
    Utilize a tabela `TRANSACOES_VENDAS`.

6. **Ranking de produtos por valor de venda por mês**  
    Utilize a tabela `TRANSACOES_VENDAS`.

7. **Média de valor de venda por categoria de produto por mês**  
    Utilize as tabelas `CADASTRO_PRODUTOS` e `TRANSACOES_VENDAS`.

8. **Ranking de margem de lucro por categoria**

9. **Lista de produtos comprados por clientes**

10. **Ranking de produtos por quantidade de estoque**

---

Bom trabalho!

---

---

## 📁 Estrutura do Projeto

Abaixo está uma sugestão da estrutura de pastas e arquivos sobre o projeto:

```
informaz-analise/
├── main.py
├── requirements.txt
├── README.md
├── data/
│   ├── Case_Infomaz_Base_de_Dados.xlsx
│   └── Orientações.csv
├── src/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── calculos.py
│   ├── load_data.py
│   └── relatorios.py
└── venv/
    └── [arquivos do ambiente virtual]
```

- **main.py**: script principal para execução do projeto
- **requirements.txt**: dependências do projeto
- **README.md**: documentação do projeto
- **data/**: arquivos de dados fornecidos
- **src/**: scripts Python para cálculos, carregamento de dados e geração de relatórios
- **venv/**: ambiente virtual Python (não versionar os arquivos internos)
- **src/__pycache__/**: arquivos compilados automaticamente pelo Python (não versionar)

Adapte conforme a necessidade do seu grupo e do desafio.

---


---

# CDPeers-Group-Case-Digital

## Documentação do projeto

## 🚀 Como instalar as dependências e executar o projeto

Siga os passos abaixo para instalar as dependências e rodar o projeto:

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd informaz-analise
```

### 2. Crie e ative um ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o arquivo principal

```bash
python main.py
```

Pronto! O projeto estará rodando e você poderá analisar os dados conforme as instruções do desafio.
