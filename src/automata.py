from typing import List, Dict, Tuple


def load_automata(filename: str) -> Tuple:
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

            Sigma = lines[0].strip().split()
            Q = lines[1].strip().split()
            F = lines[2].strip().split()
            q0 = lines[3].strip()
            delta = {}

            # Check if final states are in the set of states
            if not set(F).issubset(Q):
                raise Exception("Final states are not present in the set of states")

            # Check if initial state is in the set of states
            if q0 not in Q:
                raise Exception("Initial state is not present in the set of states")

            for line in lines[4:]:
                src, symbol, dest = line.strip().split()

                # Check if transition leads to a state that is not in the set of states
                if dest not in Q:
                    raise Exception(
                        "Transition leads to a state that is not in the set of states"
                    )

                # Check if transition starts from a state that is not in the set of states
                if src not in Q:
                    raise Exception(
                        "Transition starts from a state that is not in the set of states"
                    )

                # Check if transition uses an invalid symbol
                if symbol not in Sigma:
                    raise Exception("Transition uses an invalid symbol")

                if src not in delta:
                    delta[src] = {}
                delta[src][symbol] = dest

            return Q, Sigma, delta, q0, F
    except Exception as e:
        raise Exception("Invalid automaton file format") from e


def process(automata: Tuple, words: List[str]) -> Dict[str, str]:
    Q, Sigma, delta, q0, F = automata
    results = {}

    for word in words:
        state = q0
        for symbol in word:
            if symbol not in Sigma:
                results[word] = "INVALIDA"
                break
            if symbol not in delta[state]:
                results[word] = "REJEITA"
                break
            state = delta[state][symbol]
        else:
            results[word] = "ACEITA" if state in F else "REJEITA"

    return results
