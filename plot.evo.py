import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'ieee'])


# data
x = [ temp for temp in range(1, 51) for times in range(100)]
y = [np.loadtxt('pso_sor_%d'%(t)).tolist() for t in range(1, 51)]
yy = [i for ii in y for i in ii]

# colormap
cm = plt.cm.get_cmap('rainbow')

# fig, ax
fig, ax = plt.subplots(figsize=(10, 4))

# ax.scatter(x, yy, c=yy, cmap=cm, vmin=2.3, vmax=2.6, s=5)
sc = ax.scatter(x, yy, c=yy, cmap=cm, vmin=-3.6, vmax=-3.2, s=10)

# beauty
ax.set_xlabel('Structure Evolution Step', fontsize=25, )
ax.set_ylabel('Energy (eV/atom)', fontsize=25, )
ax.set_xticks([0, 10, 20, 30, 40, 50],)
ax.set_yticks([-3.6, -3.5, -3.4, -3.3, -3.2],)
# ax.tick_params(width=5, labelsize=10)
ax.set_ylim((-3.6, -3.2))

plt.tick_params(labelsize=20)

# colorbar
cbar = fig.colorbar(sc)
cbar.set_ticks(ticks=[-3.6, -3.5, -3.4, -3.3, -3.2])
cbar.ax.tick_params(labelsize=20)
cbar.ax.minorticks_off()
cbar.outline.set_visible(False)


# spines width
width = 2
ca = plt.gca()

ca.spines['bottom'].set_linewidth(width)
ca.spines['left'].set_linewidth(width)
ca.spines['top'].set_linewidth(width)
ca.spines['right'].set_linewidth(width)

plt.tight_layout()

fig.savefig('evo.png', dpi=350)
