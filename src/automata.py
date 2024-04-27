"""Implementação de autômatos finitos."""


def load_automata(filename):
    with open(filename, "rt") as arquivo:
        content = arquivo.readlines()
        content = [line.split() for line in content]
        return content


def process(automata, words):
    result = {}
    for x in words:
        currentState = ''.join(automata[3])
        splitWord = [i for i in x]
        for y in splitWord:
            if(y not in automata[0]):
                result[x] = 'INVALIDA'
        cont = 0
        if(x not in result):
            while(cont < len(splitWord)):
                for states in automata[4:]:
                    for state in states:
                        if(currentState == state and cont < len(splitWord)):
                            if(splitWord[cont] == states[1]):
                                currentState = states[2]
                                cont = cont + 1
                        break
            if(currentState in automata[2]):
                result[x] = 'ACEITA'
            else:
                result[x] = 'REJEITA'
    return result