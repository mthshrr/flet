from flet import app, TextField, ElevatedButton, Column, Text

def main(page):
    # Criação das caixas de texto para entrada de números
    input1 = TextField(label="Número 1", keyboard_type="number")
    input2 = TextField(label="Número 2", keyboard_type="number")
    
    # Função para o botão
    def on_button_click(e):
        try:
            num1 = float(input1.value)
            num2 = float(input2.value)
            result = num1 + num2  # Exemplo de operação: soma
            page.add(Text(f"Resultado: {result}"))
        except ValueError:
            page.add(Text("Por favor, insira números válidos."))

    # Criação do botão
    button = ElevatedButton(text="Calcular", on_click=on_button_click)

    # Adicionando os componentes à página
    page.add(Column(controls=[input1, input2, button]))

app(target=main)