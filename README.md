# 🧮 Calculadoras Python

Três ferramentas de cálculo desenvolvidas em Python: duas com interface desktop (CustomTkinter) e uma versão web com Streamlit.

---

## 📁 Estrutura do projeto

```
├── calculadora.py       # Calculadora desktop (4 operações básicas + exponenciação e módulo)
├── imc.py               # Calculadora de IMC desktop (tela cheia, classificação OMS)
├── calculadora_web.py   # Calculadora web com Streamlit (deploy no Streamlit Cloud)
├── requirements.txt     # Dependências do projeto
└── .gitignore
```

---

## ⚙️ Pré-requisitos

- Python 3.10 ou superior
- pip

---

## 🖥️ Calculadora Desktop — `calculadora.py`

Interface gráfica com tema escuro usando CustomTkinter. Suporta 6 operações: adição, subtração, multiplicação, divisão, exponenciação e módulo.

### Instalação

```bash
pip install customtkinter
```

### Como rodar

```bash
python calculadora.py
```

---

## 🏋️ Calculadora de IMC — `imc.py`

Interface desktop em tela cheia com tema escuro. Aceita altura em centímetros ou metros e classifica o resultado seguindo a tabela da OMS com feedback visual por cores.

**Classificações:**
| IMC | Classificação |
|-----|--------------|
| < 18.5 | Abaixo do peso |
| 18.5 – 24.9 | Peso normal |
| 25.0 – 29.9 | Sobrepeso |
| 30.0 – 34.9 | Obesidade Grau I |
| 35.0 – 39.9 | Obesidade Grau II |
| ≥ 40.0 | Obesidade Grau III (Mórbida) |

### Instalação

```bash
pip install customtkinter
```

### Como rodar

```bash
python imc.py
```

---

## 🌐 Calculadora Web — `calculadora_web.py`

Versão web da calculadora usando Streamlit. Suporta 8 operações: adição, subtração, multiplicação, divisão, exponenciação, módulo, raiz quadrada e porcentagem.

### Instalação

```bash
pip install streamlit
```

### Como rodar localmente

```bash
streamlit run calculadora_web.py
```

> ⚠️ **Windows:** Se o comando `streamlit` não for reconhecido, use:
> ```bash
> python -m streamlit run calculadora_web.py
> ```
> Isso acontece quando o Python foi instalado sem adicionar os scripts ao PATH do sistema.

Acesse no navegador: `http://localhost:8501`

### Deploy no Streamlit Community Cloud

1. Suba o projeto em um repositório público no GitHub
2. Crie um arquivo `requirements.txt` com apenas:
   ```
   streamlit
   ```
3. Acesse [share.streamlit.io](https://share.streamlit.io)
4. Conecte seu repositório GitHub e aponte o arquivo principal para `calculadora_web.py`
5. Clique em **Deploy**


---

## 📦 Instalando todas as dependências de uma vez (ambiente local)

```bash
pip install -r requirements.txt
```

---

## 🛠️ Tecnologias

- [Python](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Streamlit](https://streamlit.io/)
