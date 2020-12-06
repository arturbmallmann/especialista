from random import *
class Pergunta:
    def __init__(self,nome_arq):
        self.perguntas_tema = dict()
        arq = open(nome_arq,'r')
        for p,s in [x.replace('\n','').split('-') for x in arq]:
            if self.perguntas_tema.get(s) == None:
                self.perguntas_tema.update({s:[p]})
            else:
                self.perguntas_tema[s].append(p)
    def texto(self,se):
        #print(se.get_sintomas(se.resultado[1]))
        #[print("perguntas {}: {}".format(x,self.perguntas_tema[x])) for x in self.perguntas_tema.keys()]
        sintomas = []
        for r in se.resultado:
            sintomas = sintomas + [s for s in se.get_sintomas(r) if sintomas.count(s) == 0 ]
        print("sintomas: {}".format(sintomas))
        temas_possiveis = [t for t in sintomas if self.perguntas_tema.get(t) != None or self.perguntas_tema.get('n_'+t)]
        print('Sintomas não descartados: {}'.format(temas_possiveis))
        tema = temas_possiveis[randint(0,len(temas_possiveis)-1)]
        perguntas = self.perguntas_tema.get(tema)
        string = (perguntas[randint(0,len(perguntas)-1)] , tema)
        return string
