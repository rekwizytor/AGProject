from PIL import Image
import random
import numpy as np
from invidual import Invidual
from crossover import crossover
from mutation import mutation

label = 'circle'
input_filename = 'circle.png'
out_filename = 'data_out.txt'
target_image = Image.open(input_filename).convert('RGB') 
#target_image = target_image.resize((600, 600))

size_of_invidual = 100
population_size = 50
generations = 100
p_mut = 0.2
size_of_mutation = 10
size_of_tournament = 5

population = [Invidual(width=target_image.width, height=target_image.height, invidual_size=size_of_invidual) for _ in range(population_size)]
for invidual in population:
    invidual.calculate_fitness(target_image)
population.sort(key=lambda x: x.fitness)

print(f'Generation: 0, the best fitness value: {population[0].fitness}.')

mean = [np.mean([invidual.fitness for invidual in population])]
std = [np.std([invidual.fitness for invidual in population])]

with open(f'{label}/{out_filename}', 'a') as f:
        f.write(f'{0}\t{population[0].fitness}\t{mean[0]}\t{std[0]}\n')

for generation in range(generations-1):


    new_population = []
    while len(new_population) < population_size:
        sub_population1 = random.sample(population, size_of_tournament)
        sub_population2 = random.sample(population, size_of_tournament)
        parent1 = sorted(sub_population1, key=lambda x: x.fitness)[0]
        parent2 = sorted(sub_population2, key=lambda x: x.fitness)[0]
        child1, child2 = crossover(parent1, parent2)
        new_population.append(child1)
        new_population.append(child2)
    
    for i, invidual in enumerate(new_population):
        if random.random() < p_mut:
            new_population[i] = mutation(invidual, size_of_mutation)

    for invidual in new_population:
        invidual.calculate_fitness(target_image)
    new_population.sort(key=lambda x: x.fitness)
    print(f'Generation: {generation+1}, the best fitness value: {population[0].fitness}.')

    new_population[0].draw().save(f'{label}/the_bests/{generation}.png')
    new_population[-1].draw().save(f'{label}/the_worsts/{generation}.png')
    mean.append(np.mean([invidual.fitness for invidual in new_population]))
    std.append(np.std([invidual.fitness for invidual in new_population]))

    with open(f'{label}/{out_filename}', 'a') as f:
        f.write(f'{generation+1}\t{new_population[0].fitness}\t{mean[generation+1]}\t{std[generation+1]}\n')

    population = new_population

for i, invidual in enumerate(population):
    invidual.draw().save(f'{label}/last_population/{i}.png')

population[0].draw().save(f'{label}/best.png')
