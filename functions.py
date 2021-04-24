from random import getrandbits, randint, random, choice
from matplotlib import pyplot as plt

rgb= [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1] ]


def individual():
    """Cria um membro da populacao"""
    return [ getrandbits(1) for x in range(3) ]

def population(tamanho_populacao):
	return [ individual() for x in range(tamanho_populacao) ]

def fitness(individuo):
    valor = ''
    for indice, binario in enumerate(individuo):
        valor += str(binario)
    return int(valor, 2)

def grandeTorneio(parents):
    torneio = int(randint(0,99))
    valor = int(parents[torneio][0])
    aleatorio = randint(0, 10)
    if valor >= aleatorio:
        return parents[torneio]
    return grandeTorneio(parents)

def reproduz(selecionados):    
    filhos = []
    while(len(filhos) < len(selecionados)):
        indice = int(randint(0,99))
        cromossomos = int(randint(0,2))
        pai = selecionados[indice][1] 
        mae = selecionados[indice-1][1] 
        filho = pai[:cromossomos] + mae[cromossomos:]
        filho = mutation(filho)
        filhos.append(filho)
    return filhos

def mutation(filho, mutate = 0.01):
    cromossomo = int(randint(0,2))
    if mutate > random():
        if filho[cromossomo] == 1:
            filho[cromossomo] = 0
            return filho
        else:
            filho[cromossomo] = 1
            return filho
    else:
        return filho
        

def geracoesBesourais(populacao):
    historico = []
    cores = [['black',0], ['blue',0], ['green',0], ['light blue',0], ['red',0], ['purple',0], ['yellow',0], ['white',0]]
    for especime in populacao:
        cores[especime[0]][1] += 1
    for x in range(8):
        historico.append(cores[x][1])
    return historico

    
def grafico(Darwin):
    plt.style.use('bmh')
    black = []
    blue = []
    green = []
    lightBlue = []
    red = []
    purple = []
    yellow = []
    white = []
    generations = []
    for x in range(len(Darwin)):
        generations.append(x)
    for x in Darwin:
        black.append(x[0])
    for x in Darwin:
        blue.append(x[1])
    for x in Darwin:
        green.append(x[2])
    for x in Darwin:
        lightBlue.append(x[3])
    for x in Darwin:
        red.append(x[4])
    for x in Darwin:
        purple.append(x[5])
    for x in Darwin:
        yellow.append(x[6])
    for x in Darwin:
        white.append(x[7])
        
    plt.plot(generations, black,color = '#000000',label="Black")
    plt.plot(generations, blue,color = '#21618C',label="Blue")
    plt.plot(generations, green,color='#28B463',label="green")
    plt.plot(generations, lightBlue,color='#85C1E9',label="lightBlue")
    plt.plot(generations, red,color='#CB4335',label="red")
    plt.plot(generations, purple,color='#8E44AD',label="purple")
    plt.plot(generations, yellow,color='#F7DC6F',label="yellow")
    plt.plot(generations, white,color = '#FDFEFE',label="white")

    plt.ylabel('Tamanho População')
    plt.xlabel('Gerações')
    plt.title("Gerações de Besouros")

    
    plt.legend()
    plt.show()

    
n_geracoes = 100
populacao = population(100)

def evolucao(populacao, n_geracoes, geracoes):
    if(n_geracoes > 0):
        parents = [[fitness(individuo),individuo]for individuo in populacao]
        geracoes += [geracoesBesourais(parents)]
        selecionados = [grandeTorneio(parents) for _ in range(len(parents))]
        filhos = reproduz(selecionados)
        return evolucao(filhos, n_geracoes-1,geracoes)
    else:
        return geracoes


geracoes = []
Darwin = evolucao(populacao, n_geracoes, geracoes)
grafico(Darwin)
