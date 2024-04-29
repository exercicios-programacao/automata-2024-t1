def load_automata(filename):
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file.readlines()]

        
        Sigma = lines[0].split()
        Q = lines[1].split()
        F = lines[2].split()
        q0 = lines[3].strip()
        transitions = lines[4:]

       
        delta = {state: {} for state in Q}
        for transition in transitions:
            parts = transition.split()
            state_from = parts[0]
            symbol = parts[1]
            state_to = parts[2]
            if symbol in delta[state_from]:
                raise Exception("Non-deterministic transition found")
            delta[state_from][symbol] = state_to

        return (Q, Sigma, delta, q0, set(F))
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found")
    except Exception as e:
        raise Exception(f"Error parsing the automaton file: {str(e)}")

def process(automata, words):
    Q, Sigma, delta, q0, F = automata
    results = {}
    
    for word in words:
        current_state = q0
        invalid = False
        
        for char in word:
            if char not in Sigma:
                results[word] = "INVÁLIDA"
                invalid = True
                break
            try:
                current_state = delta[current_state][char]
            except KeyError:
                results[word] = "REJEITA"
                invalid = True
                break
        
        if not invalid:
            if current_state in F:
                results[word] = "ACEITA"
            else:
                results[word] = "REJEITA"
    
    return results