import os
import random
import FreeSimpleGUI as sg


def carregar_palavras(arquivo="palavras.txt"):
    """Lê as palavras de um arquivo .txt e retorna uma lista em maiúsculas."""
    if not os.path.exists(arquivo):
        sg.popup(
            f"Arquivo '{arquivo}' não encontrado na pasta do projeto!",
            title="Erro",
        )
        return ["PYTHON", "ALGORITMO", "COMPUTADOR", "UNIVERSIDADE", "PROGRAMACAO"]

    with open(arquivo, "r", encoding="utf-8") as f:
        palavras = [
            linha.strip().upper()
            for linha in f
            if linha.strip().isalpha()
        ]

    if len(palavras) < 50:
        sg.popup(
            f"O arquivo contém apenas {len(palavras)} palavras (mínimo recomendado: 50).",
            title="Aviso",
        )
    return palavras if palavras else ["PYTHON"]


def escolher_palavra(lista):
    """Seleciona e retorna uma palavra aleatória da lista."""
    return random.choice(lista)
def atualizar_display(palavra, letras_tentadas):
    """Retorna a string formatada com letras descobertas e underscores."""
    return " ".join(
        letra if letra in letras_tentadas else "_" for letra in palavra
    )


def verificar_vitoria(palavra, letras_tentadas):
    """Verifica se todas as letras da palavra já foram descobertas."""
    return all(letra in letras_tentadas for letra in palavra)
def carregar_estatisticas(arquivo="estatisticas.txt"):
    """Lê vitórias e derrotas salvas anteriormente."""
    if not os.path.exists(arquivo):
        return 0, 0
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            v, d = f.read().strip().split(",")
            return int(v), int(d)
    except (ValueError, IndexError):
        return 0, 0


def salvar_estatisticas(vitorias, derrotas, arquivo="estatisticas.txt"):
    """Salva o placar acumulado de vitórias e derrotas em arquivo."""
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(f"{vitorias},{derrotas}")