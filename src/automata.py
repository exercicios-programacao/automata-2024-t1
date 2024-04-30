from typing import List, Dict, Tuple

def load_automata(filename: str) -> Tuple:
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file.readlines()]

        Sigma = lines[0].split()
        Q = lines[1].split()
        F = lines[2].split()
        q0 = lines[3].strip()
        transitions = lines[4:]

        # Check if initial state is in the set of states
        if q0 not in Q:
            raise Exception("Initial state is not in the set of states")

        # Check if final states are in the set of states
        for final_state in F:
            if final_state not in Q:
                raise Exception("A final state is not in the set of states")

        delta = parse_transitions(transitions, Q, Sigma)

        return (Q, Sigma, delta, q0, set(F))
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found")
    except Exception as e:
        raise Exception(f"Error parsing the automaton file: {str(e)}")

def parse_transitions(transitions: List[str], Q: List[str], Sigma: List[str]) -> Dict[str, Dict[str, str]]:
    delta = {state: {} for state in Q}
    for transition in transitions:
        parts = transition.split()
        state_from = parts[0]
        symbol = parts[1]
        state_to = parts[2]

        # Check if transition uses a valid symbol
        if symbol not in Sigma:
            raise Exception("Transition uses an invalid symbol")

        # Check if transition leads to a state in the set of states
        if state_to not in Q:
            raise Exception("Transition leads to a state not in the set of states")

        if symbol in delta[state_from]:
            if state_to in delta[state_from][symbol]:
                raise Exception("Non-deterministic transition found")
        delta[state_from][symbol] = state_to
    return delta

def process_word(automata: Tuple, word: str) -> str:
    Q, Sigma, delta, q0, F = automata
    current_state = q0

    if word == "":
        return "ACEITA" if current_state in F else "REJEITA"

    for char in word:
        if char not in Sigma:
            return "INVALIDA"
        try:
            current_state = delta[current_state][char]
        except KeyError:
            return "REJEITA"

    if current_state in F:
        return "ACEITA"
    else:
        return "REJEITA"

def process(automata: Tuple, words: List[str]) -> Dict[str, str]:
    return {word: process_word(automata, word) for word in words}