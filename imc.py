# ==========================================================
# CALCULADORA DE IMC MODERNA - CUSTOM TKINTER
# ==========================================================
# Requisitos:
# pip install customtkinter
#
# Execute:
# python imc.py
# ==========================================================

import customtkinter as ctk
from tkinter import messagebox
import re

# ---------------- CONFIGURAÇÕES ---------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ---------------- APP PRINCIPAL ---------------- #

class IMCCalculator(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ---------------- JANELA ---------------- #

        self.title("Calculadora de IMC")

        # Tela cheia
        self.state("zoomed")  # Windows

        # Linux/Mac:
        # self.attributes("-fullscreen", True)

        self.configure(fg_color="#0F172A")

        # ---------------- HEADER ---------------- #

        self.title_label = ctk.CTkLabel(
            self,
            text="CALCULADORA DE IMC",
            font=("Poppins", 24, "bold"),
            text_color="#38BDF8"
        )
        self.title_label.pack(pady=(15, 2))

        self.subtitle = ctk.CTkLabel(
            self,
            text="Descubra seu Índice de Massa Corporal",
            font=("Poppins", 13),
            text_color="#CBD5E1"
        )
        self.subtitle.pack(pady=(0, 10))

        # ---------------- CARD PRINCIPAL ---------------- #

        self.card = ctk.CTkFrame(
            self,
            corner_radius=20,
            fg_color="#1E293B",
            border_width=2,
            border_color="#334155"
        )

        self.card.pack(
            padx=25,
            pady=10,
            fill="both",
            expand=True
        )

        # ---------------- TÍTULO INPUT ---------------- #

        self.input_title = ctk.CTkLabel(
            self.card,
            text="Informe seus dados",
            font=("Poppins", 24, "bold"),
            text_color="white"
        )
        self.input_title.pack(pady=(20, 20))

        # ---------------- PESO ---------------- #

        self.weight_label = ctk.CTkLabel(
            self.card,
            text="Peso (kg)",
            font=("Poppins", 16)
        )
        self.weight_label.pack(anchor="w", padx=40)

        self.weight_entry = ctk.CTkEntry(
            self.card,
            placeholder_text="Ex: 70.5",
            height=50,
            corner_radius=12,
            font=("Poppins", 15),
            border_width=2
        )
        self.weight_entry.pack(
            fill="x",
            padx=40,
            pady=(5, 20)
        )

        # ---------------- ALTURA ---------------- #

        self.height_label = ctk.CTkLabel(
            self.card,
            text="Altura (cm ou m)",
            font=("Poppins", 16)
        )
        self.height_label.pack(anchor="w", padx=40)

        self.height_entry = ctk.CTkEntry(
            self.card,
            placeholder_text="Ex: 175 ou 1.75",
            height=50,
            corner_radius=12,
            font=("Poppins", 15),
            border_width=2
        )
        self.height_entry.pack(
            fill="x",
            padx=40,
            pady=(5, 25)
        )

        # ---------------- BOTÕES ---------------- #

        self.button_frame = ctk.CTkFrame(
            self.card,
            fg_color="transparent"
        )
        self.button_frame.pack(pady=10)

        self.calc_button = ctk.CTkButton(
            self.button_frame,
            text="Calcular IMC",
            height=50,
            width=190,
            corner_radius=12,
            fg_color="#06B6D4",
            hover_color="#0891B2",
            font=("Poppins", 16, "bold"),
            command=self.calculate_imc
        )
        self.calc_button.grid(row=0, column=0, padx=10)

        self.clear_button = ctk.CTkButton(
            self.button_frame,
            text="Limpar",
            height=50,
            width=150,
            corner_radius=12,
            fg_color="#EF4444",
            hover_color="#DC2626",
            font=("Poppins", 16, "bold"),
            command=self.clear_fields
        )
        self.clear_button.grid(row=0, column=1, padx=10)

        # ---------------- RESULTADO ---------------- #

        self.result_frame = ctk.CTkFrame(
            self.card,
            corner_radius=18,
            fg_color="#0F172A",
            border_width=2,
            border_color="#334155"
        )

        self.result_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(15, 20)
        )

        # ---------------- TÍTULO RESULTADO ---------------- #

        self.result_title = ctk.CTkLabel(
            self.result_frame,
            text="Seu Resultado",
            font=("Poppins", 22, "bold"),
            text_color="#E2E8F0"
        )
        self.result_title.pack(pady=(20, 10))

        # ---------------- VALOR IMC ---------------- #

        self.imc_value_label = ctk.CTkLabel(
            self.result_frame,
            text="--",
            font=("Poppins", 42, "bold"),
            text_color="#38BDF8"
        )
        self.imc_value_label.pack()

        # ---------------- CLASSIFICAÇÃO ---------------- #

        self.classification_label = ctk.CTkLabel(
            self.result_frame,
            text="Aguardando cálculo...",
            font=("Poppins", 24, "bold"),
            text_color="#CBD5E1"
        )
        self.classification_label.pack(pady=(10, 10))

        # ---------------- MENSAGEM ---------------- #

        self.message_label = ctk.CTkLabel(
            self.result_frame,
            text="",
            wraplength=900,
            justify="center",
            font=("Poppins", 16),
            text_color="#E2E8F0"
        )

        self.message_label.pack(
            padx=30,
            pady=(0, 30),
            fill="x"
        )

        # ENTER para calcular
        self.bind("<Return>", lambda event: self.calculate_imc())

    # ======================================================
    # VALIDAÇÃO
    # ======================================================

    def validate_input(self, value):

        pattern = r'^\d*\.?\d*$'

        return re.match(pattern, value) is not None

    # ======================================================
    # ANIMAÇÃO / EFEITO VISUAL
    # ======================================================

    def animate_result(self, color):

        self.result_frame.configure(border_color=color)

        self.after(
            120,
            lambda: self.result_frame.configure(border_color="#334155")
        )

        self.after(
            240,
            lambda: self.result_frame.configure(border_color=color)
        )

    # ======================================================
    # CLASSIFICAÇÃO OMS
    # ======================================================

    def classify_imc(self, imc):

        if imc < 18.5:
            return {
                "classificacao": "Abaixo do peso",
                "mensagem": (
                    "Seu IMC está abaixo do ideal. "
                    "É recomendado procurar orientação nutricional "
                    "para manter uma boa saúde."
                ),
                "cor": "#F59E0B"
            }

        elif 18.5 <= imc <= 24.9:
            return {
                "classificacao": "Peso normal",
                "mensagem": (
                    "Parabéns! Seu peso está dentro da faixa saudável. "
                    "Continue mantendo hábitos equilibrados."
                ),
                "cor": "#22C55E"
            }

        elif 25 <= imc <= 29.9:
            return {
                "classificacao": "Sobrepeso",
                "mensagem": (
                    "Seu IMC indica sobrepeso. "
                    "Atividades físicas e alimentação balanceada "
                    "podem ajudar bastante."
                ),
                "cor": "#EAB308"
            }

        elif 30 <= imc <= 34.9:
            return {
                "classificacao": "Obesidade Grau I",
                "mensagem": (
                    "Atenção! É recomendado acompanhamento profissional "
                    "para melhorar sua saúde e qualidade de vida."
                ),
                "cor": "#F97316"
            }

        elif 35 <= imc <= 39.9:
            return {
                "classificacao": "Obesidade Grau II",
                "mensagem": (
                    "Alerta urgente! Procure apoio médico e nutricional "
                    "para acompanhamento adequado."
                ),
                "cor": "#EF4444"
            }

        else:
            return {
                "classificacao": "Obesidade Grau III (Mórbida)",
                "mensagem": (
                    "Alerta crítico! É muito importante buscar "
                    "acompanhamento profissional o quanto antes."
                ),
                "cor": "#DC2626"
            }

    # ======================================================
    # CÁLCULO IMC
    # ======================================================

    def calculate_imc(self):

        peso = self.weight_entry.get().strip().replace(",", ".")
        altura = self.height_entry.get().strip().replace(",", ".")

        # ---------------- CAMPOS VAZIOS ---------------- #

        if not peso or not altura:

            messagebox.showerror(
                "Erro",
                "Preencha todos os campos."
            )

            return

        # ---------------- VALIDAÇÃO ---------------- #

        if not self.validate_input(peso) or not self.validate_input(altura):

            messagebox.showerror(
                "Erro",
                "Digite apenas números válidos."
            )

            return

        try:

            peso = float(peso)
            altura = float(altura)

            # Se altura vier em centímetros
            if altura > 3:
                altura = altura / 100

            # ---------------- VALORES INVÁLIDOS ---------------- #

            if peso <= 0 or altura <= 0:

                messagebox.showerror(
                    "Erro",
                    "Peso e altura devem ser maiores que zero."
                )

                return

            # ---------------- CÁLCULO ---------------- #

            imc = peso / (altura ** 2)

            dados = self.classify_imc(imc)

            # ---------------- RESULTADO ---------------- #

            self.imc_value_label.configure(
                text=f"{imc:.1f}",
                text_color=dados["cor"]
            )

            self.classification_label.configure(
                text=dados["classificacao"],
                text_color=dados["cor"]
            )

            self.message_label.configure(
                text=dados["mensagem"]
            )

            # ---------------- FEEDBACK VISUAL ---------------- #

            self.weight_entry.configure(
                border_color=dados["cor"]
            )

            self.height_entry.configure(
                border_color=dados["cor"]
            )

            self.animate_result(dados["cor"])

        except Exception:

            messagebox.showerror(
                "Erro",
                "Não foi possível calcular o IMC."
            )

    # ======================================================
    # LIMPAR CAMPOS
    # ======================================================

    def clear_fields(self):

        self.weight_entry.delete(0, "end")
        self.height_entry.delete(0, "end")

        self.imc_value_label.configure(
            text="--",
            text_color="#38BDF8"
        )

        self.classification_label.configure(
            text="Aguardando cálculo...",
            text_color="#CBD5E1"
        )

        self.message_label.configure(text="")

        self.result_frame.configure(
            border_color="#334155"
        )

        self.weight_entry.configure(
            border_color="#565B5E"
        )

        self.height_entry.configure(
            border_color="#565B5E"
        )


# ==========================================================
# EXECUÇÃO
# ==========================================================

if __name__ == "__main__":

    app = IMCCalculator()
    app.mainloop()