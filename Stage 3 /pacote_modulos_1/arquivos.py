def ler_arquivo(caminho_arquivo):
    """Lê o conteúdo de um arquivo de texto e retorna como string."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        return conteudo
    except FileNotFoundError:
        return "Erro: Arquivo não encontrado."
    except Exception as e:
        return f"Ocorreu um erro ao ler o arquivo: {e}"

def escrever_arquivo(caminho_arquivo, conteudo, modo='w'):
    """Escreve um conteúdo em um arquivo. 'w' para sobrescrever, 'a' para adicionar."""
    try:
        with open(caminho_arquivo, modo, encoding='utf-8') as f:
            f.write(conteudo)
        return "Conteúdo escrito com sucesso!"
    except Exception as e:
        return f"Ocorreu um erro ao escrever no arquivo: {e}"
