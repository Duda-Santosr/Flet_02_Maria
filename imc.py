import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = "#f3f0f9"  # fundo claro lilás

    # Cores padrão
    texto_cor = "#6a1b9a"  # roxo escuro no modo claro
    texto_claro = "#e0e0e0"  # cinza claro no modo escuro

    # Função para atualizar cores
    def atualizar_cores():
        titulo.color = texto_claro if page.theme_mode == ft.ThemeMode.DARK else texto_cor
        subtitulo.color = texto_claro if page.theme_mode == ft.ThemeMode.DARK else texto_cor
        resultado.color = texto_claro if page.theme_mode == ft.ThemeMode.DARK else texto_cor
        page.update()

    # Alternância de tema
    def toggle_tema(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            page.bgcolor = "#1f1b2e"  # fundo escuro
            tema_btn.icon = ft.Icons.LIGHT_MODE
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.bgcolor = "#f3f0f9"
            tema_btn.icon = ft.Icons.DARK_MODE
        atualizar_cores()

    # Campos de entrada
    peso = ft.TextField(
        label="Peso (kg)",
        width=300,
        prefix_icon=ft.Icons.FITNESS_CENTER,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_color="#6a1b9a",
    )
    altura = ft.TextField(
        label="Altura (m)",
        width=300,
        prefix_icon=ft.Icons.HEIGHT,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_color="#6a1b9a",
    )

    # Texto do resultado
    resultado = ft.Text(
        size=20,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        color=texto_cor,
    )

    # Função para calcular IMC
    def calcular_imc(e):
        try:
            p = float(peso.value.replace(",", "."))
            a = float(altura.value.replace(",", "."))
            if p <= 0 or a <= 0:
                resultado.value = "⚠️ Informe valores válidos!"
            else:
                imc = p / (a * a)
                if imc < 18.5:
                    classificacao = "Abaixo do peso"
                elif imc < 24.9:
                    classificacao = "Peso normal"
                elif imc < 29.9:
                    classificacao = "Sobrepeso"
                elif imc < 34.9:
                    classificacao = "Obesidade grau I"
                elif imc < 39.9:
                    classificacao = "Obesidade grau II"
                else:
                    classificacao = "Obesidade grau III"

                resultado.value = f"📊 Seu IMC é {imc:.2f} → {classificacao}"
        except:
            resultado.value = "⚠️ Preencha peso e altura corretamente!"
        page.update()

    # Função para limpar os campos
    def limpar(e):
        peso.value = ""
        altura.value = ""
        resultado.value = ""
        page.update()

    # Botão de alternância de tema
    tema_btn = ft.IconButton(
        ft.Icons.DARK_MODE,
        on_click=toggle_tema,
        icon_color="#c579f4",
    )

    # Botões principais
    btn_calcular = ft.ElevatedButton(
        "Calcular IMC",
        bgcolor="#6a1b9a",
        color=ft.Colors.WHITE,
        width=150,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)),
        on_click=calcular_imc,
    )

    btn_limpar = ft.ElevatedButton(
        "Limpar",
        bgcolor="#d32f63",
        color=ft.Colors.WHITE,
        width=150,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)),
        on_click=limpar,
    )

    # Elementos de texto para fácil atualização de cor
    titulo = ft.Text(
        "Calculadora de IMC",
        size=24,
        weight=ft.FontWeight.BOLD,
        color=texto_cor,
        text_align=ft.TextAlign.CENTER,
    )
    subtitulo = ft.Text(
        "Informe seus dados",
        size=16,
        color=texto_cor,
        text_align=ft.TextAlign.CENTER,
    )

    # Layout da interface
    page.add(
        ft.Column(
            [
                ft.Row(
                    [titulo, tema_btn],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                subtitulo,
                peso,
                altura,
                ft.Row(
                    [btn_calcular, btn_limpar],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                ),
                resultado,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
    )

ft.app(main)
