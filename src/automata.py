"""Implementação de autômatos finitos."""

from typing import List, Dict


def load_automata(filename) -> tuple[List[str], List[str], List[tuple[str, str, str]], str, List[str]]:
    try:
        with open(filename, "rt") as input_file:
            alphabet: List[str] = input_file.readline().strip().split()
            state_list: List[str] = input_file.readline().strip().split()
            end_state_list: List[str] = input_file.readline().strip().split()
            start_state: str = input_file.readline().strip()
            transition_rule_list: List[tuple[str, str, str]] = []
            
            # region ESTADOS FINAIS NÃO ESTÃO PRESENTES NO CONJUNTO DE ESTADOS
            try:
                for end_state in end_state_list:
                    if end_state not in state_list:
                        raise ValueError("Estados finais não estão presentes no conjunto de estados")
            except ValueError as e:
                error(e)
            # endregion ESTADOS FINAIS NÃO ESTÃO PRESENTES NO CONJUNTO DE ESTADOS
            
            # region ESTADO INICIAL NÃO ESTÁ PRESENTE NO CONJUNTO DE ESTADOS
            try:
                if start_state not in state_list:
                    raise ValueError("Estado inicial não está presente no conjunto de estados")
            except ValueError as e:
                error(e)
            # endregion ESTADO INICIAL NÃO ESTÁ PRESENTE NO CONJUNTO DE ESTADOS

            for line in input_file:
                if line == "":
                    break
                else:
                    split_line: List[str] = line.split()
                    transition_rule_list.append((split_line[0], split_line[1], split_line[2]))
                    
            # region ERROS NA TRANSIÇÃO
            try:
                for transition_rule in transition_rule_list:
                    if transition_rule[2] not in state_list:
                        raise ValueError("Transição leva a estado que não está no conjunto de estados")
                    if transition_rule[0] not in state_list:
                        raise ValueError("Transição parte de estado que não está no conjunto de estados")
                    if transition_rule[1] not in alphabet:
                        raise ValueError("Transição utiliza símbolo inválido")
            except ValueError as e:
                error(e)
            # endregion ERROS NA TRANSIÇÃO

            return state_list, alphabet, transition_rule_list, start_state, end_state_list
    except FileNotFoundError as error:
        error(error)


def process(automata: tuple[List[str], List[str], List[tuple[str, str, str]], str, List[str]], words: List[str]) -> dict[str, str]:
    final_map: Dict[str: str] = {}
    
    for word in words:
        path: List[str] = [automata[3]]
        for symbol in word:
            transition_rule: tuple[str, str, str] = next(
                filter(lambda e: path[-1] == e[0] and symbol == e[1], automata[2]), None)
            if transition_rule is None:
                final_map[word] = "INVALIDA"
                break
            else:
                path.append(transition_rule[2])
        if word in final_map:
            pass
        elif path[-1] in automata[4]:
            final_map[word] = "ACEITA"
        else:
            final_map[word] = "REJEITA"
    return final_map


read_automata = load_automata("examples/01-simples.txt")
words: List[str] = input("Digite paravras para o autômato: ").split()
status = process(read_automata, words)

# Q -> LISTA DE ESTADOS
# SIGMA -> ALFABETO
# DELTA -> LISTA DE TRANSIÇÃO DE ESTADOS
# q0 -> ESTADO INICIAL
# F -> LISTA DE ESTADOS FINAIS
