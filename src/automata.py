import os

class Automato:
    def __init__(self, sigma, Q, delta, q0, F): 
        self.sigma = sigma  # alfabeto
        self.Q = Q  # conjunto de estados
        self.q0 = q0  # estado inicial
        self.F = F  # estados finais
        self.delta = delta  # função de transição


# pega os dados de um automato a partir dos arquivos na pasta examples
def load_automata(nome_arquivo: str) -> Automato:
    with open(nome_arquivo, "rt") as arquivo:
        linhas = arquivo.readlines()
        if len(linhas) < 5: # verifica a quantidade de linhas minimas no arquivo
            raise Exception("Arquivo inválido por número insuficiente de linhas")  

    # coloca cada linha do arquivo em uma variável
    linhaAlfabeto = linhas[0].strip().split()
    linhaEstados = linhas[1].strip().split()
    linhaEstadoFinal = linhas[2].strip().split()
    linhaEstadoInicial = linhas[3].strip()
    linhasTransicoes = [linha.strip().split() for linha in linhas[4:]]

    # verifica se cada linha tem a quantidade minima de informações
    if len(linhaAlfabeto) < 1 or len(linhaEstados) < 1 or len(linhaEstadoInicial) < 1:
        raise Exception("Arquivo inválido por falta de conteúdo no autômato")  

    automato = Automato(linhaAlfabeto, linhaEstados, {}, linhaEstadoInicial,linhaEstadoFinal)

    for origem, simbolo, destino in linhasTransicoes:
        automato.delta[( origem, simbolo)] = destino  # colocando as transições no dicionario ex: (q0, a): q1


    """

    Verificações de estados

    """

    # verifica se os estados finais estão no conjunto de estados
    for estadoFinal in automato.F:
        if estadoFinal not in automato.Q:
            raise Exception(f"O estado final '{estadoFinal}' não está presente no conjunto de estados.")

    # vrifica se o estado inicial está no conjunto de estados
    if automato.q0 not in automato.Q:
        raise Exception(f"O estado inicial '{automato.q0}' não está presente no conjunto de estados.")

    for origem, simbolo, destino in linhasTransicoes:
        # verifica se o estado de origem e destino das transições estão no conjunto de estados
        if origem not in automato.Q or destino not in automato.Q:
            raise Exception(f"A transição '{origem} --({simbolo})--> {destino}' possui um estado que não está presente no conjunto de estados.")

        # verificar se os símbolos de transição estão no alfabeto
        if simbolo not in automato.sigma:
            raise Exception(f"A transição '{origem} --({simbolo})--> {destino}' possui um simbolo que não está presente no alfabeto.")


    return automato

def process(automato: Automato, palavras) -> dict:
    
    resultados = {}
    for palavra in palavras:
        estadoAtual = automato.q0
        palavraValida = True

        # validação das palavras e transições
        for simbolo in palavra:
            transicaoValida = False
            for origem, simbolo_transicao in automato.delta.keys():
                if origem == estadoAtual and simbolo_transicao == simbolo: # verifica se o estado e os simbolos sao iguais aos do automato
                    estadoAtual = automato.delta[(origem, simbolo_transicao)]
                    transicaoValida = True
                    break
            if not transicaoValida: # se a transição não é válida, a palavra também não é
                palavraValida = False
                break
            
        if palavraValida:
            if estadoAtual in automato.F:
                resultados[palavra] = "ACEITA"
            else:
                resultados[palavra] = "REJEITA"
        else:
            resultados[palavra] = "INVALIDA"
    return resultados

if __name__ == "__main__":
    diretorioAtual = os.path.dirname(__file__)  # deu problema pra ler arquivo e o chat gpt disse pra por isso e funcionou
    caminhoAbsoluto = os.path.join(diretorioAtual, "../examples/01-simples.txt") 

    automato = load_automata(caminhoAbsoluto)

    palavras = ["a","b","ab","abb","aabb","abab","baba","bbaa","bbbabaaa","bbabbaa"]  # palavras testes
    resultados = process(automato, palavras)

    print("O resultados são: \n")
    print(resultados)
