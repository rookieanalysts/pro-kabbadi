import pandas as games
import quandl
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

plt.subplots(figsize=(15,15))
games=games.read_csv('TeamLeaderBoard.csv')
max_genres=games.groupby('Name')['Name'].count()
max_genres.sort_values(ascending=True,inplace=True)
mean_games=games[games['Name'].isin(max_genres.index)]
abc=mean_games.groupby(['SeasonId','Name'])['Value'].mean().reset_index()
abc=abc.pivot('SeasonId','Name','Value')
sns.heatmap(abc,annot=True,cmap='RdYlGn',linewidths=0.4)
plt.title('Average Score By Genre"s')
plt.show()