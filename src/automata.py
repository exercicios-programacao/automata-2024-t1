"""Implementação de autômatos finitos."""

""" load_automata(filename: str): -> tuple(Q, Sigma, delta, q0, F)"""
def get_F(F_list):
    F_return = []
    for F in F_list:
        F_return.append(F.strip().split(" "))
    return F_return

def get_transitional_Q(F):
    transitional_Q = []
    for element_F in F:
        element_Q = element_F[1]
        transitional_Q.append(element_Q)
    return transitional_Q

def get_transitional_state(F):
    transitional_state = []
    for element_F in F:
        transitional_state.append(element_F[0])
        transitional_state.append(element_F[2])
    return transitional_state

def automata_validate(automata):
    Q = automata[0]
    Sigma = automata[1]
    delta = automata[2]
    q0 = automata[3]
    F = automata[4]

    errorMsg = []

    if not q0 in Sigma:
        errorMsg.append("Estado inicial "+q0+" não está na lista de estados")
    
    for end_state in delta:
        if not end_state in Sigma:
            errorMsg.append("Estado final "+end_state+" não está na lista de estados")
    
    for element_Q in get_transitional_Q(F):
        if not element_Q in Q:
            errorMsg.append("Letra de transição "+element_Q+" não está no alfabeto")

    for element_state in get_transitional_state(F):
        if not element_state in Sigma:
            errorMsg.append("Estado de transição "+element_state+" não está na lista de estados")
    
    if not q0 == automata[1][0]:
        errorMsg.append("Estado inicial de transição "+automata[1][0]+" não é o estado inicial "+q0)        

    if not errorMsg:
        return "Automato Válido"
    else:
        return '; '.join(errorMsg)
    
        
def load_automata(filename):
    """
    Lê os dados de um autômato finito a partir de um arquivo.

    A estsrutura do arquivo deve ser:

    <lista de símbolos do alfabeto, separados por espaço (' ')> -> Q
    <lista de nomes de estados> -> Sigma
    <lista de nomes de estados finais> -> delta
    <nome do estado inicial> -> q0
    <lista de regras de transição, com "origem símbolo destino"> -> F

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


    try:
        with open(filename, "rt") as arquivo:
            lines = arquivo.readlines()
            pass
    except:
        print("Arquivo inválido")
    
    Q = lines[0].strip().split(" ")
    Sigma = lines[1].strip().split(" ")
    delta = lines[2].strip().split(" ")
    q0 = lines[3].strip()
    F = get_F(lines[4:])

    tuple = (Q, Sigma, delta, q0, F)

    if automata_validate(tuple) == "Automato Válido":
        return tuple
    else:
        raise Exception( automata_validate(tuple))

def get_nextState(state, letter, F):
        for transition_rule in F:
            if transition_rule[0] == state and transition_rule[1] == letter:
                return transition_rule[2]
        return None

def processWord(word, automata):
    

    Q = automata[0]
    Sigma = automata[1]
    delta = automata[2]
    q0 = automata[3]
    F = automata[4]

    curr_state = q0

    i = -1
    for letter in word:
        i += 1
        if not letter in Q:
            #print("INVALIDA")
            return "INVALIDA"
        previous_state = curr_state
        curr_state = get_nextState(curr_state, letter, F)
        if curr_state is None:
            #print("REJEITA")
            return "REJEITA"
        if i != len(word) - 1:
            pass
        #    print(previous_state+", "+letter)
        #    print("|")
        #    print("v")
        else:
            print(curr_state+", "+letter)
            if curr_state in delta:
                #print("ACEITA")
                return "ACEITA"
            else:
                #print("REJEITA")
                return "REJEITA"
    
    if word == "" and q0 in delta:
        return "ACEITA"
    else:
        return "REJEITA"




def process(automata, words):
    """
    Processa a lista de palavras e retora o resultado.
    
    Os resultados válidos são ACEITA, REJEITA, INVALIDA.
    """

    print(automata_validate(automata))

    if automata_validate(automata) == "Automato Válido":
        dict = {}
        for word in words:
            #print("\nProcessando palavra "+word+"--------------------------------------------------")
            dict[word] = processWord(word, automata)
        return dict
    else:
        return "INVALIDA"

#print(process(load_automata("./examples/feature_error_3.txt"), ["","a","b","ab","abb","aabb","abab","baba","bbaa","bbbabaaa","bbabbaa"]))
#Estados finais não estão presentes no conjunto de estados.
#print(process(load_automata("./examples/feature_error_16.txt"), ["","a","b","ab","abb","aabb","abab","baba","bbaa","bbbabaaa","bbabbaa"]))
#Estados inicial não está presente no conjunto de estados.
#print(process(load_automata("./examples/feature_error_29.txt"), ["","a","b","ab","abb","aabb","abab","baba","bbaa","bbbabaaa","bbabbaa"]))
#Transição leva a estado que não está no conjunto de estados.
#print(process(load_automata("./examples/feature_error_42.txt"), ["","a","b","ab","abb","aabb","abab","baba","bbaa","bbbabaaa","bbabbaa"]))
#Transição parte de estado que não está no conjunto de estados.
#print(process(load_automata("./examples/feature_error_55.txt"), ["","a","b","ab","abb","aabb","abab","baba","bbaa","bbbabaaa","bbabbaa"]))
#Transição utiliza símbolo inválido