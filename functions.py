from random import getrandbits, randint, random, choice



def individual():
    """Cria um membro da populacao"""
    return [ getrandbits(1) for x in range(3) ]

def population(tamanho_populacao):
	return [ individual() for x in range(tamanho_populacao) ]

def fitness(individuo):
    valor = ''
    for indice, binario in enumerate(rgb):
        valor += String(binario)
    return int(valor, 2)


def seleção():
def crossover():
def mutation():

