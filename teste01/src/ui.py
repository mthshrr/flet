from flet import Page, TextField, ElevatedButton, Column

def create_ui(page: Page):
    # Criação das caixas de texto para entrada de números
    input1 = TextField(label="Número 1", keyboard_type="number")
    input2 = TextField(label="Número 2", keyboard_type="number")

    # Função que será chamada ao clicar no botão
    def on_button_click(e):
        try:
            num1 = float(input1.value)
            num2 = float(input2.value)
            # Aqui você pode adicionar a lógica que deseja executar com os números
            page.add(TextField(value=f"Soma: {num1 + num2}", read_only=True))
        except ValueError:
            page.add(TextField(value="Por favor, insira números válidos.", read_only=True))

    # Criação do botão
    button = ElevatedButton(text="Calcular", on_click=on_button_click)

    # Adicionando os componentes à página
    page.add(Column(controls=[input1, input2, button]))