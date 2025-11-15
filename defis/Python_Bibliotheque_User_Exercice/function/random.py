import random

def choix_alea() :
    nbChoix = random.randrange(1, 101, 2)
    print(f'Le nombre aléatoire choisie entre 1 et 101 est {nbChoix}')
