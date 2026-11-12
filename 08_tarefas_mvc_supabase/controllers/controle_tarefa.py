import flet as ft
from models.model_tarefa import Tarefa
from models.sql_tarefa import SQL_Tarefa
from views.ft_tarefa import criar_card_tarefa


class ControleTarefa:
    """
    CONTROLLER: Coordena a lógica de negócio entre o modelo de banco (SQL_Tarefa)
    e os componentes visuais do Flet na página.
    """

    def __init__(self, page: ft.Page, sql_tarefa: SQL_Tarefa, coluna_tarefas: ft.Column, texto_xp: ft.Text):
        self.page = page
        self.sql = sql_tarefa
        self.coluna_tarefas = coluna_tarefas
        self.texto_xp = texto_xp
        self.xp_total = 0

    def carregar_tarefas_iniciais(self):
        """
        Busca todas as tarefas gravadas no Supabase e preenche a coluna na tela.
        Calcula o XP total acumulado com base nas tarefas já concluídas.
        """
        try:
            lista_tarefas = self.sql.listar_todas()
            self.coluna_tarefas.controls.clear()
            self.xp_total = 0

            for tarefa in lista_tarefas:
                if tarefa.concluida:
                    self.xp_total += tarefa.xp

                card = criar_card_tarefa(
                    tarefa=tarefa,
                    on_alternar_conclusao=self.alternar_conclusao_tarefa,
                    on_remover=self.remover_tarefa,
                )
                self.coluna_tarefas.controls.append(card)

            self.atualizar_placar_xp()
            self.page.update()
        except Exception as erro:
            self.mostrar_mensagem_erro(f"Erro ao carregar tarefas do Supabase: {erro}")

    def adicionar_nova_tarefa(self, nome: str, tipo: str):
        """
        Valida os dados, define o XP, grava no Supabase e adiciona o componente na tela.
        """
        nome = nome.strip()
        if not nome:
            self.mostrar_mensagem_erro("O nome da tarefa não pode ficar vazio!")
            return False

        # Define pontuação de XP por tipo
        if tipo == "Urgente":
            xp = 20
        elif tipo == "Épica":
            xp = 50
        else:
            tipo = "Comum"
            xp = 10

        try:
            # 1. Cria a entidade Tarefa
            nova_tarefa = Tarefa(nome=nome, tipo=tipo, xp=xp, concluida=False)

            # 2. Persiste no banco de dados Supabase via SQL_Tarefa
            self.sql.inserir(nova_tarefa)

            # 3. Cria o componente visual correspondente via View com Herança
            card = criar_card_tarefa(
                tarefa=nova_tarefa,
                on_alternar_conclusao=self.alternar_conclusao_tarefa,
                on_remover=self.remover_tarefa,
            )

            # 4. Adiciona na lista visual e atualiza a tela
            self.coluna_tarefas.controls.append(card)
            self.page.update()
            self.mostrar_mensagem_sucesso(f"Tarefa '{nome}' gravada com sucesso no Supabase!")
            return True
        except Exception as erro:
            self.mostrar_mensagem_erro(f"Falha ao salvar no banco: {erro}")
            return False

    def alternar_conclusao_tarefa(self, tarefa: Tarefa, novo_status: bool):
        """
        Atualiza o status da tarefa no banco e recalcula o XP total na tela.
        """
        try:
            # Atualiza no Supabase
            self.sql.atualizar_status(tarefa.id, novo_status)
            tarefa.concluida = novo_status

            # Atualiza o XP
            if novo_status:
                self.xp_total += tarefa.xp
            else:
                self.xp_total -= tarefa.xp

            self.atualizar_placar_xp()
            self.page.update()
        except Exception as erro:
            self.mostrar_mensagem_erro(f"Erro ao atualizar status no banco: {erro}")

    def remover_tarefa(self, tarefa: Tarefa, card_container):
        """
        Exclui a tarefa do banco de dados e a retira da tela.
        """
        try:
            # Remove do Supabase
            self.sql.excluir(tarefa.id)

            # Se estava concluída, subtrai o XP
            if tarefa.concluida:
                self.xp_total -= tarefa.xp
                self.atualizar_placar_xp()

            # Remove o controle visual da coluna
            self.coluna_tarefas.controls.remove(card_container)
            self.page.update()
            self.mostrar_mensagem_sucesso("Tarefa removida com sucesso!")
        except Exception as erro:
            self.mostrar_mensagem_erro(f"Erro ao excluir tarefa do banco: {erro}")

    def atualizar_placar_xp(self):
        self.texto_xp.value = f"XP Total: {self.xp_total}"

    def mostrar_mensagem_erro(self, texto: str):
        snackbar = ft.SnackBar(
            content=ft.Text(texto, color=ft.Colors.WHITE),
            bgcolor=ft.Colors.RED_600,
        )
        self.page.overlay.append(snackbar)
        snackbar.open = True
        self.page.update()

    def mostrar_mensagem_sucesso(self, texto: str):
        snackbar = ft.SnackBar(
            content=ft.Text(texto, color=ft.Colors.WHITE),
            bgcolor=ft.Colors.GREEN_700,
        )
        self.page.overlay.append(snackbar)
        snackbar.open = True
        self.page.update()
