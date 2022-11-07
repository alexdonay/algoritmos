class filaPriority:
    dados = []
    def __init__(self):
        self.dados = [{"prioridade":0, "valor":""}]
    
    def __str__(self):
        for i in range(len(self.dados)):
            print(f"{self.dados[i]['prioridade']} {self.dados[i]['valor']}")
    
    
# utilitários para manipulação de array
def insert(prioridade, dados):
    arr = filaPriority()
    arr.dados[0]["prioridade"] = prioridade
    arr.dados[0]["valor"] = dados
    arr.__str__()
    

insert(1, "Alex")