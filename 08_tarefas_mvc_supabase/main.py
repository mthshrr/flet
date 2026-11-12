import flet as ft
from database.connect_supabase import connect_supabase, verificar_tabela_tarefas
from models.sql_tarefa import SQL_Tarefa
from controllers.controle_tarefa import ControleTarefa


def exibir_tela_erro_configuracao(page: ft.Page, mensagem_erro: str):
    """
    Exibe uma tela didática e elegante orientando o aluno caso falte o .env
    ou ocorra erro de conexão/tabela inexistente no Supabase.
    """
    def ao_clicar_tentar_novamente(evento):
        main(page)

    page.clean()
    page.add(
        ft.Container(
            padding=30,
            content=ft.Column(
                controls=[
                    ft.Icon(ft.Icons.CLOUD_OFF, size=64, color=ft.Colors.RED_500),
                    ft.Text("Atenção: Conexão com o Supabase Não Estabelecida", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_700),
                    ft.Text(
                        "O aplicativo precisa se conectar ao Supabase para carregar e salvar as tarefas.",
                        size=16,
                    ),
                    ft.Divider(),
                    ft.Text("Siga o checklist de verificação abaixo:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("1. Verifique se você criou o arquivo .env a partir do .env.example;"),
                    ft.Text("2. Preencha SUPABASE_URL e SUPABASE_KEY com as chaves do seu projeto;"),
                    ft.Text("3. Abra o painel do Supabase, vá em 'SQL Editor' e execute o script 'database/schema.sql';"),
                    ft.Text("4. Verifique se o seu computador está conectado à internet."),
                    ft.Divider(),
                    ft.Text("Detalhes técnicos da exceção capturada:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_700),
                    ft.Container(
                        content=ft.Text(str(mensagem_erro), color=ft.Colors.RED_900, font_family="monospace", size=13),
                        padding=12,
                        bgcolor=ft.Colors.RED_50,
                        border_radius=6,
                    ),
                    ft.Button(
                        content="Tentar Novamente",
                        icon=ft.Icons.REFRESH,
                        on_click=ao_clicar_tentar_novamente,
                    ),
                ],
                spacing=12,
            ),
        )
    )
    page.update()


def main(page: ft.Page):
    page.title = "Gerenciador de Tarefas Gamificado (MVC + Supabase)"
    page.theme_mode = ft.ThemeMode.LIGHT

    # ==========================================================================
    # 1. CONEXÃO COM O BANCO DE DADOS (DATABASE)
    # ==========================================================================
    try:
        cliente_supabase = connect_supabase()
        verificar_tabela_tarefas(cliente_supabase)
    except Exception as erro_conexao:
        exibir_tela_erro_configuracao(page, str(erro_conexao))
        return

    # Inicializa o Model de acesso ao banco
    sql_tarefas = SQL_Tarefa(cliente_supabase)

    # ==========================================================================
    # 2. CONSTRUÇÃO DA INTERFACE (VIEW PRINCIPAL)
    # ==========================================================================
    page.clean()

    texto_xp = ft.Text("XP Total: 0", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.AMBER_900)
    coluna_tarefas = ft.Column(spacing=8)

    input_nome = ft.TextField(label="Nova Tarefa", expand=True)
    dropdown_tipo = ft.Dropdown(
        label="Dificuldade / Tipo",
        options=[
            ft.DropdownOption(key="Comum", text="Comum (+10 XP)"),
            ft.DropdownOption(key="Urgente", text="Urgente (+20 XP)"),
            ft.DropdownOption(key="Épica", text="Épica (+50 XP)"),
        ],
        value="Comum",
        width=200,
    )

    # ==========================================================================
    # 3. INICIALIZAÇÃO DO CONTROLLER
    # ==========================================================================
    controller = ControleTarefa(
        page=page,
        sql_tarefa=sql_tarefas,
        coluna_tarefas=coluna_tarefas,
        texto_xp=texto_xp,
    )

    def ao_clicar_adicionar(evento):
        nome_digitado = input_nome.value
        tipo_selecionado = dropdown_tipo.value
        sucesso = controller.adicionar_nova_tarefa(nome_digitado, tipo_selecionado)
        if sucesso:
            input_nome.value = ""
            page.update()

    botao_adicionar = ft.Button(content="Adicionar Tarefa", on_click=ao_clicar_adicionar)

    linha_formulario = ft.Row(
        controls=[
            input_nome,
            dropdown_tipo,
            botao_adicionar,
        ]
    )

    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.CLOUD_DONE, color=ft.Colors.GREEN_600, size=28),
                        ft.Text("Tarefas com MVC + Supabase", size=26, weight=ft.FontWeight.BOLD),
                    ]
                ),
                ft.Text("Dados persistidos diretamente na nuvem (PostgreSQL) com arquitetura MVC."),
                texto_xp,
                linha_formulario,
                ft.Divider(),
                coluna_tarefas,
            ],
            spacing=15,
        )
    )

    # Carrega as tarefas já existentes no banco de dados ao iniciar
    controller.carregar_tarefas_iniciais()


if __name__ == "__main__":
    ft.run(main)
