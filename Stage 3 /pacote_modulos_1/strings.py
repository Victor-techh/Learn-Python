def reverter_string(texto):
    """Retorna a string invertida."""
    return texto[::-1]

def contar_vogais(texto):
    """Conta o número de vogais em uma string (ignorando maiúsculas/minúsculas)."""
    vogais = "aeiouAEIOU"
    return sum(1 for char in texto if char in vogais)

def capitalizar_primeira_letra(texto):
    """Retorna a string com a primeira letra de cada palavra em maiúscula."""
    return ' '.join(word.capitalize() for word in texto.split())
