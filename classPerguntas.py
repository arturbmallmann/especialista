from random import *
class Pergunta:
    def __init__(self):
        self.perguntas_tema = dict()
        arq = open('perguntas.txt','r')
        for p,s in [x.replace('\n','').split('-') for x in arq]:
            if self.perguntas_tema.get(s) == None:
                self.perguntas_tema.update({s:[p]})
            else:
                self.perguntas_tema[s].append(p)
    def texto(self,se):
        #print(se.get_sintomas(se.resultado[1]))
        sintomas = []
        for r in se.resultado:
            sintomas += se.get_sintomas(r)
        temas_possiveis = [t for t in sintomas if self.perguntas_tema.get(t) != None]
        print('temas possiveis: {}'.format(temas_possiveis))
        tema = temas_possiveis[randint(0,len(temas_possiveis)-1)]
        perguntas = self.perguntas_tema.get(tema)
        string = (perguntas[randint(0,len(perguntas)-1)] , tema)
        return string
