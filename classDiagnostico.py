class Diagnostico():
    # metodo construtor
    def __init__(self,nome_arq):
        self.pessoa = []
        # abre o arquivo db.txt em modo leitura e passa os dados para
        # uma lista de listas de str
        self.my_dict = dict()
        arquivo = open(nome_arq,'r')
        for s,r in [x.replace('\n','').split('-') for x in arquivo]: 
            if self.my_dict.get(r) == None:
                self.my_dict.update({r:[s]})
            else:
                self.my_dict[r].append(s)
        
        self.resultado = list(self.my_dict.keys())
        arquivo.close()

    # imprime a quantidade de possibilidades cadastradas
    def tamanho(self):
        print(len(self.resultado))

    # imprime a probabilidade do diagnótico
    probabilidade = lambda self: int ((1/int(len(self.resultado)))*100) if len(self.resultado) > 0 else 0

    # verifica se diagnóstico pensado tem a caracteristica passada por parametro
    busca = lambda self,r,s: True if self.my_dict.get(r).count(s) > 0 else False
        
        
    # remove os diagnósticos que não possuem o atributo passado por parametro
    def excluiquemnaoe(self, atributo):
        for r in self.resultado:
            if not self.busca(r, atributo):
                self.resultado.remove(r)
    
    # remove os diagnosticos que possuem o atributo passado por parametro
    def excluiqueme(self, atributo):
        for r in self.resultado:
            if self.busca(r, atributo):
                self.resultado.remove(r)
        
    def pergunta(self,pergunta,caract):
        print("Lista resultados: {}".format(self.resultado))
        resp = input(pergunta+'(s,n,p): ')
        if resp == 's' or resp == 'S':
            self.excluiquemnaoe(caract)
            self.excluiqueme("n_"+caract)
        elif resp == 'n' or resp == 'N':
            self.excluiqueme(caract)
            #self.excluiquemnaoe("n_"+caract) negação nem sempre está inclusa, então acho responsável comentar essa linha
        elif resp == 'p' or resp =='P':
            print("pergunta pulada")
    def get_sintomas(self,para):
        return self.my_dict.get(para)
"""
O seu Pet está agitado?'            ->        'agitado'
O seu Pet está comendo bem?'        ->        'alimentado'
'O ambiente é adequado?'            ->        'ambiente_adequado'
'O seu Pet fez atividade física?'     ->         'se_movimenta',        

"""
