import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from matplotlib import style

matches = pd.read_csv('MatchResults.csv') 

plt.subplots(figsize=(10,6))
ax = matches['MatchVenue'].value_counts().plot.bar(width=0.5, color='R') #color=["#999966", "#8585ad", "#c4ff4d", "#ffad33"])
ax.set_xlabel('Grounds')
ax.set_ylabel('Count')
plt.show()