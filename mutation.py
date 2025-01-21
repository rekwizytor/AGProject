import random

def mutation(invidual, number=4):
    mut_invidual = invidual.copy()
    indexes = random.sample(range(len(mut_invidual.shapes)), number)

    for index in sorted(indexes, reverse=True):
        del mut_invidual.shapes[index]

    for _ in range(number):
        mut_invidual.shapes.append(mut_invidual.generate_random_shape())
        
    return mut_invidual
