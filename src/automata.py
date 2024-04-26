"""Implementação de autômatos finitos."""


def load_automata(filename):

 with open(filename, "rt") as arquivo:
    arquivo = arq.readlines()
    linha = arquivo.split("\n")

    estadoInicial = ""

    estadoInicial = linha[0]
    alfabeto = linha[1].split(" ")
    estados = linha[2].split(" ")
    estadosFinais = linha[3].split(" ")
    nodos = linha[4:]

# print("Estado Inicial:", estadoInicial)
# print("Alfabeto:", alfabeto)
# print("Estados:", estados)
# print("Estados Finais:", estadosFinais)
# print("Nodos:", nodos)
    pass



# palavra = input("Informe a palavra: ")




def process(automata, words):
  for nodo in nodos:
    n = nodo.split(" ")
    if n[0] == automata and words == n[2]:
      return n[1]
  return None

atual = estadoInicial    
i = -1
for letra in palavra:
  i += 1
  atual = process(atual, letra)
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
        
   # for word in words:
        # tenta reconhecer `word`
