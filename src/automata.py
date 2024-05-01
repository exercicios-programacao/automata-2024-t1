# import json
# import os

# os.system("cls")
# meu formatter "ms-python.black-formatter" deixa feinho assim mas da pra ler melhor
# comentarios:
# eu não gosto de snake_case, adiciona muitos underlines e deixa o código espaçado demais
# vou colocar pra ficar verdinho no github
#
# coloquei as docstrings de volta, tinha tirado quando estava testando

"""
Arquivo com as funções de processamento do autômato.

load_automata: carrega um autômato a partir de um arquivo de texto.

process: processa um autômato com uma lista de palavras.
"""


def load_automata(filename):
    """
    Carrega um autômato a partir de um arquivo de texto.

    Args:
        filename (str): nome do arquivo de texto.
        Returns:
        tuple: uma tupla com os elementos do autômato.

    Raises:
        Exception: se houver erro na entrada.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            linhas = []
            for linha_do_arquivo in f.readlines():
                linhas.append(linha_do_arquivo.strip())
        # tratando o arquivo
        alfabeto = linhas[0].split(" ")
        conjunto_de_estados = linhas[1].split(" ")
        estados_finais = linhas[2].split(" ")
        estado_inicial = linhas[3]
        # dict para guardar as transições
        dicionario_de_transicoes = {}
        for estado in conjunto_de_estados:
            dicionario_de_transicoes[estado] = {}
            for letra in alfabeto:
                dicionario_de_transicoes[estado][letra] = ""
        for regras in linhas[4:]:
            regra = regras.split(" ")
            estado_inicial_transicao = regra[0]
            letra = regra[1]
            estado_final_transicao = regra[2]
            # exceptions
            if letra not in alfabeto:
                raise IOError(
                    f"ALFABETO a letra: {
                        letra} não pertence ao alfabeto: {alfabeto}"
                )
            if estado_inicial_transicao not in conjunto_de_estados:
                raise IOError(
                    f"{estado_inicial_transicao} não pertence ao{conjunto_de_estados}"
                )
            if estado_final_transicao not in conjunto_de_estados:
                raise IOError(
                    f"{estado_final_transicao} não pertence ao{conjunto_de_estados}"
                )
            if dicionario_de_transicoes[estado_inicial_transicao][letra] != "":
                raise Warning(
                    f"TRANSIÇÃO NÃO DETERMINÍSTICA: {
                        estado_inicial_transicao} - {letra} - {estado_final_transicao}"
                )
            # exceptions
            dicionario_de_transicoes[estado_inicial_transicao][
                letra
            ] = estado_final_transicao
        # exceptions o retorno
        if estado_inicial not in conjunto_de_estados:
            raise IOError(
                f"ESTADO INICIAL {estado_inicial} não pertence ao{
                    conjunto_de_estados}"
            )
        for estado, transicoes in dicionario_de_transicoes.items():
            for letra, estado_final in transicoes.items():
                if estado_final == "":
                    raise IOError(
                        f"TRANSIÇÃO INCOMPLETA: {
                            estado} - {letra} - {estado_final}"
                    )
        for estado in estados_finais:
            if estado not in conjunto_de_estados:
                raise IOError(
                    f"ESTADO FINAL {estado} não pertence ao{
                        conjunto_de_estados}"
                )
        # exceptions o retorno
        return (
            conjunto_de_estados,
            alfabeto,
            dicionario_de_transicoes,
            estado_inicial,
            estados_finais,
        )
    # erro se erro
    except Exception as exception:
        raise IOError("ERRO DE ENTRADA" + str(exception)) from exception
    # erro se erro


def process(automata, words):
    """
    Processa um autômato com uma lista de palavras.

    Args:
        automata (tuple): uma tupla com os elementos do autômato.
        words (list): uma lista de palavras.

    Returns:
        dict: um dicionário com as palavras e seus respectivos resultados.
    """
    (
        conjunto_de_estados,
        alfabeto,
        dicionario_de_transicoes,
        estado_inicial,
        estados_finais,
    ) = automata
    return_dict = {}
    print(conjunto_de_estados)

    for palavra in words:
        estado_atual = estado_inicial
        invalida = False

        # para cada letra da palavra
        for char in palavra:

            if char not in alfabeto:  # se o char não pertence ao alfabeto é invalida
                return_dict[palavra] = "INVALIDA"
                invalida = True
                break

            try:
                estado_atual = dicionario_de_transicoes[estado_atual][char]
            except (
                KeyError
            ):  # se não tiver transição para o estado no dicionário é rejeitada pelo automato
                return_dict[palavra] = "REJEITA"
                invalida = True
                break

        if estado_atual in estados_finais and not invalida:
            return_dict[palavra] = "ACEITA"
        elif estado_atual not in estados_finais and not invalida:
            return_dict[palavra] = "REJEITA"
        else:
            # nada deveria chegar aqui mas se chegar deve ser invalida
            return_dict[palavra] = "INVALIDA"

    return return_dict


# words = [
#     "ab",  # ACEITA
#     "bac",  # INVALIDA
#     "abab",  # ACEITA
#     "baba",  # ACEITA
#     "abba",  # ACEITA
#     "babaab",  # ACEITA
#     "ababab",  # ACEITA
#     "bababa",  # ACEITA
#     "abababa",  # REJEITA
#     "bababab",  # REJEITA
# ]

# print(
#     json.dumps(
#         process(load_automata("automata-2024-t1/examples/01-simples.txt"), words),
#         indent=4,
#     )
# )
# print(
#     json.dumps(
#         process(load_automata("automata-2024-t1/examples/02-invalido.txt"), words),
#         indent=4,
#     )
# )
# print(
#     json.dumps(
#         process(load_automata("automata-2024-t1/examples/03-invalido.txt"), words),
#         indent=4,
#     )
# )
# print(
#     json.dumps(
#         process(load_automata("automata-2024-t1/examples/04-invalido.txt"), words),
#         indent=4,
#     )
# )
# print(
#     json.dumps(
#         process(load_automata("automata-2024-t1/examples/05-invalido.txt"), words),
#         indent=4,
#     )
# )
# nice
