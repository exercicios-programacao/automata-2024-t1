import os

class Automato:
    def __init__(self, sigma, Q, delta, q0, F): 
        self.sigma = sigma # alfabeto
        self.Q = Q # conjunto de estados
        self.q0 = q0 # estado inicial
        self. F = F # estados finais
        self.delta = delta # função de transição 


# pega os dados de um automato a partir dos arquivos na pasta examples
def load_automata(nome_arquivo: str) -> Automato:
    with open(nome_arquivo, "rt") as arquivo:
        linhas = arquivo.readlines()
        if len(linhas) < 5:
            raise Exception("Arquivo inválido por número insuficiente de linhas") # erro por poucas linhas no automato

    # coloca cada linha do arquivo em uma variável
    linhaAlfabeto = linhas[0].strip().split()
    linhaEstados = linhas[1].strip().split()
    linhaEstadoFinal = linhas[2].strip()
    linhaEstadoInicial = linhas[3].strip()
    linhasTransicoes = [linha.strip().split() for linha in linhas[4:]]

    if len(linhaAlfabeto) < 1 or len(linhaEstados) < 1 or len(linhaEstadoInicial) < 1:
        raise Exception("Arquivo inválido por falta de conteúdo no autômato")  # erro por ter menos informação no automato

    automato = Automato(linhaEstados, linhaAlfabeto, {}, linhaEstadoInicial, linhaEstadoFinal)
    for origem, alfabeto, destino in linhasTransicoes:
        automato.delta[(origem, alfabeto)] = destino # colocando as transições no dicionario ex: (q0, a): q1

    return automato

def process(automato: Automato, palavras) -> dict:
    resultados = {}
    for palavra in palavras:
        estadoAtual = automato.q0
        palavraValida = True # começa com a palavra sendo valida
        for alfabeto in palavra:
            transicaoValida = False # começa com a transição não estando no automato
            for origem, alfabeto in automato.delta.keys():
                if origem == estadoAtual and alfabeto[0] == alfabeto: # verifica se tem algum estado e alfabeto iguais os do automato
                    estadoAtual = automato.delta[(origem, alfabeto)] # muda o estado atual
                    transicaoValida = True # transição foi
                    break
            if transicaoValida == False:
                palavraValida = False
                break
        if palavraValida == True:
            if estadoAtual in automato.F:
                resultados[palavra] = "ACEITA"
            else:
                resultados[palavra] = "REJEITA"
        else:
            resultados[palavra] = "INVÁLIDA"
    
    return resultados



if __name__ == "__main__":
    diretorioAtual = os.path.dirname(__file__)  # deu problema pra ler arquivo e o chat gpt disse pra por isso e funcionou
    caminhoAbsoluto = os.path.join(diretorioAtual, "../examples/01-simples.txt") 

    automato = load_automata(caminhoAbsoluto)

    palavras = ["ab", "ba", "aaa", "bbb", "abba"] # palavras testes
    resultados = process(automato, palavras)

    print("O resultados são: \n")
    print(resultados)

