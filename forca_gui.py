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
        
def desenhar_boneco(graph, erros):
    """Desenha a estrutura da forca e as 6 partes do boneco conforme os erros."""
    graph.erase()

    graph.draw_line((30, 20), (130, 20), color="#333333", width=4)
    graph.draw_line((80, 20), (80, 220), color="#333333", width=4)
    graph.draw_line((80, 220), (170, 220), color="#333333", width=4)
    graph.draw_line((170, 220), (170, 190), color="#8B4513", width=3)

    if erros >= 1:
        graph.draw_circle((170, 170), 20, line_color="#222222", line_width=3)
    if erros >= 2:
        graph.draw_line((170, 150), (170, 90), color="#222222", width=3)
    if erros >= 3:
        graph.draw_line((170, 135), (140, 110), color="#222222", width=3)
    if erros >= 4:
        graph.draw_line((170, 135), (200, 110), color="#222222", width=3)
    if erros >= 5:
        graph.draw_line((170, 90), (145, 50), color="#222222", width=3)
    if erros >= 6:
        graph.draw_line((170, 90), (195, 50), color="#222222", width=3)


def criar_teclado_virtual():
    """Monta as linhas de botões A-Z para o teclado virtual."""
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    linhas = []
    for i in range(0, len(alfabeto), 9):
        linha = [
            sg.Button(
                letra,
                key=f"-LETRA-{letra}-",
                size=(4, 2),
                font=("Helvetica", 11, "bold"),
                button_color=("#1E293B", "#FFFFFF"),
            )
            for letra in alfabeto[i : i + 9]
        ]
        linhas.append(linha)
    return linhas