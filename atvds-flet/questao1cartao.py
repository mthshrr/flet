import flet as ft

def main(page: ft.Page):
    page.title = "Cartão de Apresentação"

    foto = ft.Image(
        src="professor.jpg",
        width=150,
        height=150,
        border_radius=75,
        fit=ft.BoxFit.COVER,
    )

    nome = ft.Text("Pythonico Framewokerson", size=22, weight=ft.FontWeight.BOLD)
    profissao = ft.Text("Professor de Programação & Python", size=14)
    botao = ft.ElevatedButton("Entrar em Contato")

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[foto, nome, profissao, botao],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.Alignment.CENTER,
            expand=True,
        )

    )

ft.app(target=main, assets_dir="assets")