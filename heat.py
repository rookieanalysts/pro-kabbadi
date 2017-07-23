import pandas as pd
import quandl
import matplotlib.pyplot as plt
import seaborn as sns
import math

pd=pd.read_csv('TeamLeaderBoard.csv')

#Replacing the Team Names with their abbreviations

pd.replace(['Bengal Warriors','Bengaluru Bulls','Dabang Delhi K.C.','Jaipur Pink Panthers','Patna Pirates',
                 'Puneri Paltan','Telugu Titans','U Mumba']
                ,['BW','BB','DD','JPP','PTP','PP','TT','UM'],inplace=True)

plt.subplots(figsize=(11,11))
max_players=pd.groupby('Name')['Name'].count()
max_players.sort_values(ascending=True,inplace=True)
mean_pd=pd[pd['Name'].isin(max_players.index)]
abc=mean_pd.groupby(['SeasonId','Name'])['Value'].mean().reset_index()
abc=abc.pivot('SeasonId','Name','Value')/1.6
sns.heatmap(abc,annot=True,cmap='RdYlGn',linewidths=0.4)
plt.title('Average Score By Players') #Title of graph
plt.show()