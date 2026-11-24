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