"""Implementação de autômatos finitos."""
    
   
def load_automata(filename):

    arq = open(filename, "rt")
    arquivo = arq.readlines()
    linha = arquivo.split("\n")

    global estadoInicial
    global alfabeto 
    global estados 
    global estadosFinais 
    global nodos   

    estadoInicial = linha[0]
    alfabeto = linha[1].split(" ")
    estados = linha[2].split(" ")
    estadosFinais = linha[3].split(" ")
    nodos = linha[4:]        


def process(automata, words):
    for nodo in nodos:
     n = nodo.split(" ")
     if n[0] == automata and words == n[2]:
        return n[1]
    return None


    i = -1
    for letra in palavra:
        i += 1
        atual = procuraEstados(atual, letra)
        if atual is None:
            print("INVALIDA \n ")
            break
        else:
            print(atual + ", " + letra)
            if i != len(palavra) - 1:
                print("Para")
            else:
                if atual in estadosFinais:
                    print("\n ACEITA ")
                else:
                    print("\n REJEITA")