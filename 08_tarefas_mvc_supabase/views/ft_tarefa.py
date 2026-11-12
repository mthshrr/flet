import flet as ft
from models.model_tarefa import Tarefa


# ==============================================================================
# VIEW: COMPONENTES VISUAIS COM HERANÇA (FLET)
# ==============================================================================

class TarefaCard(ft.Container):
    """
    Superclasse visual que herda de ft.Container.
    Define a estrutura base, o layout e os eventos de uma tarefa.
    """

    def __init__(self, tarefa: Tarefa, on_alternar_conclusao, on_remover):
        super().__init__()
        self.tarefa = tarefa
        self.on_alternar_conclusao = on_alternar_conclusao
        self.on_remover = on_remover

        # Atributos visuais padrão (podem ser especializados pelas subclasses)
        self.cor_fundo = "#E3F2FD"  # Azul claro
        self.icone = ft.Icons.TASK_ALT
        self.rotulo_tipo = "Comum"

    def construir_layout(self):
        """
        Monta os elementos visuais internos do container.
        """
        self.padding = 12
        self.border_radius = 8
        self.bgcolor = self.cor_fundo

        self.checkbox = ft.Checkbox(value=self.tarefa.concluida, on_change=self.ao_mudar_checkbox)

        # Se já veio do banco concluída, aplica o texto tachado
        if self.tarefa.concluida:
            estilo_texto = ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH)
        else:
            estilo_texto = ft.TextStyle(decoration=ft.TextDecoration.NONE)

        self.texto_nome = ft.Text(self.tarefa.nome, expand=True, size=16, style=estilo_texto)

        self.botao_excluir = ft.IconButton(
            icon=ft.Icons.DELETE,
            icon_color=ft.Colors.RED_400,
            on_click=self.ao_clicar_excluir,
        )

        self.content = ft.Row(
            controls=[
                ft.Icon(self.icone),
                self.checkbox,
                self.texto_nome,
                ft.Container(
                    content=ft.Text(self.rotulo_tipo, size=12, weight=ft.FontWeight.W_500),
                    padding=ft.Padding.symmetric(horizontal=8, vertical=4),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=4,
                ),
                ft.Text(f"+{self.tarefa.xp} XP", weight=ft.FontWeight.BOLD),
                self.botao_excluir,
            ]
        )

    def ao_mudar_checkbox(self, evento):
        """Disparado quando o usuário clica no checkbox."""
        novo_status = self.checkbox.value
        if novo_status:
            self.texto_nome.style = ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH)
        else:
            self.texto_nome.style = ft.TextStyle(decoration=ft.TextDecoration.NONE)
        self.update()

        # Notifica o Controller via callback
        self.on_alternar_conclusao(self.tarefa, novo_status)

    def ao_clicar_excluir(self, evento):
        """Disparado quando o usuário clica no botão de lixeira."""
        # Notifica o Controller via callback
        self.on_remover(self.tarefa, self)


# ==============================================================================
# SUBCLASSES (HERANÇA E POLIMORFISMO VISUAL)
# ==============================================================================

class TarefaComumCard(TarefaCard):
    def __init__(self, tarefa: Tarefa, on_alternar_conclusao, on_remover):
        super().__init__(tarefa, on_alternar_conclusao, on_remover)
        self.cor_fundo = "#E3F2FD"  # Azul suave
        self.icone = ft.Icons.TASK_ALT
        self.rotulo_tipo = "Comum"
        self.construir_layout()


class TarefaUrgenteCard(TarefaCard):
    def __init__(self, tarefa: Tarefa, on_alternar_conclusao, on_remover):
        super().__init__(tarefa, on_alternar_conclusao, on_remover)
        self.cor_fundo = "#FFCDD2"  # Vermelho suave
        self.icone = ft.Icons.WARNING_AMBER
        self.rotulo_tipo = "Urgente"
        self.construir_layout()


class TarefaEpicaCard(TarefaCard):
    def __init__(self, tarefa: Tarefa, on_alternar_conclusao, on_remover):
        super().__init__(tarefa, on_alternar_conclusao, on_remover)
        self.cor_fundo = "#FFE082"  # Dourado suave
        self.icone = ft.Icons.STAR
        self.rotulo_tipo = "Épica ⭐"
        self.construir_layout()


def criar_card_tarefa(tarefa: Tarefa, on_alternar_conclusao, on_remover) -> TarefaCard:
    """
    Função auxiliar que instancia a subclasse de card apropriada com base no tipo da tarefa.
    """
    if tarefa.tipo == "Urgente":
        return TarefaUrgenteCard(tarefa, on_alternar_conclusao, on_remover)
    elif tarefa.tipo == "Épica":
        return TarefaEpicaCard(tarefa, on_alternar_conclusao, on_remover)
    else:
        return TarefaComumCard(tarefa, on_alternar_conclusao, on_remover)
