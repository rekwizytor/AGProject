import random

def crossover(parent1, parent2):
    child1 = parent1.copy()
    child2 = parent2.copy()
    number = random.randint(1, len(parent1.shapes)-1)
    child1.shapes = parent1.shapes[:number] + parent2.shapes[number:]
    child2.shapes = parent2.shapes[:number] + parent1.shapes[number:]
    return child1, child2
