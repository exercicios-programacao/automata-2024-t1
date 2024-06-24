def load_automata(filename: str):
    try:
        with open(filename) as arquivo:
            linhas = arquivo.readlines()

            if len(linhas) < 5:
                raise Exception("Arquivo não é autômato")

            alfabeto = linhas[0].strip().split()
            estados = linhas[1].strip().split()
            estadosFinais = linhas[2].strip().split()
            estadoInicial = linhas[3].strip()

            transicoes = {}

            for linha in linhas[4:]:
                transicao = linha.strip().split()
                if len(transicao) != 3 or transicao[0] not in estados or transicao[1] not in alfabeto or transicao[2] not in estados:
                    raise Exception("Transição inválida encontrada")
                
                estado_origem = transicao[0]
                simbolo = transicao[1]
                estado_destino = transicao[2]

                if estado_origem not in transicoes:
                    transicoes[estado_origem] = {}
                
                transicoes[estado_origem][simbolo] = estado_destino

        return alfabeto, estados, estadosFinais, estadoInicial, transicoes

    except FileNotFoundError as e:
        raise Exception(f"Arquivo {filename} não encontrado") from e
def process(automata, words):
    alfabeto, estados, estadosFinais, estadoInicial, transicoes = automata

    verifica = {}
    try:
        for word in words:
            if not isinstance(word, str):
                raise Exception(f"A palavra '{word}' não é uma string válida")

            if any(simbolo not in alfabeto for simbolo in word):
                verifica[word] = "INVÁLIDA"
                continue

            estadoAtual = estadoInicial
            for simbolo in word:
                if estadoAtual in transicoes and simbolo in transicoes[estadoAtual]:
                    estadoAtual = transicoes[estadoAtual][simbolo]
                else:
                    verifica[word] = "REJEITA"
                    break
            else:
                if estadoAtual in estadosFinais:
                    verifica[word] = "ACEITA"
                else:
                    verifica[word] = "REJEITA"

    except Exception as e:
        raise Exception(f"Erro ao processar palavra '{word}': {e}") from e

    return verifica
