"""Implementação de autômatos finitos."""


class InvalidTransitionError(Exception):
    """Exceção lançada para indicar uma transição inválida no autômato."""


def load_automata(filename):
    """
    Lê os dados de um autômato finito a partir de um arquivo.

    A estrutura do arquivo deve ser:

    <lista de símbolos do alfabeto, separados por espaço (' ')>
    <lista de nomes de estados>
    <lista de nomes de estados finais>
    <nome do estado inicial>
    <lista de regras de transição, com "origem símbolo destino">

    Um exemplo de arquivo válido é:

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

    Caso o arquivo seja inválido uma exceção InvalidTransitionError é gerada.
    """
    with open(filename, 'rt', encoding="utf-8") as file:
        lines = file.read().splitlines()

    alphabet = lines[0].split()
    states = lines[1].split()
    final_states = lines[2].split()
    initial_state = lines[3]
    transitions = [line.split() for line in lines[4:]]

    delta = {}
    for state in states:
        delta[state] = {}
        for symbol in alphabet:
            delta[state][symbol] = None

    for origin, symbol, destination in transitions:
        if origin in states and symbol in alphabet and destination in states:
            delta[origin][symbol] = destination
        else:
            raise InvalidTransitionError(f"Transição inválida: {origin} {symbol} {destination}")

    # Verificar se todos os estados finais estão no conjunto de estados
    for state in final_states:
        if state not in states:
            raise InvalidTransitionError(f"Estado final não encontrado no conjunto de estados: {state}")

    # Verificar se o estado inicial está no conjunto de estados
    if initial_state not in states:
        raise InvalidTransitionError(f"Estado inicial não encontrado no conjunto de estados: {initial_state}")

    automata = (states, alphabet, delta, initial_state, final_states)
    return automata


def process(automata, words):
    """
    Processa uma lista de palavras através do autômato e retorna os resultados.

    Args:
    automata: A estrutura do autômato.
    words: Lista de palavras a serem processadas.

    Returns:
    Um dicionário com palavras como chaves e seus respectivos resultados ('ACEITA', 'REJEITA', 'INVALIDA').
    """
    _, alphabet, delta, initial_state, final_states = automata
    results = {}

    for word in words:
        current_state = initial_state
        valid = True

        for symbol in word:
            if symbol not in alphabet:
                results[word] = 'INVALIDA'
                valid = False
                break
            current_state = delta[current_state].get(symbol)
            if current_state is None:
                results[word] = 'REJEITA'
                valid = False
                break

        if valid:
            if current_state in final_states:
                results[word] = 'ACEITA'
            else:
                results[word] = 'REJEITA'

    return results