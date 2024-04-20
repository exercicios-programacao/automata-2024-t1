from collections import namedtuple
class RespostaAutomato:
    def __init__(self,palavra,resultado):
        self.palavra = palavra
        self.resultado = resultado

    def __repr__(self):
        return '%s -> %s' % (self.palavra, self.resultado)

class main:
    listaPares = []
    listaRegras = []
    #namedtuple('listaPares',['palavra' , 'resultado'])
    resultado = 'INVALIDA'
    palavra = "ababa"
    RegrasTransicao= namedtuple('RegrasTransicao',['origem' , 'símbolo', 'destino'])
    Regras=RegrasTransicao('q0','a','q1')
    listaRegras.append(Regras)
    Regras=RegrasTransicao('q1','a','q1')
    listaRegras.append(Regras)
    Regras=RegrasTransicao('q1','b','q0')
    listaRegras.append(Regras)
    print("regras:")
    for regras in listaRegras:
        print("\torigem: "+regras[0]+" símbolo: "+regras[1]+" destino: "+regras[2])
        #falta tranformar os simbolos numa lista de simbolos
    automato={
             'simbolos':['ab'],
             'estados':['q0','q1'],
             'estadosFinais':['q1','q0'],
             'NomeEstadoInicial':"q0",
             'RegrasTransicao':listaRegras
        }
    def DescricaoAutomatoValida(automato):
        if (automato.get('simbolos')!=''
        and len(automato.get('estados'))>0
        and len(automato.get('estadosFinais'))>0
        and automato.get('NomeEstadoInicial')!=''
        and len(automato.get('RegrasTransicao'))>0):
            #verifica se os estados finais é valido com algum estado
            #verifica estados finais
            cont=0
            for esF in automato.get('estadosFinais'):
                for es in automato.get('estados'):
                    if(esF == es):
                        cont+=1
                        StatusAutomato='VALIDO'
                        break
            #verifica se a mesma quantidade de estados finais é valido com algum estado
            #verifica estados finais
            if(len(automato.get('estadosFinais')) == cont):
                StatusAutomato='VALIDO'
            else:
                StatusAutomato='INVALIDO'
                return StatusAutomato
            #verifica NomeEstadoInicial
            for es in automato.get('estados'):
                if(automato.get('NomeEstadoInicial') == es):
                    StatusAutomato='VALIDO'
                    break
            else:
                StatusAutomato='INVALIDO'
                return StatusAutomato
            #Falta implementar a verificacao das regras de transição
            print(StatusAutomato)
            print("VALIDO")
        else:
            StatusAutomato='INVALIDO'
            return StatusAutomato
    retStatusAutomato = DescricaoAutomatoValida(automato)
    
    #print(automato)
    EstadoInicial =  str(automato.get('NomeEstadoInicial'))
    estadosFinais =  str(automato.get('estadosFinais'))
    simbolos = str(automato.get('simbolos'))
    print("Estado inicial:\n\t"+EstadoInicial,"\nestadosFinais:\n\t"+estadosFinais,"\nSimbolos:\n\t"+simbolos)
    #Verificar se uma palavra válida, ou seja, se todos os símbolos da palavra fazem parte do alfabeto da lingugaem
    def VerificaPalavra(palavra,simbolos):
        for caractere in str(palavra):
            if caractere in(simbolos):
                #print("SIM")
                resultado = 'VALIDA'
            else:
                #print("NAO")
                resultado = 'INVALIDA'
                break
        return tuple((palavra,resultado))

    retTuple = VerificaPalavra(palavra,simbolos)
    listaPares.append(retTuple)
    print(listaPares)
    def AutonomoReconhecePalavra(palavra,automato):
        print("funcao")
        caminhoDoAutonomo=""
        EstadoInicial =  str(automato.get('NomeEstadoInicial'))
        estadosFinais =  str(automato.get('estadosFinais'))
        simbolos = str(automato.get('simbolos'))
        listaRegras= automato.get('RegrasTransicao')
        for regras in listaRegras:
            print("\torigem: "+regras[0]+" símbolo: "+regras[1]+" destino: "+regras[2])
        resultado = "OK"
        contador = 0;
        palavraAserMontada=""
        if str(palavra)!="":
            for caractere in str(palavra):
                #verifica se é posição do estado inicial
                if contador == 0:
                    for regras in listaRegras:
                        #se origem for igual estado inicial
                        if regras[0] == EstadoInicial:
                            #se simbolo for igual caracter
                            if regras[1] == caractere:
                                caminhoDoAutonomo = caminhoDoAutonomo+ "Orig: " + regras[0] + " Simb: " + regras[1] + " Destino: " + regras[2]+ "\n"
                                ProximaOrigem = regras[2]
                                palavraAserMontada += caractere
                                break
                    else:
                        ProximaOrigem=0
                        resultado="REJEITA"
                        break
                else:
                    for regras in listaRegras:
                        #se origem for igual estado inicial
                        if regras[0] == ProximaOrigem:
                            #se simbolo for igual caracter
                            if regras[1] == caractere:
                                caminhoDoAutonomo = caminhoDoAutonomo+ "Orig: "+ regras[0]+  " Simb: " + regras[1] + " Destino:"+regras[2] + "\n"
                                ProximaOrigem = regras[2]
                                palavraAserMontada += caractere
                                break
                    else:
                        ProximaOrigem=0
                        resultado="REJEITA"
                        break
                contador+=1
        
        if palavraAserMontada == str(palavra):
            if ProximaOrigem in estadosFinais:
                resultado = "ACEITA"
            else:
                resultado = "REJEITA"
        else:
            resultado = "REJEITA"
        print("\n")
        print("CaminhoAutonomo: "+caminhoDoAutonomo)
        print(palavraAserMontada)
        print(resultado)    
        return tuple((palavra,resultado))

    retorno = AutonomoReconhecePalavra(palavra,automato)            
