""" Variaveis globais"""
ESTADOINICIAL = ""
ALFABETO  = ""
ESTADO = ""
ESTADOSFINAIS = ""
NODOS  = ""

def load_automata(filename):
    """Chama arquivo e abre"""
    with open(filename, encoding="utf-8") as arq:
        arquivo = arq.readlines()
        linha = arquivo.split("\n")

# Usado quando você usa a instrução "global" para atualizar uma variável global.
# Pylint desencoraja seu uso. Isso não significa que você não possa usá-lo!
        global ESTADOINICIAL
        ESTADOINICIAL = linha[0]
        global ALFABETO
        ALFABETO = linha[1].split(" ") 
        global ESTADO 
        ESTADO = linha[2].split(" ")        
        global ESTADOSFINAIS 
        ESTADOSFINAIS = linha[3].split(" ")        
        global NODOS   
        NODOS = linha[4:]        
        
def procura_estado(automata, words):
    """procura estados"""
    for nodo in NODOS:
        n = nodo.split(" ")
        if n[0] == automata and words == n[2]:
            return n[1]
    return None

def process(automata, words):
    """Processo"""
    i = -1
    for letra in words:
        i += 1
        atual =  procura_estado(atual, letra)
        if atual is None:
            print("INVALIDA \n ")
            break
        else:
            print(atual + ", " + letra)
            if i != len(words) - 1:
                print("Para")
            else:
                if atual in ESTADOSFINAIS:
                    print("\n ACEITA ")
                else:
                    print("\n REJEITA")                   