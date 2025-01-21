import matplotlib.pyplot as plt
import numpy as np

label = 'circle'
input_filename = 'data_out.txt'
data = np.loadtxt(f'{label}/{input_filename}')

generation = data[:, 0]
best_fitness = data[:, 1]
mean = data[:, 2]
std = data[:, 3]

plt.figure(figsize=(6, 6))
plt.scatter(generation, best_fitness, s=60, marker='o', edgecolors='black', zorder=2)
plt.plot(generation, best_fitness, color='black', zorder=1)
plt.tick_params(axis='both', direction='in')
ax = plt.gca()
ax.ticklabel_format(style='scientific', axis='y', scilimits=(-4, 4))
ax.yaxis.offsetText.set_fontsize(11)
plt.xticks(size='11')
plt.yticks(size='11')
plt.xlabel('Generation', size=13)
plt.ylabel('Fitness', size=13)
plt.title('The best fitness in generation', size=13)
plt.tight_layout()
plt.savefig(f'{label}/best_graf.png', dpi=300)

plt.figure(figsize=(6, 6))
plt.scatter(generation, mean, s=60, marker='o', edgecolors='black', label='Mean', zorder=2)
plt.plot(generation, mean, color='black', zorder=1)
plt.fill_between(generation, [m - s for m, s in zip(mean, std)], [m + s for m, s in zip(mean, std)], color='#1f77b4', alpha=0.2, label='Std')
plt.tick_params(axis='both', direction='in')
ax = plt.gca()
ax.ticklabel_format(style='scientific', axis='y', scilimits=(-4, 4))
ax.yaxis.offsetText.set_fontsize(11)
plt.xticks(size='11')
plt.yticks(size='11')
plt.xlabel('Generation', size=13)
plt.ylabel('Fitness', size=13)
plt.title('Average fitness in generation', size=13)
plt.tight_layout()
plt.savefig(f'{label}/mean_graf.png', dpi=300)