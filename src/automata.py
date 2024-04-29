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

    simbolos = [] 
    estados = []
    estadosFinais = []
    estadoInicial = []
    regrasTransicao = []
    auxiliar = []

    with open(filename, "rt") as arquivo:
        # processa arquivo.. .
        for linha in arquivo:
            linha = linha.strip()
            linha = linha.split()
            auxiliar.append(linha)
    
    simbolos = auxiliar[0]
    estados = auxiliar[1]
    estadosFinais = auxiliar[2]
    estadoInicial = auxiliar[3] 
    regrasTransicao = auxiliar[4:]

    print("Simbolos: ", simbolos)
    print("estados:", estados)
    print("Estados Finais: ", estadosFinais)
    print("Estado Inicial: ", estadoInicial)
    print("Regras de Transição: ", regrasTransicao)


    """
    valida simbolos
    """
    for valor in simbolos:
        if not isinstance(valor, str) or not valor.isalpha():
            raise Exception("simbolos inválidos")

    """
    valida estados
    """        
    for valor in estados:
        if not valor.startswith("q"):
            raise Exception("Estados Inválidos")
    
    """
    valida Estados Finais
    """
    for valor in estadosFinais:
        if valor not in estados:
            raise Exception("O estado final não está contido no conjunto de estados")
    
    """
    valida estado inicial
    """
    for valor in estadoInicial:
        if valor not in estados:
            raise Exception("O estado inicial não está contido no conjunto de estados")
        
    """
    valida transicoes
    """
    for valor in regrasTransicao:
        if valor[0] not in estados or valor[1] not in simbolos or valor[2] not in estados:
            raise Exception("Regras de Transição incorretas")

    automatoValido = (simbolos, estados, estadosFinais, estadoInicial, regrasTransicao)  
    return automatoValido



def process(automata, words):

    simbolos, estados, estadosFinais, estadoInicial, regrasTransicao = automata

    """
    Processa a lista de palavras e retora o resultado.
    
    Os resultados válidos são ACEITA, REJEITA, INVALIDA.
    """



    for word in words:
        # tenta reconhecer `word`
        pass