import flet as ft

def main(page: ft.Page):
    page.title = "Layout de Card"

    imagem = ft.Image(
        src="fone.jpg",
        width=100,
        height=100,
        border_radius=8,
    )

    textos = ft.Column(
        controls=[
            ft.Text("Fone de Ouvido Bluetooth", size=18, weight=ft.FontWeight.BOLD),
            ft.Text("Cancelamento de ruído\nBateria de 40h"),
            ft.Text("R$ 299,90", size=16, color=ft.Colors.GREEN),
        ]
    )

    linha_card = ft.Row(
        controls=[imagem, textos]
    )

    card = ft.Container(
        content=linha_card,
        bgcolor=ft.Colors.WHITE,
        border=ft.Border(
            top=ft.BorderSide(1, ft.Colors.GREY_400),
            bottom=ft.BorderSide(1, ft.Colors.GREY_400),
            left=ft.BorderSide(1, ft.Colors.GREY_400),
            right=ft.BorderSide(1, ft.Colors.GREY_400),
        ),
        border_radius=10,
        padding=15,
    )

    page.add(card)

ft.app(target=main, assets_dir="assets")