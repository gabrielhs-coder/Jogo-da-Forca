# Jogo da Forca com Interface Gráfica.

Implementação do clássico **Jogo da Forca** em Python utilizando **FreeSimpleGUI**,


---

## Funcionalidades

* **Leitura de arquivo externo (`palavras.txt`):** carrega palavras automaticamente (com suporte a 50+ palavras), converte para maiúsculas e valida o conteúdo.
* **Seleção aleatória:** sorteia uma nova palavra a cada partida.
* **Interface gráfica com FreeSimpleGUI:**
  * Exibição da palavra oculta com traços (`_ _ _ _`) e revelação progressiva das letras corretas.
  * Desenho dinâmico da forca e das **6 partes do boneco** (cabeça, tronco, braço esquerdo, braço direito, perna esquerda e perna direita).
  * Teclado virtual **A–Z** clicável com feedback visual de cores (verde para acerto, vermelho para erro) e suporte ao teclado físico.
  * Contador de tentativas restantes (máximo de 6 erros).
  * Botões de ação: **Novo Jogo**, **Dica** (até 2 dicas por partida) e **Desistir**.
  * Mensagens claras de vitória, derrota, desistência e letras já tentadas.
* **Estatísticas persistentes:** salva e carrega o total de vitórias e derrotas em `estatisticas.txt`.

## Uso de Copilot

Durante o desenvolvimento deste projeto, ferramentas de assistência por IA (como GitHub Copilot) foram utilizadas como apoio para:

* Estruturar a organização modular das funções sugeridas no enunciado (`carregar_palavras`, `escolher_palavra`, `atualizar_display`, `desenhar_boneco`, `verificar_vitoria`, `salvar_estatisticas` e `main`).
* Montar o layout da interface gráfica com `FreeSimpleGUI`, incluindo teclado virtual A–Z, desenho no `Graph`, sistema de dicas, botão de desistir e persistência de estatísticas.
* Diagnosticar e corrigir problemas de execução e compatibilidade no ambiente local, além de revisar a clareza da documentação.

Todo o código foi testado, revisado e adaptado manualmente para atender aos requisitos da Tarefa 03

## Estrutura do Repositório

Jogo-da-Forca/
├── forca_gui.py        # Código principal do jogo e da interface gráfica
├── palavras.txt        # Lista de palavras (50+ palavras, uma por linha)
├── estatisticas.txt    # Gerado automaticamente para armazenar vitórias e derrotas
└── README.md           # Documentação do projeto