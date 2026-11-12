import flet as ft

def main(page: ft.Page):
    page.title = "Contador"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    valor = 0
    texto_valor = ft.Text(str(valor), size=30, weight=ft.FontWeight.BOLD)

    def somar(e):
        nonlocal valor
        valor += 1
        texto_valor.value = str(valor)
        page.update()

    def subtrair(e):
        nonlocal valor
        valor -= 1
        texto_valor.value = str(valor)
        page.update()

    botoes = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.ElevatedButton(content=ft.Text("-"), on_click=subtrair),
            ft.ElevatedButton(content=ft.Text("+"), on_click=somar),
        ],
    )

    page.add(
        ft.Column(
            controls=[
                ft.Text("Contador", size=20),
                texto_valor,
                botoes,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
