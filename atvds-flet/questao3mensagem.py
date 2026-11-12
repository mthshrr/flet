import flet as ft

def main(page: ft.Page):
    page.title = "Mensagem de Boas-Vindas Dinâmica"
    page.padding = 20

    campo_nome = ft.TextField(
        label="Digite seu nome",
        hint_text="Ex: Ana Silva",
    )

    mensagem = ft.Text(size=16)

    def enviar_saudacao(e):
        nome = campo_nome.value.strip()
        if nome:
            mensagem.value = f"Olá, {nome}! Seja bem-vindo ao Flet!"
        else:
            mensagem.value = "Por favor, digite um nome válido."
        page.update()

    botao_enviar = ft.ElevatedButton(
        content=ft.Text("Enviar Saudação"),
        on_click=enviar_saudacao,
    )

    imagem = ft.Image(
        src="assets/sua_imagem.png",
        width=200,
        height=200,
        fit="contain",
    )

    page.add(
        ft.Column(
            controls=[
                imagem,
                campo_nome,
                botao_enviar,
                ft.Divider(),
                mensagem,
            ],
            spacing=15,
        )
    )

ft.app(target=main)