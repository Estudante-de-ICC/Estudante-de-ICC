import random
import copy

id = 0

tab = [["#", "#", "#", "#", "#", "#", "#", "#"], 
      ["#", "#", "#", "#", "#", "#", "#", "#"], 
      ["#" ,"#", "#", "#", "#", "#", "#", "#"], 
      ["#", "#", "#", "#", "#", "#", "#", "#"],
      ["#", "#", "#", "#", "#", "#", "#", "#"],
      ["#", "#", "#", "#", "#", "#", "#", "#"],
      ["#", "#", "#", "#", "#", "#", "#", "#"],
      ["#", "#", "#", "#", "#", "#", "#", "#"]]

def ger_random():
    ind = []
    for i in range(0,8):
        i = random.randint(1,8)
        ind.append(i)
    return ind

class indv: 
    def __init__(self, ind):
        self.ind = ind
        global id
        self.id = id
        id += 1
        self.fitness = self.atk()
    
    def atk(self):
        explorados = []
        total = 0
        for i in range (0, len(self.ind) - 1):
            for j in range(i+1, len(self.ind)):
                if self.ind[i] != self.ind[j] and not(((self.ind[i], self.ind[j])  in explorados) or ((self.ind[j], self.ind[i])  in explorados)):
                    if not(abs(i - j) == abs(self.ind[i] - self.ind[j])):
                        total += 1
                        explorados.append((self.ind[i],self.ind[j]))
        return total
    
    def mutar(self): 
        gen_mut = random.randint(1, 8)
        for i in range(1, gen_mut):
            gene = random.randint(0,7)
            mudanca = random.randint(1,8)
            self.ind[gene] = mudanca
            self.fitness  = self.atk()

class pop: 
    def __init__(self, tam, gerat):
        self.tam = tam
        self.gerat = gerat
        self.ger = []
        self.prob = []
        self.soma = 0
    
    def GPI(self): 
        for i in range(self.tam):
            ind = indv(ger_random())
            self.soma += ind.fitness
            self.ger.append(ind)

    def MFNE(self):
        N_achou = True
        for i in self.ger:
            if i.fitness == 28:
                N_achou = False
                return N_achou
        return N_achou

    def MI(self): 
        for i in self.ger: 
            maior = self.ger[0].fitness
            index = 0
            for i in range(len(self.ger)):
                if maior < self.ger[i].fitness:
                    maior = self.ger[i].fitness
                    index =  i
            return (self.ger[index])

    def sel_pai(self):
        for i in self.ger:
            self.prob.append((i.fitness/self.soma))
        x = random.choices(self.ger, self.prob, k = 1)
        self.prob.clear()
        return x[0]

    def add_P(self, k):
        self.ger.append(k)
        self.soma += k.fitness

    def melhores(self):
        self.ger.sort(key= lambda x: x.fitness)
        i = 0
        while (len(self.ger) > int(self.tam)):
            self.soma -= self.ger[i].fitness
            self.ger.pop(i)

def reproduzir(x, y):

    v = random.randint(0, 8)
    filho1 = []
    filho2 = []
    for i in range(0, 8 ):
        if i < v:
            filho1.append(x.ind[i])
            filho2.append(y.ind[i])
        else:
            filho1.append(y.ind[i])
            filho2.append(x.ind[i])
    return indv(filho1), indv(filho2)

def adicionar_p(Pop1, Pop2):
    for i in Pop2.ger:
        Pop1.ger.append(i)
        Pop1.soma += i.fitness

def GA(TP, IT, MUT):
    geracao = 1
    Populacao = pop(TP, geracao)
    Populacao.GPI()
    while (geracao < IT) and Populacao.MFNE():
        N_Populacao = pop(TP, geracao)
        for i in range(1, TP+1):
            pai1 = Populacao.sel_pai()
            pai2 = Populacao.sel_pai()
            filho1, filho2 = reproduzir(pai1, pai2)
            m = float(random.randint(0, 100))
            if m <= MUT: 
                filho1.mutar()
            m = float(random.randint(0, 100))
            if m <= MUT:
                filho2.mutar()
            N_Populacao.add_P(filho1)
            N_Populacao.add_P(filho2)
        adicionar_p(Populacao, N_Populacao)
        Populacao.melhores()
        geracao += 1
        Populacao.gerat = geracao
    print(f"Geração {Populacao.gerat}")
    Melhor = Populacao.MI()
    print(f"Individuo {Melhor.ind} com Fitness de {Melhor.fitness} \nID: {Melhor.id} :D")
    #print(f"----------------------------------------------------------------------------")

    for i in range(0, 8):
        tabuleiro [Melhor.ind [i] - 1] [i] = "Q"
    for i in range(0, 9):
        if(i < 8):
            print(f"Linha {i+1}: ", end = '')
        for j in range(0, 8):
            if (i < 8 and j < 8):
                print(tabuleiro[i][j] + "  ", end = '')
            else:
                if (i >= 8):
                    if (j == 0 and j < 8):
                        print("         ", end = '')
                    print(f"{j+1}" + "  ", end = '')
        print()

if __name__ == "__main__":
    for i in range(0, 10):
        tabuleiro = copy.deepcopy(tab)
        GA(150, 100, float(20))
        id = 0
        print(f"----------------------------------------------------------------------------")
        tabuleiro.pop()

        #Caso 150 - 100 - 20% -> Resultado - O algoritmo encontrou 3 respostas
        #Caso 200 - 100 - 20% -> Resultado - O algoritmo encontrou 5 respostas
