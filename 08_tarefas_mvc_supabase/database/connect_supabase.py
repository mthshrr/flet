import os
from dotenv import load_dotenv
from supabase import create_client, Client


def connect_supabase() -> Client:
    """
    Carrega as variáveis do arquivo .env e inicializa a conexão com o Supabase.
    Trata automaticamente a URL caso o aluno copie com '/rest/v1/' do painel.
    Lança ValueError caso as variáveis de ambiente não estejam preenchidas.
    """
    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key or "seu-projeto" in url or "sua-chave" in key:
        raise ValueError(
            "Configuração do Supabase ausente ou inválida no arquivo .env.\n"
            "Preencha SUPABASE_URL e SUPABASE_KEY corretamente."
        )

    # 🛡️ TRATAMENTO AUTOMÁTICO PARA ALUNOS:
    # Se o aluno copiou a URL com '/rest/v1/' ou barra no final, nós limpamos:
    url = url.strip()
    if url.endswith("/rest/v1/"):
        url = url[:-9]
    elif url.endswith("/rest/v1"):
        url = url[:-8]
    elif url.endswith("/"):
        url = url[:-1]

    key = key.strip()

    return create_client(url, key)


def verificar_tabela_tarefas(cliente: Client) -> bool:
    """
    Testa se a tabela 'tarefas' já existe e se o cliente possui acesso a ela.
    Retorna True se conseguir consultar a tabela, ou lança uma Exception com detalhes.
    """
    try:
        # Faz uma consulta simples limitando a 1 registro para testar
        resposta = cliente.table("tarefas").select("id").limit(1).execute()
        return True
    except Exception as erro:
        # Propaga a exceção para que a interface capture e mostre ao aluno
        raise RuntimeError(
            "Não foi possível acessar a tabela 'tarefas' no Supabase.\n"
            "Verifique se você executou o script 'database/schema.sql' no SQL Editor do Supabase.\n"
            f"Detalhe do erro: {erro}"
        )
