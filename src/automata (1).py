from typing import List, Dict, Tuple

class Automata:
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0
        self.F = F

def load_automata(filename: str) -> Tuple:
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            Sigma = lines[0].strip().split(' ')
            Q = lines[1].strip().split(' ')
            F = lines[2].strip().split(' ')
            q0 = lines[3].strip()
            delta = {}

            for line in lines[4:]:
                orig, sym, dest = line.strip().split(' ')
                if orig not in delta:
                    delta[orig] = {}
                delta[orig][sym] = dest

            # Check if final states are in the set of states
            if not all(state in Q for state in F):
                raise Exception("Final states are not present in the set of states")

            # Check if the initial state is in the set of states
            if q0 not in Q:
                raise Exception("Initial state is not present in the set of states")

            # Check if transitions are valid
            for orig, transitions in delta.items():
                if orig not in Q:
                    raise Exception("Transition starts from a state that is not in the set of states")
                for sym, dest in transitions.items():
                    if sym not in Sigma:
                        raise Exception("Transition uses an invalid symbol")
                    if dest not in Q:
                        raise Exception("Transition leads to a state that is not in the set of states")

            return Automata(Q, Sigma, delta, q0, F)
    except Exception as e:
        raise Exception("Invalid automata format") from e

def process(automata: Automata, words: List[str]) -> Dict[str, str]:
    results = {}
    for word in words:
        state = automata.q0
        for symbol in word:
            if symbol not in automata.Sigma or state not in automata.delta or symbol not in automata.delta[state]:
                results[word] = 'INVALIDA'
                break
            state = automata.delta[state][symbol]
        else:
            results[word] = 'ACEITA' if state in automata.F else 'REJEITA'
    return results