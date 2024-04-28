def load_automata(filename):
  if isinstance(filename, str):
      try:
          with open(filename) as f:
              lines = f.readlines()
              if len(lines) < 4:
                  raise Exception('File does not contain enough lines to represent an automata')

              symbols = tuple(lines[0].strip().split(' '))
              states = tuple(lines[1].strip().split(' '))

              final_states = tuple(state for state in lines[2].strip().split(' ') if state in states)
              if len(final_states) == 0:
                  raise Exception('Final states must be present in the automata description')

              initial_state = lines[3].strip()
              if initial_state not in states:
                  raise Exception('The initial state is not present in the automata description')

              rules = []
              for line in lines[4:]:
                  rule = tuple(line.strip().split(' '))
                  if len(rule) < 3 or rule[0] not in states or rule[1] not in symbols or rule[2] not in states:
                      raise Exception('Invalid transition rule')
                  rules.append(rule)

              return {
                  'symbols': symbols,
                  'states': states,
                  'final_states': final_states,
                  'initial_state': initial_state,
                  'rules': rules
              }
      except FileNotFoundError:
          raise Exception('File not found in the system')
  else:
      raise Exception('Expected type for filename is string')

def process(automata, word):
  if isinstance(automata, dict) and isinstance(word, list):
    for w in word:
      if not isinstance(w, str):
        raise Exception('As palavras devem ser do tipo string')
  else:
    raise Exception('O tipo esperado para o autômato é dict e para a palavra é list')

  try:
    symbols = automata['symbols']
    states = automata['states']
    final_states = automata['final_states']
    initial_state = automata['initial_state']
    rules = automata['rules']
  except KeyError:
    raise Exception('O autômato não possui todos os campos esperados')

  response = []
  words = tuple(word)

  for word in words:
    container = None
    actual_state = initial_state

    for c in word:
      if container:
        break

      if c not in symbols:
        container = (word, 'INVALIDA')
        response.append(container)
        break

      for rule in rules:
        if rule[0] == actual_state and rule[1] == c:
          actual_state = rule[2]
          break
      else:
        container = (word, 'REJEITA')
        response.append(container)
        break
    else:
      if actual_state in final_states:
        container = (word, 'ACEITA')
        response.append(container)
      else:
        container = (word, 'REJEITA')
        response.append(container)
  else:
    return response
