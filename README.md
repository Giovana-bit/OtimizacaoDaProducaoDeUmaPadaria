# 🥖 Otimização da Produção de uma Padaria

Projeto desenvolvido para a disciplina de **Pesquisa Operacional**, com o objetivo de aplicar conceitos de Programação Linear Inteira na otimização da produção de uma padaria fictícia.

A aplicação utiliza Python e a biblioteca PuLP para encontrar a combinação ideal de produção de pães e bolos, buscando maximizar o lucro diário e respeitar os recursos disponíveis.

## 🎯 Objetivo do projeto

Desenvolver um modelo matemático e computacional capaz de auxiliar no planejamento da produção de uma padaria, identificando quantos lotes de pães e bolos devem ser produzidos para obter o maior lucro possível.

O modelo considera limitações de matéria-prima, mão de obra, tempo de forno e demanda dos produtos.

## 🛠️ Tecnologias utilizadas

- **Python:** linguagem utilizada para desenvolver a aplicação.
- **PuLP:** biblioteca utilizada para modelagem e resolução do problema de otimização.
- **Programação Linear Inteira:** método matemático utilizado para encontrar a solução ótima.
- **VS Code:** ambiente de desenvolvimento utilizado para escrever e executar o código.
- **Streamlit:** tecnologia utilizada na versão com interface visual (Front-end).

## 📊 Descrição do problema

A padaria trabalha com dois produtos:

- Pães: cada lote representa 100 unidades.
- Bolos: cada lote representa 10 unidades.

Os dados utilizados são fictícios e foram definidos para representar uma situação hipotética de produção.

### Dados do modelo

| Informação | Pães | Bolos |
|---|---:|---:|
| Lucro por lote | R$ 80 | R$ 150 |
| Farinha por lote | 5 kg | 4 kg |
| Mão de obra por lote | 2 horas | 3 horas |
| Tempo de forno por lote | 1 hora | 2 horas |
| Demanda máxima | 15 lotes | 10 lotes |

### Recursos disponíveis

- Farinha: 100 kg.
- Mão de obra: 40 horas.
- Tempo de forno: 30 horas.

## 🧮 Modelo matemático

As variáveis de decisão são:

- **X:** quantidade de lotes de pães.
- **Y:** quantidade de lotes de bolos.

### Função objetivo

Maximizar o lucro total:

`Max Z = 80X + 150Y`

### Restrições

```text
5X + 4Y <= 100  (Farinha)

2X + 3Y <= 40   (Mão de obra)

X + 2Y <= 30    (Tempo de forno)

X <= 15         (Demanda de pães)

Y <= 10         (Demanda de bolos)

X, Y >= 0 e inteiros
```

## 💻 Funcionamento da aplicação

O programa realiza as seguintes etapas:

1. Construção do modelo computacional.
2. Definição das variáveis de decisão.
3. Configuração da função objetivo.
4. Configuração das restrições de recursos e demanda.
5. Execução do algoritmo de otimização.
6. Identificação da solução ótima.
7. Apresentação dos resultados.
8. Interpretação dos resultados.
9. Recomendações práticas para a produção.
10. Discussão das limitações e oportunidades de melhoria.

## 📈 Resultados obtidos

Após a execução do modelo com os dados definidos, a solução ótima encontrada é:

| Indicador | Resultado |
|---|---:|
| Lotes de pães | 5 |
| Quantidade de pães | 500 unidades |
| Lotes de bolos | 10 |
| Quantidade de bolos | 100 unidades |
| **Lucro máximo diário** | **R$ 1.900,00** |

### Utilização dos recursos

| Recurso | Utilizado | Disponível | Sobra |
|---|---:|---:|---:|
| Farinha | 65 kg | 100 kg | 35 kg |
| Mão de obra | 40 h | 40 h | 0 h |
| Forno | 25 h | 30 h | 5 h |

A solução demonstra que a produção de 500 pães e 100 bolos proporciona o maior lucro possível dentro das condições estabelecidas.

A mão de obra é totalmente utilizada, enquanto ainda existe disponibilidade de farinha e tempo de forno.

## 💡 Interpretação e recomendações

Com base nos resultados, recomenda-se utilizar a solução encontrada como referência para o planejamento diário da produção.

Também é importante monitorar a disponibilidade de mão de obra, pois esse é o recurso totalmente utilizado no cenário estudado.

A padaria pode avaliar futuras mudanças na organização dos turnos ou na equipe, caso exista demanda adicional e viabilidade financeira.

## ⚠️ Limitações e melhorias futuras

O modelo apresenta algumas limitações:

- Utiliza dados fictícios.
- Considera os lucros e recursos como valores fixos.
- Não considera perdas de matéria-prima.
- Não considera estoque ou produtos não vendidos.
- Não considera variações na demanda ao longo do tempo.

Como melhorias futuras, o projeto poderá incluir:

- Dados reais de vendas e custos.
- Novos produtos.
- Controle de estoque.
- Variação de demanda.
- Planejamento de diferentes turnos.
- Interface visual para facilitar a utilização do sistema.

## ▶️ Como executar o projeto

### 1. Pré-requisitos

- Python instalado.
- Visual Studio Code instalado.

### 2. Instalar as dependências

Abra o terminal na pasta do projeto e execute:

```bash
python -m pip install pulp==2.9.0 streamlit==1.41.1
```

### 3. Executar a versão Python

```bash
python parte_pratica_padaria.py
```

### 4. Executar a versão com Front-end

Caso esteja utilizando o arquivo `app_padaria.py`, execute:

```bash
python -m streamlit run app_padaria.py
```

A interface será aberta no navegador.

## 📁 Estrutura do projeto

```text
otimizacao-padaria/
│
├── parte_pratica_padaria.py
│
├── app_padaria.py
│
├── requirements.txt
│
└── README.md
```

## 📚 Finalidade acadêmica

Este projeto foi desenvolvido como atividade acadêmica da disciplina de Pesquisa Operacional, com a finalidade de demonstrar a aplicação de técnicas matemáticas e computacionais na resolução de problemas de otimização.

A experiência permite compreender como a Programação Linear Inteira pode auxiliar na tomada de decisões, no planejamento de recursos e na maximização dos resultados de uma organização.

---

**Projeto acadêmico — Otimização da Produção de uma Padaria**

Desenvolvido em Python utilizando Programação Linear Inteira e a biblioteca PuLP.