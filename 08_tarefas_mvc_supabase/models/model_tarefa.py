# ==============================================================================
# MODELO DE DADOS: Tarefa
# Representa a entidade de negócio de forma pura (sem dependência de banco ou Flet)
# ==============================================================================

class Tarefa:
    def __init__(self, nome: str, tipo: str = "Comum", xp: int = 10, concluida: bool = False, id_tarefa: int = None):
        self.id = id_tarefa
        self.nome = nome
        self.tipo = tipo
        self.xp = xp
        self.concluida = concluida

    def alternar_conclusao(self):
        """Inverte o estado de conclusão da tarefa."""
        if self.concluida:
            self.concluida = False
        else:
            self.concluida = True

    def para_dicionario(self):
        """
        Converte o objeto para um dicionário Python para ser enviado ao Supabase.
        """
        dados = {
            "nome": self.nome,
            "tipo": self.tipo,
            "xp": self.xp,
            "concluida": self.concluida,
        }
        if self.id is not None:
            dados["id"] = self.id
        return dados

    @staticmethod
    def de_dicionario(dados: dict):
        """
        Método de fábrica (Factory): cria um objeto Tarefa a partir de um dicionário retornado do banco.
        """
        return Tarefa(
            id_tarefa=dados.get("id"),
            nome=dados.get("nome", ""),
            tipo=dados.get("tipo", "Comum"),
            xp=dados.get("xp", 10),
            concluida=dados.get("concluida", False),
        )
