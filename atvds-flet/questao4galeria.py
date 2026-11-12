import flet as ft

def main(page: ft.Page):
    page.title = "Galeria de Imagens com Troca de Tema"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    imagem_exibida = ft.Image(
        src="cachorro.jpg",
        width=300,
        height=300,
        fit="cover",
        border_radius=12,
    )

    def alternar_tema(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    def mostrar_cachorro(e):
        imagem_exibida.src = "cachorro.jpg"
        page.update()

    def mostrar_gato(e):
        imagem_exibida.src = "gato.jpg"
        page.update()

    botao_tema = ft.ElevatedButton(
        content=ft.Text("Alternar Tema"),
        icon=ft.Icons.WB_SUNNY_OUTLINED,
        on_click=alternar_tema,
    )

    botoes_animais = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15,
        controls=[
            ft.ElevatedButton(
                content=ft.Text("Cachorro"),
                icon=ft.Icons.PETS,
                on_click=mostrar_cachorro,
            ),
            ft.ElevatedButton(
                content=ft.Text("Gato"),
                icon=ft.Icons.PETS,
                on_click=mostrar_gato,
            ),
        ],
    )

    page.add(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                botao_tema,
                imagem_exibida,
                botoes_animais,
            ],
        )
    )

ft.app(target=main)