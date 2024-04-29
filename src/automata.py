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

    with open(filename, "rt") as arquivo:
        # processa arquivo...
        alphabet = tuple( arquivo.readline().strip().split() )
        states = tuple( arquivo.readline().strip().split() )
        finalStates = tuple( arquivo.readline().strip().split() )
        initialState = arquivo.readline().strip()
        delta = list()
        for line in arquivo:
            tempEdge = tuple( line.strip().split() )
            delta.append( tempEdge )

        pass

    if not initialState in states:
        raise Exception ("invalid initial state")

    for state in finalStates:
        if not (state in states):
            raise Exception ("invalid final state")
    
    for edge in delta:
        if not ( edge[0] in states and edge[1] in alphabet and edge[2] in states ):
            raise Exception ("invalid edge")
        
    return ( states, alphabet, delta, initialState, finalStates )

def process(automata, words):
    """
    Processa a lista de palavras e retora o resultado.
    
    Os resultados válidos são ACEITA, REJEITA, INVALIDA.
    """
    delta = automata[0]
    alphabet = automata[1]
    delta = automata[2]
    inicialState = automata[3]
    finalStates = automata[4]
    result = dict()
    for word in words:
        currentState = inicialState
        isValidWord = True
        for symbol in word:
            if not ( symbol in alphabet ):
                result[word] = "INVALIDA"
                isValidWord = False
                break
            for edge in delta:
                if edge[0] == currentState and  edge[1] == symbol:
                    print(edge)
                    currentState = edge[2]
                    break
        if isValidWord:
            if currentState in finalStates:
                result[word] = "ACEITA"
            else:
                result[word] = "REJEITA"

    return result
