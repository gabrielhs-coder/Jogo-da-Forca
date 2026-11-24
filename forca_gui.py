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
def main():
    sg.theme("LightGrey1")

    palavras = carregar_palavras("palavras.txt")
    vitorias, derrotas = carregar_estatisticas()

    estado = {
        "palavra": "",
        "letras_tentadas": set(),
        "erros": 0,
        "max_erros": 6,
        "dicas_usadas": 0,
        "max_dicas": 2,
        "jogo_ativo": True,
        "vitorias": vitorias,
        "derrotas": derrotas,
    }

    graph = sg.Graph(
        canvas_size=(240, 250),
        graph_bottom_left=(0, 0),
        graph_top_right=(240, 250),
        background_color="#FFFFFF",
        key="-FORCA-",
    )

    coluna_direita = [
        [
            sg.Text(
                "Tentativas restantes: 6",
                key="-TENTATIVAS-",
                font=("Helvetica", 13, "bold"),
                text_color="#0F172A",
            )
        ],
        [sg.VPush()],
        [
            sg.Text(
                "",
                key="-PALAVRA-",
                font=("Courier", 22, "bold"),
                text_color="#1D4ED8",
                justification="center",
                expand_x=True,
            )
        ],
        [sg.VPush()],
        [
            sg.Text(
                "Escolha uma letra para começar!",
                key="-MENSAGEM-",
                font=("Helvetica", 11, "italic"),
                text_color="#475569",
                justification="center",
                expand_x=True,
            )
        ],
    ]

    layout = [
        [
            sg.Text("JOGO DA FORCA", font=("Helvetica", 20, "bold"), text_color="#1E293B"),
            sg.Push(),
            sg.Text(
                f"Vitórias: {estado['vitorias']}  |  Derrotas: {estado['derrotas']}",
                key="-STATS-",
                font=("Helvetica", 12, "bold"),
                background_color="#E2E8F0",
                text_color="#334155",
                pad=(10, 5),
            ),
        ],
        [sg.HorizontalSeparator(pad=(0, 10))],
        [graph, sg.Column(coluna_direita, expand_x=True, expand_y=True)],
        [sg.HorizontalSeparator(pad=(0, 10))],
        *criar_teclado_virtual(),
        [sg.VPush()],
        [
            sg.Push(),
            sg.Button(
                "Novo Jogo",
                key="-NOVO-",
                font=("Helvetica", 11, "bold"),
                button_color=("#FFFFFF", "#2563EB"),
                pad=(10, 10),
            ),
            sg.Button(
                "Dica (2)",
                key="-DICA-",
                font=("Helvetica", 11, "bold"),
                button_color=("#FFFFFF", "#F59E0B"),
                pad=(10, 10),
            ),
            sg.Button(
                "Desistir",
                key="-DESISTIR-",
                font=("Helvetica", 11, "bold"),
                button_color=("#FFFFFF", "#DC2626"),
                pad=(10, 10),
            ),
            sg.Push(),
        ],
    ]

    window = sg.Window(
        "Jogo da Forca - INE5201",
        layout,
        size=(700, 600),
        finalize=True,
        return_keyboard_events=True,
    )

    def atualizar_interface():
        window["-PALAVRA-"].update(
            atualizar_display(estado["palavra"], estado["letras_tentadas"])
        )
        restantes = estado["max_erros"] - estado["erros"]
        cor_tentativas = "#DC2626" if restantes <= 2 else "#0F172A"
        window["-TENTATIVAS-"].update(
            f"Tentativas restantes: {restantes}", text_color=cor_tentativas
        )
        window["-STATS-"].update(
            f"Vitórias: {estado['vitorias']}  |  Derrotas: {estado['derrotas']}"
        )
        desenhar_boneco(graph, estado["erros"])

    def encerrar_partida(venceu, motivo=""):
        estado["jogo_ativo"] = False
        for letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            window[f"-LETRA-{letra}-"].update(disabled=True)
        window["-DICA-"].update(disabled=True)
        window["-DESISTIR-"].update(disabled=True)

        if venceu:
            estado["vitorias"] += 1
            window["-MENSAGEM-"].update("Parabéns! Você venceu!", text_color="#16A34A")
            sg.popup(
                f"Você acertou a palavra: {estado['palavra']}",
                title="Vitória!",
            )
        else:
            estado["derrotas"] += 1
            window["-PALAVRA-"].update(" ".join(estado["palavra"]))
            window["-MENSAGEM-"].update(
                f"Fim de jogo! A palavra era {estado['palavra']}.",
                text_color="#DC2626",
            )
            sg.popup(
                f"{motivo}\nA palavra secreta era: {estado['palavra']}",
                title="Derrota",
            )

        salvar_estatisticas(estado["vitorias"], estado["derrotas"])
        atualizar_interface()

    def tentar_letra(letra):
        if not estado["jogo_ativo"]:
            return

        if letra in estado["letras_tentadas"]:
            window["-MENSAGEM-"].update(
                f"A letra '{letra}' já foi tentada!", text_color="#D97706"
            )
            return

        estado["letras_tentadas"].add(letra)
        chave_btn = f"-LETRA-{letra}-"

        if letra in estado["palavra"]:
            window[chave_btn].update(
                disabled=True, button_color=("#14532D", "#86EFAC")
            )
            window["-MENSAGEM-"].update(
                f"Boa! A letra '{letra}' existe na palavra.", text_color="#16A34A"
            )
            atualizar_interface()
            if verificar_vitoria(estado["palavra"], estado["letras_tentadas"]):
                encerrar_partida(True)
        else:
            estado["erros"] += 1
            window[chave_btn].update(
                disabled=True, button_color=("#7F1D1D", "#FCA5A5")
            )
            window["-MENSAGEM-"].update(
                f"Ops! A letra '{letra}' não está na palavra.", text_color="#DC2626"
            )
            atualizar_interface()
            if estado["erros"] >= estado["max_erros"]:
                encerrar_partida(False, "Você atingiu o limite de 6 erros!")

    def pedir_dica():
        if not estado["jogo_ativo"]:
            return
        if estado["dicas_usadas"] >= estado["max_dicas"]:
            sg.popup("Você já usou todas as dicas desta partida!", title="Dicas")
            return

        nao_descobertas = [
            l for l in set(estado["palavra"]) if l not in estado["letras_tentadas"]
        ]
        if not nao_descobertas:
            return

        letra_dica = random.choice(nao_descobertas)
        estado["dicas_usadas"] += 1
        restantes = estado["max_dicas"] - estado["dicas_usadas"]
        window["-DICA-"].update(f"Dica ({restantes})")
        tentar_letra(letra_dica)

    def desistir():
        if not estado["jogo_ativo"]:
            return
        resposta = sg.popup_yes_no(
            "Tem certeza que deseja desistir desta partida?",
            title="Desistir",
        )
        if resposta == "Yes":
            estado["erros"] = estado["max_erros"]
            encerrar_partida(False, "Você desistiu da partida.")

    def novo_jogo():
        estado["palavra"] = escolher_palavra(palavras)
        estado["letras_tentadas"] = set()
        estado["erros"] = 0
        estado["dicas_usadas"] = 0
        estado["jogo_ativo"] = True

        for letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            window[f"-LETRA-{letra}-"].update(
                disabled=False, button_color=("#1E293B", "#FFFFFF")
            )

        window["-DICA-"].update(disabled=False, text=f"Dica ({estado['max_dicas']})")
        window["-DESISTIR-"].update(disabled=False)
        window["-MENSAGEM-"].update(
            "Escolha uma letra para começar!", text_color="#475569"
        )
        atualizar_interface()

    novo_jogo()

    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == "-NOVO-":
            novo_jogo()
        elif event == "-DICA-":
            pedir_dica()
        elif event == "-DESISTIR-":
            desistir()
        elif isinstance(event, str) and event.startswith("-LETRA-") and event.endswith("-"):
            letra = event.replace("-LETRA-", "").replace("-", "")
            tentar_letra(letra)
        elif isinstance(event, str) and len(event) == 1 and event.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            tentar_letra(event.upper())

    window.close()


if __name__ == "__main__":
    main()