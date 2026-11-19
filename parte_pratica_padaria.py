
"""
TRABALHO DE PESQUISA OPERACIONAL
Otimização da produção de uma padaria

Modelo: Programação Linear Inteira
Objetivo: Maximização do lucro diário.

Como executar no VS Code:
1. Instale o Python.
2. Abra o terminal do VS Code na pasta do arquivo.
3. Execute: python -m pip install pulp==2.9.0
4. Execute: python parte_pratica_padaria.py

Observação:
Os dados são sintéticos (fictícios), conforme definido na parte teórica.
Cada lote representa 100 unidades de pão ou 10 bolos.
"""

import pulp


def resolver_modelo():

    # 1. CONSTRUÇÃO DO MODELO COMPUTACIONAL

    modelo = pulp.LpProblem(
        "Otimizacao_Producao_Padaria",
        pulp.LpMaximize
    )

    # Variáveis de decisão:
    # X = quantidade de lotes de pães
    # Y = quantidade de lotes de bolos

    paes = pulp.LpVariable(
        "Lotes_de_paes",
        lowBound=0,
        cat=pulp.LpInteger
    )

    bolos = pulp.LpVariable(
        "Lotes_de_bolos",
        lowBound=0,
        cat=pulp.LpInteger
    )

    # 2. FUNÇÃO OBJETIVO E RESTRIÇÕES
    # Maximizar o lucro diário
    modelo += 80 * paes + 150 * bolos, "Lucro_Total"

    # Restrições de recursos disponíveis
    modelo += 5 * paes + 4 * bolos <= 100, "Farinha"
    modelo += 2 * paes + 3 * bolos <= 40, "Mao_de_obra"
    modelo += paes + 2 * bolos <= 30, "Forno"

    # Restrições de demanda
    modelo += paes <= 15, "Demanda_paes"
    modelo += bolos <= 10, "Demanda_bolos"

    # 3. EXECUÇÃO DO MODELO E SOLUÇÃO ÓTIMA

    modelo.solve(pulp.PULP_CBC_CMD(msg=False))

    status = pulp.LpStatus[modelo.status]

    print("\n" + "=" * 65)
    print("OTIMIZAÇÃO DA PRODUÇÃO DE UMA PADARIA")
    print("=" * 65)

    print("\n1. CONSTRUÇÃO DO MODELO COMPUTACIONAL")
    print("Método utilizado: Programação Linear Inteira")
    print("Objetivo: Maximizar o lucro diário da padaria.")
    print("Variáveis: quantidade de lotes de pães e bolos.")

    print("\n2. FUNÇÃO OBJETIVO")
    print("Maximizar Z = 80X + 150Y")

    print("\nRestrições:")
    print("5X + 4Y <= 100 (Farinha)")
    print("2X + 3Y <= 40 (Mão de obra)")
    print("X + 2Y <= 30 (Forno)")
    print("X <= 15 (Demanda de pães)")
    print("Y <= 10 (Demanda de bolos)")
    print("X, Y >= 0 e inteiros")

    print("\n3. EXECUÇÃO DO MODELO")
    print(f"Status da solução: {status}")

    if status != "Optimal":
        print("Não foi encontrada uma solução ótima.")
        print("Verifique os dados e as configurações do modelo.")
        return

    # Obtenção da solução
    qtd_paes = int(round(pulp.value(paes)))
    qtd_bolos = int(round(pulp.value(bolos)))
    lucro = pulp.value(modelo.objective)

    # Conversão de lotes para unidades
    unidades_paes = qtd_paes * 100
    unidades_bolos = qtd_bolos * 10

    # Consumo dos recursos
    farinha_usada = 5 * qtd_paes + 4 * qtd_bolos
    mao_de_obra_usada = 2 * qtd_paes + 3 * qtd_bolos
    forno_usado = qtd_paes + 2 * qtd_bolos

    # Recursos restantes
    farinha_sobra = 100 - farinha_usada
    mao_de_obra_sobra = 40 - mao_de_obra_usada
    forno_sobra = 30 - forno_usado

    # 4. APRESENTAÇÃO DOS RESULTADOS

    print("\n4. RESULTADOS OBTIDOS")
    print("-" * 65)

    print("\nPLANO DE PRODUÇÃO RECOMENDADO")
    print(f"Lotes de pães: {qtd_paes} ({unidades_paes} unidades)")
    print(f"Lotes de bolos: {qtd_bolos} ({unidades_bolos} unidades)")

    print(
        "\nLucro diário máximo: R$ "
        + f"{lucro:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

    print("\nUTILIZAÇÃO DOS RECURSOS")

    print(
        f"Farinha: {farinha_usada} kg de 100 kg "
        f"(sobra: {farinha_sobra} kg)"
    )

    print(
        f"Mão de obra: {mao_de_obra_usada} h de 40 h "
        f"(sobra: {mao_de_obra_sobra} h)"
    )

    print(
        f"Forno: {forno_usado} h de 30 h "
        f"(sobra: {forno_sobra} h)"
    )

    print("\nVERIFICAÇÃO DAS RESTRIÇÕES")
    print(f"Demanda de pães: {qtd_paes} de 15 lotes")
    print(f"Demanda de bolos: {qtd_bolos} de 10 lotes")

    print("\n5. INTERPRETAÇÃO DOS RESULTADOS")
    print("-" * 65)

    print(
        f"A solução ótima indica a produção de {unidades_paes} pães "
        f"e {unidades_bolos} bolos por dia."
    )

    print(
        f"Essa combinação proporciona um lucro máximo estimado "
        f"de R$ {lucro:,.2f}."
    )

    print(
        "A mão de obra é totalmente utilizada, sendo o recurso "
        "que limita a produção neste cenário."
    )

    print(
        "A farinha apresenta sobra de 35 kg e o forno apresenta "
        "5 horas disponíveis."
    )

    print(
        "O limite de demanda de bolos também é atingido, indicando "
        "que o modelo respeita a quantidade máxima prevista para venda."
    )

    print("\n6. RECOMENDAÇÕES PRÁTICAS")
    print("-" * 65)

    print(
        "1. Utilizar o plano de produção encontrado como referência "
        "para organizar a produção diária."
    )

    print(
        "2. Monitorar a disponibilidade de mão de obra, pois ela "
        "é totalmente utilizada."
    )

    print(
        "3. Avaliar a possibilidade de reorganizar os horários ou "
        "ampliar a equipe caso exista demanda adicional."
    )

    print(
        "4. Acompanhar as vendas reais para evitar produção excessiva "
        "e desperdício de alimentos."
    )

    print(
        "5. Aproveitar a capacidade restante de farinha e forno "
        "em possíveis ajustes futuros na produção."
    )

    print("\n7. LIMITAÇÕES E OPORTUNIDADES DE MELHORIA")
    print("-" * 65)

    print(
        "1. Os dados utilizados são sintéticos e representam "
        "uma situação hipotética."
    )

    print(
        "2. O modelo considera os lucros e os recursos disponíveis "
        "como valores fixos."
    )

    print(
        "3. Não são consideradas perdas de matéria-prima, "
        "estoques ou produtos que não sejam vendidos."
    )

    print(
        "4. A demanda pode variar conforme o dia, a época do ano "
        "e o comportamento dos consumidores."
    )

    print(
        "5. Como melhoria, podem ser utilizados dados reais de vendas, "
        "custos, preços e consumo de recursos."
    )

    print(
        "6. O modelo também pode ser ampliado para incluir novos "
        "produtos, turnos de trabalho, estoques e variações de demanda."
    )

    # CONCLUSÃO

    print("\nCONCLUSÃO GERAL")
    print("-" * 65)

    print(
        "O modelo de Pesquisa Operacional permitiu identificar "
        "uma combinação de produção que maximiza o lucro da padaria "
        "respeitando os limites de recursos e demanda estabelecidos."
    )

    print(
        "Dessa forma, a programação linear inteira demonstra como "
        "a matemática e a computação podem auxiliar no planejamento "
        "da produção e na tomada de decisões."
    )

    print("\n" + "=" * 65)
    print("FIM DA EXECUÇÃO DO MODELO")
    print("=" * 65)


# Execução principal do programa
if __name__ == "__main__":
    resolver_modelo()