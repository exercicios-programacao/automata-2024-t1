"""Implementação de autômatos finitos."""


def load_automata(filename: str):
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
        lines = arquivo.readlines()
        sigma = lines[0].strip().split()
        q = lines[1].strip().split()
        f = lines[2].strip().split()
        for estado in f:
            if estado not in q:
                raise ValueError("Estado final não está na lista de estados.")
        q0 = lines[3].strip()
        if q0 not in q:
            raise ValueError("O estado inicial não está na lista de estados.")
        delta = {}
        for linha in lines[4:]:
            origem, simbolo, destino = linha.strip().split()
            if origem not in q or destino not in q or simbolo not in sigma:
                raise ValueError("Transição inválida")
            if origem not in delta:
                delta[origem] = {}
            delta[origem][simbolo] = destino
    return q, sigma, delta, q0, f


def process(automata, words):
    """
    Processa a lista de palavras e retora o resultado.

    Os resultados válidos são ACEITA, REJEITA, INVALIDA.
    """
    sigma, delta, q0, f = automata
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
                if atual in f:
                    resultado[word] = 'ACEITA'
                else:
                    resultado[word] = 'REJEITA'
    return resultado
