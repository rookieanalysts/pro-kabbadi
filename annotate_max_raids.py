import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from matplotlib import style

plb = pd.read_csv('PlayerLeaderBoard.csv')

plt.subplots(figsize=(11,6))
max_raids=plb.groupby(['Name'])['Value'].sum()
ax=max_raids.sort_values(ascending=False)[:10].plot.bar(width=0.8,color='R')
for p in ax.patches:
    ax.annotate(format(p.get_height()), (p.get_x()+0.1, p.get_height()+1),fontsize=11)
plt.show()