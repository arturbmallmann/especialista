from classDiagnostico import *
from classPerguntas import *

se = Diagnostico()
pergunta = Pergunta()


while se.probabilidade() != 100 and se.probabilidade() != 0 :
    string = pergunta.texto(se)
    se.pergunta(string[0],string[1])
    print('probabilidade é %d' %(se.probabilidade()))
    print(se.resultado)
    if se.probabilidade() == 100:
        print('O Diagnostico é: ',se.resultado[0])    
    elif se.probabilidade() == 0:
        print('Não posso ajudar, procure ajuda profissional!')
