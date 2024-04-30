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
    with open(filename, "rt", encoding="utf-8") as arquivo:
        # processa arquivo...
        alphabet = tuple(arquivo.readline().strip().split())
        states = tuple(arquivo.readline().strip().split())
        final_states = tuple(arquivo.readline().strip().split())
        initial_state = arquivo.readline().strip()
        delta = []
        for line in arquivo:
            temp_edge = tuple(line.strip().split())
            delta.append(temp_edge)

    if initial_state not in states:
        raise ValueError("invalid initial state")

    for state in final_states:
        if state not in states:
            raise ValueError("invalid final state")

    for edge in delta:
        if not (
            edge[0] in states and edge[1] in alphabet and edge[2] in states
        ):
            raise ValueError("invalid edge")

    return (states, alphabet, delta, initial_state, final_states)


def process(automata, words):
    """
    Processa a lista de palavras e retora o resultado.

    Os resultados válidos são ACEITA, REJEITA, INVALIDA.
    """
    delta = automata[0]
    alphabet = automata[1]
    delta = automata[2]
    initial_state = automata[3]
    final_states = automata[4]
    result = {}
    for word in words:
        current_state = initial_state
        is_valid_word = True
        for symbol in word:
            if symbol not in alphabet:
                result[word] = "INVALIDA"
                is_valid_word = False
                break
            for edge in delta:
                if edge[0] == current_state and edge[1] == symbol:
                    current_state = edge[2]
                    break
        if is_valid_word:
            if current_state in final_states:
                result[word] = "ACEITA"
            else:
                result[word] = "REJEITA"

    return result
