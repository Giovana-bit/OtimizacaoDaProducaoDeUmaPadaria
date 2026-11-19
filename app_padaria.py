import streamlit as st
import pulp

st.set_page_config(page_title="Otimização da Padaria", page_icon="🥖", layout="centered")

st.title("🥖 Otimização da Produção da Padaria")
st.write(
    "Aplicativo para encontrar a quantidade de lotes de pães e bolos "
    "que maximiza o lucro, respeitando os recursos disponiveis."
)

with st.sidebar:
    st.header("Dados do problema")
    lucro_paes = st.number_input("Lucro por lote de pães (R$)", min_value=0.0, value=80.0, step=5.0)
    lucro_bolos = st.number_input("Lucro por lote de bolos (R$)", min_value=0.0, value=150.0, step=5.0)
    farinha_total = st.number_input("Farinha disponivel (kg)", min_value=0.0, value=100.0, step=5.0)
    mao_obra_total = st.number_input("Mao de obra disponivel (horas)", min_value=0.0, value=40.0, step=1.0)
    forno_total = st.number_input("Tempo de forno disponivel (horas)", min_value=0.0, value=30.0, step=1.0)
    demanda_paes = st.number_input("Limite de lotes de pães", min_value=0, value=15, step=1)
    demanda_bolos = st.number_input("Limite de lotes de bolos", min_value=0, value=10, step=1)

st.subheader("Consumo de recursos por lote")
st.markdown("- Paes: 5 kg de farinha, 2 horas de trabalho e 1 hora de forno.")
st.markdown("- Bolos: 4 kg de farinha, 3 horas de trabalho e 2 horas de forno.")
st.caption("Um lote corresponde a 100 paes ou 10 bolos. As quantidades de lotes sao inteiras.")

if st.button("Calcular producao ideal", type="primary", use_container_width=True):
    modelo = pulp.LpProblem("Otimizacao_Producao_Padaria", pulp.LpMaximize)
    paes = pulp.LpVariable("Lotes_de_paes", lowBound=0, upBound=demanda_paes, cat=pulp.LpInteger)
    bolos = pulp.LpVariable("Lotes_de_bolos", lowBound=0, upBound=demanda_bolos, cat=pulp.LpInteger)

    modelo += lucro_paes * paes + lucro_bolos * bolos
    modelo += 5 * paes + 4 * bolos <= farinha_total
    modelo += 2 * paes + 3 * bolos <= mao_obra_total
    modelo += paes + 2 * bolos <= forno_total

    resultado = modelo.solve(pulp.PULP_CBC_CMD(msg=False))
    status = pulp.LpStatus[resultado]

    if status == "Optimal":
        x = int(round(pulp.value(paes)))
        y = int(round(pulp.value(bolos)))
        lucro = pulp.value(modelo.objective)

        st.success("Solucao otima encontrada!")
        c1, c2, c3 = st.columns(3)
        c1.metric("Lotes de paes", x)
        c2.metric("Lotes de bolos", y)
        c3.metric("Lucro maximo", f"R$ {lucro:,.2f}")

        st.subheader("Producao recomendada")
        st.write(f"- Paes: **{x * 100} unidades** ({x} lotes)")
        st.write(f"- Bolos: **{y * 10} unidades** ({y} lotes)")

        farinha_usada = 5*x + 4*y
        trabalho_usado = 2*x + 3*y
        forno_usado = x + 2*y

        st.subheader("Utilizacao dos recursos")
        st.write(f"Farinha: {farinha_usada:g} de {farinha_total:g} kg")
        st.progress(min(1.0, farinha_usada / farinha_total) if farinha_total else 0.0)
        st.write(f"Trabalho: {trabalho_usado:g} de {mao_obra_total:g} horas")
        st.progress(min(1.0, trabalho_usado / mao_obra_total) if mao_obra_total else 0.0)
        st.write(f"Forno: {forno_usado:g} de {forno_total:g} horas")
        st.progress(min(1.0, forno_usado / forno_total) if forno_total else 0.0)

        st.info(
            f"Recursos restantes: {farinha_total - farinha_usada:g} kg de farinha, "
            f"{mao_obra_total - trabalho_usado:g} horas de trabalho e "
            f"{forno_total - forno_usado:g} horas de forno."
        )
    else:
        st.error(f"Nao foi possivel encontrar uma solucao otima. Status: {status}")

st.divider()
st.caption("Modelo de Programacao Linear Inteira desenvolvido para fins academicos.")
