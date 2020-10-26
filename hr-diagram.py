import math
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.cm import get_cmap
from matplotlib.colors import LogNorm
cmap = get_cmap('inferno')

data = pd.read_csv('1603729801595O-result.csv')
bp_rp = data['bp_rp']
mg = data['mg']

fig, ax = plt.subplots(figsize=(12, 12))
h=ax.hist2d(bp_rp, mg, bins = 300,  
          norm = colors.LogNorm(), 
          cmap ="Reds") 
ax.scatter(bp_rp, mg, alpha=0.5, s=10, color='red', zorder=0)

plt.gca().invert_yaxis()

cb = fig.colorbar(h[3], ax=ax, pad=0.02)
plt.title('Colour Magnitude Diagram of 900000 stars' , fontsize=18)
plt.xlabel(r'$G_{BP} - G_{RP}$' , fontsize=14)
plt.ylabel(r'$M_G$' , fontsize=14)
cb.set_label(r"$\mathrm{Stellar~density}$" , fontsize=14)           

plt.savefig("hr-diagram.jpg", dpi=400)

plt.show()
