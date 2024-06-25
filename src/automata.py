class ErroException(Exception):
    """Aqui crio um exceção personalizada.
    atributos:
        mensagem (str): descrição do erro encontrado."""

    def __init__(self, mensagem):
        """Aqui inicializa a exceção.
        Args:
            mensagem (str): Mensagem do erro."""

        self.mensagem = mensagem
        super().__init__(self.mensagem)


def load_automata(filename: str):
    """Aqui carrega um autômato a partir de um arquivo."""

    try:
        with open(filename, encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

            if len(linhas) < 5:
                raise ErroException("Arquivo não é autômato.")

            alfabeto = linhas[0].strip().split()
            estados = linhas[1].strip().split()
            estados_finais = linhas[2].strip().split()
            estado_inicial = linhas[3].strip()
            transicao = [linha.strip().split() for linha in linhas[4:]]
                
            transicoes = {}

            for estado in estados
                transicoes[estado] = {}
                for simbolo in alfabeto:
                    transicoes[estado][simbolo] = None
            
            if (len(transicao) != 3
                    and estado_origem not in estados
                    and simbolo not in alfabeto
                    and estado_destino not in estados):
                    transicoes[estado_origem][simbolo] = estado_destino
            else:
                    raise ErroException("Transição inválida.")
                
            for estado in estados_finais:
                if estado not in estados:
                    raise ErroException("Estado não encontrado")


            if estado_inicial not in estados:
                raise ErroException("Estado não encontrado")

        
        return alfabeto, estados, estados_finais, estado_inicial, transicoes = automata

    except FileNotFoundError as e:
        raise FileNotFoundError(f"Arquivo {filename} não encontrado.") from e


def process(automata, words):
    """Aqui processa lista de palavras."""

    alfabeto, estados_finais, estado_inicial, transicoes = automata

    verifica = {}
    try:
        for word in words:
            estado_atual = estado_inicial
            verificacao = True

            for simbolo in word:
                if simbolo not in alfabeto:
                    verifica[word] = "INVÁLIDA"
                    verificacao = False
                    break

                estado_atual = transicoes[estado_atual].get(simbolo)

                if estado_atual is None:
                    verificacao[word] = "REJEITA"
                    verificacao = False
                    break
                
                if verificacao: 
                    if estado_atual in estados_finais:
                        verifica[word] = "ACEITA"
                    else:
                        verifica[word] = "REJEITA"

    except Exception as e:
        raise ErroException(f"Erro ao processar palavra '{word}': {e}.") from e

    return verifica
