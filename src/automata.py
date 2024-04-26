"""Implementação de autômatos finitos."""


def load_automata(filename):
    """
    Lê os dados de um autômato finito a partir de um arquivo.

    A estsrutura do arquivo deve ser:

    <lista de símbolos do alfabeto, separados por espaço (' ')>
    <lista de nomes de estados>
    <lista de nomes de estados finais>
    <nome do estado inicial>
    <lista de regras de transição, com "origem símbolo destino">

    Um exemplo de arquivo válido é:

    ```
    a b
    q0 q1 q2 q3
    q0 q3
    q0
    q0 a q1
    q0 b q2
    q1 a q0
    q1 b q3
    q2 a q3
    q2 b q0
    q3 a q1
    q3 b q2
    ```

    Caso o arquivo seja inválido uma exceção Exception é gerada.

    """


arq = open("arquivo.txt")
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

palavra = input("Informe a palavra: ")

atual = estadoInicial


def process(automata, words):
  for nodo in nodos:
    n = nodo.split(" ")
    if n[0] == automata and words == n[2]:
      return n[1]
  return None
    
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
