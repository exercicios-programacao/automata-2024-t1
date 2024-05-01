# import json
# import os

# os.system("cls")
# meu formatter "ms-python.black-formatter" deixa feinho assim mas da pra ler melhor


def load_automata(filename):
    try:
        with open(filename, "r") as f:
            linhas = []
            for l in f.readlines():
                linhas.append(l.strip())
        # tratando o arquivo
        alfabeto = linhas[0].split(" ")
        conjuntoDeEstados = linhas[1].split(" ")
        estadosFinais = linhas[2].split(" ")
        estadoInicial = linhas[3]
        regrasDeTransicao = linhas[4:]

        # dict para guardar as transições
        dictTransicoes = {}
        for estado in conjuntoDeEstados:
            dictTransicoes[estado] = {}
            for letra in alfabeto:
                dictTransicoes[estado][letra] = ""

        for regras in regrasDeTransicao:
            regra = regras.split(" ")
            estadoInicialTransicao = regra[0]
            letra = regra[1]
            estadoFinalTransicao = regra[2]
            # exceptions
            if letra not in alfabeto:
                raise Exception(
                    f"ERRO DE ENTRADA - ALFABETO  a letra: {letra} não pertence ao alfabeto: {alfabeto}"
                )
            if estadoInicialTransicao not in conjuntoDeEstados:
                raise Exception(
                    f"ERRO DE ENTRADA - ESTADO INICIAL DE TRANSIÇÃO {estadoInicialTransicao} não pertence ao conjunto de estados: {conjuntoDeEstados}"
                )
            if estadoFinalTransicao not in conjuntoDeEstados:
                raise Exception(
                    f"ERRO DE ENTRADA - ESTADO FINAL DE TRANSIÇÃO {estadoFinalTransicao} não pertence ao conjunto de estados: {conjuntoDeEstados}"
                )
            if dictTransicoes[estadoInicialTransicao][letra] != "":
                raise Exception(
                    f"ERRO DE ENTRADA - TRANSIÇÃO NÃO DETERMINÍSTICA: {estadoInicialTransicao} - {letra} - {estadoFinalTransicao}"
                )
            # exceptions
            dictTransicoes[estadoInicialTransicao][letra] = estadoFinalTransicao
        # exceptions o retorno
        if estadoInicial not in conjuntoDeEstados:
            raise Exception(
                f"ERRO DE ENTRADA - ESTADO INICIAL {estadoInicial} não pertence ao conjunto de estados: {conjuntoDeEstados}"
            )
        for estado in estadosFinais:
            if estado not in conjuntoDeEstados:
                raise Exception(
                    f"ERRO DE ENTRADA - ESTADO FINAL {estado} não pertence ao conjunto de estados: {conjuntoDeEstados}"
                )
        for estado in dictTransicoes:
            for letra in dictTransicoes[estado]:
                if dictTransicoes[estado][letra] == "":
                    raise Exception(
                        f"ERRO DE ENTRADA - TRANSIÇÃO INCOMPLETA: {estado} - {letra} - {dictTransicoes[estado][letra]}"
                    )
        # exceptions o retorno
        return (
            conjuntoDeEstados,
            alfabeto,
            dictTransicoes,
            estadoInicial,
            estadosFinais,
        )
    # erro se erro
    except Exception as exception:
        raise Exception("ERRO DE ENTRADA" + str(exception))
    # erro se erro


def process(automata, words):
    (
        conjuntoDeEstados,
        alfabeto,
        dictTransicoes,
        estadoInicial,
        estadosFinais,
    ) = automata
    returnDict = {}

    for palavra in words:
        estadoAtual = estadoInicial
        invalida = False

        # para cada letra da palavra
        for char in palavra:

            if char not in alfabeto:  # se o char não pertence ao alfabeto é invalida
                returnDict[palavra] = "INVALIDA"
                invalida = True
                break

            try:
                estadoAtual = dictTransicoes[estadoAtual][char]
            except (
                KeyError
            ):  # se não tiver transição para o estado no dicionário é rejeitada pelo automato
                returnDict[palavra] = "REJEITA"
                invalida = True
                break

        if estadoAtual in estadosFinais and not invalida:
            returnDict[palavra] = "ACEITA"
        elif estadoAtual not in estadosFinais and not invalida:
            returnDict[palavra] = "REJEITA"
        else:
            # nada deveria chegar aqui mas se chegar deve ser invalida
            returnDict[palavra] = "INVALIDA"

    return returnDict


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
