# Instale o customtkinter antes de executar:
# pip install customtkinter

import customtkinter as ctk
from tkinter import messagebox

# Configurações da janela
ctk.set_appearance_mode("dark")  # dark, light ou system
ctk.set_default_color_theme("blue")

# Janela principal
app = ctk.CTk()
app.title("Calculadora")
app.geometry("400x450")

# Função da calculadora
def calcular():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        operacao = operacao_var.get()

        if operacao == "Adição":
            resultado = num1 + num2

        elif operacao == "Subtração":
            resultado = num1 - num2

        elif operacao == "Multiplicação":
            resultado = num1 * num2

        elif operacao == "Divisão":
            if num2 == 0:
                messagebox.showerror("Erro", "Divisão por zero!")
                return
            resultado = num1 / num2

        elif operacao == "Exponenciação":
            resultado = num1 ** num2

        elif operacao == "Módulo":
            if num2 == 0:
                messagebox.showerror("Erro", "Módulo por zero!")
                return
            resultado = num1 % num2

        else:
            messagebox.showwarning("Aviso", "Selecione uma operação!")
            return

        label_resultado.configure(
            text=f"Resultado: {resultado}"
        )

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite números válidos!"
        )

# Título
titulo = ctk.CTkLabel(
    app,
    text="CALCULADORA",
    font=("Arial", 24, "bold")
)
titulo.pack(pady=20)

# Entrada número 1
entrada_num1 = ctk.CTkEntry(
    app,
    placeholder_text="Digite o primeiro número",
    width=250
)
entrada_num1.pack(pady=10)

# Entrada número 2
entrada_num2 = ctk.CTkEntry(
    app,
    placeholder_text="Digite o segundo número",
    width=250
)
entrada_num2.pack(pady=10)

# Seleção de operação
operacao_var = ctk.StringVar(value="Adição")

menu_operacoes = ctk.CTkOptionMenu(
    app,
    values=[
        "Adição",
        "Subtração",
        "Multiplicação",
        "Divisão",
        "Exponenciação",
        "Módulo"
    ],
    variable=operacao_var,
    width=250
)
menu_operacoes.pack(pady=20)

# Botão calcular
botao_calcular = ctk.CTkButton(
    app,
    text="Calcular",
    command=calcular,
    width=200,
    height=40
)
botao_calcular.pack(pady=20)

# Resultado
label_resultado = ctk.CTkLabel(
    app,
    text="Resultado: ",
    font=("Arial", 18)
)
label_resultado.pack(pady=20)

# Executar aplicação
app.mainloop()