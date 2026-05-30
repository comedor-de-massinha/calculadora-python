import streamlit as st
import math

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Calculadora Web",
    page_icon="🧮",
    layout="centered"
)

# ==========================================
# ESTILO PERSONALIZADO
# ==========================================
st.markdown("""
    <style>
        .main {
            background-color: #0f172a;
        }

        .titulo {
            text-align: center;
            color: white;
            font-size: 42px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .subtitulo {
            text-align: center;
            color: #94a3b8;
            margin-bottom: 30px;
        }

        .resultado {
            background-color: #1e293b;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            color: #38bdf8;
            font-size: 28px;
            font-weight: bold;
            margin-top: 30px;
            border: 1px solid #334155;
        }

        .stButton>button {
            width: 100%;
            height: 50px;
            border-radius: 12px;
            background-color: #2563eb;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border: none;
        }

        .stButton>button:hover {
            background-color: #1d4ed8;
        }        .github-btn {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 10px 16px;
            border-radius: 12px;
            background-color: #111827;
            color: #ffffff;
            text-decoration: none;
            font-weight: 700;
            border: 1px solid #334155;
            transition: background-color 0.15s ease;
        }
        .github-btn:hover {
            background-color: #1f2937;
        }    </style>
""", unsafe_allow_html=True)

# ==========================================
# TÍTULO
# ==========================================
st.markdown(
    '<div class="titulo">🧮 Calculadora Web</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="display: flex; justify-content: center; margin-bottom: 24px;"><a href="https://github.com/comedor-de-massinha/calculadora-python" target="_blank" rel="noopener noreferrer" class="github-btn"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M12 0a12 12 0 00-3.79 23.4c.6.11.82-.26.82-.58v-2.1c-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.33-1.76-1.33-1.76-1.09-.74.08-.73.08-.73 1.2.08 1.84 1.24 1.84 1.24 1.07 1.84 2.81 1.3 3.49 1 .11-.78.42-1.3.76-1.61-2.67-.3-5.47-1.33-5.47-5.93 0-1.31.47-2.38 1.24-3.22-.12-.3-.54-1.52.12-3.18 0 0 1.01-.32 3.3 1.23A11.5 11.5 0 0112 6.8c1.02.01 2.05.14 3 .4 2.29-1.55 3.3-1.23 3.3-1.23.65 1.65.24 2.87.12 3.18.77.84 1.24 1.91 1.24 3.22 0 4.6-2.81 5.62-5.48 5.92.42.36.82 1.1.82 2.22v3.29c0 .32.22.7.82.58A12 12 0 0012 0z"/></svg>GitHub</a></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">Calculadora moderna usando Streamlit</div>',
    unsafe_allow_html=True
)

# ==========================================
# CAMPOS
# ==========================================
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input(
        "Primeiro número",
        value=0.0,
        format="%.2f"
    )

with col2:
    num2 = st.number_input(
        "Segundo número",
        value=0.0,
        format="%.2f"
    )

# ==========================================
# OPERAÇÕES
# ==========================================
operacao = st.selectbox(
    "Selecione a operação",
    [
        "Adição",
        "Subtração",
        "Multiplicação",
        "Divisão",
        "Exponenciação",
        "Módulo",
        "Raiz Quadrada",
        "Porcentagem"
    ]
)

# ==========================================
# CÁLCULO
# ==========================================
resultado = None

if st.button("CALCULAR"):

    try:

        if operacao == "Adição":
            resultado = num1 + num2

        elif operacao == "Subtração":
            resultado = num1 - num2

        elif operacao == "Multiplicação":
            resultado = num1 * num2

        elif operacao == "Divisão":
            if num2 == 0:
                st.error("❌ Divisão por zero!")
            else:
                resultado = num1 / num2

        elif operacao == "Exponenciação":
            resultado = num1 ** num2

        elif operacao == "Módulo":
            if num2 == 0:
                st.error("❌ Módulo por zero!")
            else:
                resultado = num1 % num2

        elif operacao == "Raiz Quadrada":
            if num1 < 0:
                st.error("❌ Número negativo!")
            else:
                resultado = math.sqrt(num1)

        elif operacao == "Porcentagem":
            resultado = (num1 * num2) / 100

        # Mostrar resultado
        if resultado is not None:
            st.markdown(
                f'''
                <div class="resultado">
                    Resultado:<br>{resultado}
                </div>
                ''',
                unsafe_allow_html=True
            )

    except Exception as erro:
        st.error(f"Erro: {erro}")

# ==========================================
# RODAPÉ
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)

st.caption("Desenvolvido com Python + Streamlit")