# CDPeers-Group-Case-Digital# Documentação do projeto

# Desafio de Análise de Dados - Infomaz

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

Para desenvolver uma solução em Python para esse desafio de análise de dados da Infomaz, você pode seguir uma abordagem estruturada utilizando **pandas** para manipulação e análise dos dados. Aqui está uma base do que você pode fazer:

---

## ✅ Pré-requisitos

Instale as bibliotecas necessárias:

```bash
pip install pandas
```

---

## ✅ Estrutura inicial em Python

### 1. Carregamento dos dados

Suponha que os dados estejam em arquivos `.csv`:

```python
import pandas as pd

# Carregar as tabelas
produtos = pd.read_csv('CADASTRO_PRODUTOS.csv')
vendas = pd.read_csv('TRANSACOES_VENDAS.csv')
estoque = pd.read_csv('CADASTRO_ESTOQUE.csv')
clientes = pd.read_csv('CADASTRO_CLIENTES.csv')
fornecedores = pd.read_csv('CADASTRO_FORNECEDORES.csv')
```

---

### 2. Métricas e Cálculos

#### 1. **Valor total de venda dos produtos por categoria**

```python
df = vendas.merge(produtos, on='id_produto')
valor_total_categoria = df.groupby('categoria')['valor_venda'].sum().reset_index()
```

#### 2. **Margem dos produtos (valor de venda - valor unitário)**

```python
df = vendas.merge(estoque[['id_produto', 'valor_unitario']], on='id_produto')
df['margem'] = df['valor_venda'] - df['valor_unitario']
```

#### 3. **Ranking de clientes por quantidade de produtos comprados por mês**

```python
vendas['mes'] = pd.to_datetime(vendas['data_venda']).dt.to_period('M')
ranking_clientes = vendas.groupby(['mes', 'id_cliente'])['quantidade'].sum().reset_index()
ranking_clientes = ranking_clientes.sort_values(['mes', 'quantidade'], ascending=[True, False])
```

#### 4. **Ranking de fornecedores por estoque disponível por mês**

```python
estoque['mes'] = pd.to_datetime(estoque['data_entrada']).dt.to_period('M')
ranking_fornecedores = estoque.groupby(['mes', 'id_fornecedor'])['quantidade_estoque'].sum().reset_index()
ranking_fornecedores = ranking_fornecedores.sort_values(['mes', 'quantidade_estoque'], ascending=[True, False])
```

#### 5. **Ranking de produtos por quantidade de venda por mês**

```python
vendas['mes'] = pd.to_datetime(vendas['data_venda']).dt.to_period('M')
ranking_produtos_qtd = vendas.groupby(['mes', 'id_produto'])['quantidade'].sum().reset_index()
ranking_produtos_qtd = ranking_produtos_qtd.sort_values(['mes', 'quantidade'], ascending=[True, False])
```

#### 6. **Ranking de produtos por valor de venda por mês**

```python
ranking_produtos_valor = vendas.groupby(['mes', 'id_produto'])['valor_venda'].sum().reset_index()
ranking_produtos_valor = ranking_produtos_valor.sort_values(['mes', 'valor_venda'], ascending=[True, False])
```

#### 7. **Média de valor de venda por categoria por mês**

```python
df = vendas.merge(produtos, on='id_produto')
df['mes'] = pd.to_datetime(df['data_venda']).dt.to_period('M')
media_valor_categoria = df.groupby(['mes', 'categoria'])['valor_venda'].mean().reset_index()
```

#### 8. **Ranking de margem de lucro por categoria**

```python
df = df.merge(estoque[['id_produto', 'valor_unitario']], on='id_produto')
df['margem'] = df['valor_venda'] - df['valor_unitario']
ranking_margem_categoria = df.groupby('categoria')['margem'].mean().reset_index().sort_values(by='margem', ascending=False)
```

#### 9. **Lista de produtos comprados por cliente**

```python
produtos_por_cliente = vendas.merge(produtos, on='id_produto')
lista_produtos_clientes = produtos_por_cliente.groupby('id_cliente')['nome_produto'].unique().reset_index()
```

#### 10. **Ranking de produtos por quantidade de estoque**

```python
ranking_estoque = estoque.groupby('id_produto')['quantidade_estoque'].sum().reset_index().sort_values(by='quantidade_estoque', ascending=False)
```

---

1️⃣ Usar um Ambiente Virtual (Recomendado)
Você pode criar um ambiente virtual e instalar os pacotes dentro dele:
[source venv/bin/activate
]
bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Isso cria uma pasta venv onde os pacotes são gerenciados independentemente do sistema.