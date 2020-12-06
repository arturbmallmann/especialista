from classDiagnostico import *
from classPerguntas import *

from pathlib import Path
path = Path()
dbs=[str(x).replace('_d.db','') for x in path.iterdir() if str(x).endswith("_d.db") ]
qual = int(input("Qual programa deseja executar? 1..{}:\n{}".format(len(dbs),
                                                                    [str(n+1)+" "+x for n,x in zip(range(len(dbs)),dbs)]
                                                                    ))) -1
se = Diagnostico(dbs[qual]+'_d.db')
pergunta = Pergunta(dbs[qual]+'_p.db')



while se.probabilidade() != 100 and se.probabilidade() != 0 :
    print (se.my_dict)
    string = pergunta.texto(se)
    se.pergunta(string[0],string[1])
    print('probabilidade é %d' %(se.probabilidade()))
    print(se.resultado)
    if se.probabilidade() == 100:
        print('O Diagnostico é: ',se.resultado[0])    
    elif se.probabilidade() == 0:
        print('Não posso ajudar, procure ajuda profissional!')
