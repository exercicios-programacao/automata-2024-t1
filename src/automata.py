def load_automata(filename: str) -> tuple:
    with open(filename, "rt") as arquivo:
        lines = arquivo.readlines()

        sigma = lines[0].strip().split()

        Q = lines[1].strip().split()
        F = lines[2].strip().split()
        for estado in F:
            if estado not in Q:
                raise Exception("Estado final '{}' não está na lista de estados.".format(estado))

        q0 = lines[3].strip()
        if q0 not in Q:
            raise Exception("O estado inicial não está na lista de estados.")

        delta = {}
        for linha in lines[4:]:
            origem, simbolo, destino = linha.strip().split()
            if origem not in Q or destino not in Q or simbolo not in sigma:
                raise Exception("Transição inválida")
            if origem not in delta:
                delta[origem] = {}
            delta[origem][simbolo] = destino

    return Q, sigma, delta, q0, F

def process(automata, words):
    Q, sigma, delta, q0, F = automata
    resultado = {}

    for word in words:
        letras = list(word)
        
        for letra in letras:
            if letra not in sigma:
                resultado[word] = 'INVALIDA'
                break
        
        else:
            atual = q0
            for letra in letras:
                if letra in delta.get(atual, {}):
                    atual = delta[atual][letra]
                else:
                    resultado[word] = 'REJEITA'
                    break
            else:
                if atual in F:
                    resultado[word] = 'ACEITA'
                else:
                    resultado[word] = 'REJEITA'
                
    return resultado
