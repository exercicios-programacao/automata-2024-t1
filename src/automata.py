def load_automata(filename):
  if isinstance(filename, str):
    if not filename.endswith('.txt'):
      filename += '.txt'
    resposta = {}
  else:
    raise Exception('O tipo esperado para o nome do arquivo é string')

  try:
    with open(filename, "rt") as arquivo:
      linhas, regras = arquivo.readlines(), []
      for linha in linhas:

        if linha == linhas[0]:
          resposta['simbolos'] = linha.strip().split(' ')

        elif linha == linhas[1]:
          resposta['estados'] = linha.strip().split(' ')

        elif linha == linhas[2]:
          final_states = []
          for estado in linha.strip().split(' '):
            if estado in resposta['estados']:
              final_states.append(estado)
            else:
              raise Exception('Os estados finais devem estar presentes na descrição do autômato')
          resposta['estados_finais'] = final_states

        elif linha == linhas[3]:
          if linha.strip() in resposta['estados']:
            resposta['estado_inicial'] = linha.strip()
          else:
            raise Exception('O estado inicial não está presente na descrição do autômato')

        else:
          linha = linha.strip().split(' ')
          if len(linha) >= 3:
            if linha[0] in resposta['estados'] and linha[2] in resposta['estados'] and linha[1] in resposta['simbolos']:
              try:
                regras.append(tuple(linha))
              except ValueError:
                raise Exception('O valor não pôde ser convertido para tupla e inserido nas regras do autômato')
            else:
              raise Exception('Os estados e símbolos devem estar presentes na descrição do autômato')
          else:
              raise Exception('As regras de transição precisam de no mínimo 3 parâmetros')

      resposta['regras'] = regras
      return resposta          
  except FileNotFoundError:
    raise Exception('O arquivo não foi encontrado no sistema')


def process(automata, words):
    if isinstance(automata, dict) and isinstance(words, list):
        for w in words:
            if not isinstance(w, str):
                raise Exception('As palavras devem ser do tipo string')
    else:
        raise Exception('O tipo esperado para o autômato é dict e para a palavra é list')

    try:
        simbolos = automata['simbolos']
        estados = automata['estados']
        estados_finais = automata['estados_finais']
        estado_inicial = automata['estado_inicial']
        regras = automata['regras']
    except KeyError:
        raise Exception('O autômato não possui todos os campos esperados')

    resposta = []

    for word in words:
        container = None
        estado_atual = estado_inicial

        for char in word:
            if container:
                break

            if char not in simbolos:
                container = resposta.append((word, 'INVALIDA'))
                break

            for regra in regras:
                if regra[0] == estado_atual and regra[1] == char:
                    estado_atual = regra[2]
                    break
            else:
                container = resposta.append((word, 'REJEITA'))
                break
        else:
            if estado_atual in estados_finais:
                container = resposta.append((word, 'ACEITA'))
            else:
                container = resposta.append((word, 'REJEITA'))
    return resposta
