import numpy as np
import pandas as pd

df1 = pd.read_csv('PlayerLeaderBoard.csv')
df2 = df1.set_index("Metric")

plb1 = df2.iloc[:112,-1].mean()  #SuccessfulRaids for Season1
plb2 = df2.iloc[112:260,-1].mean() #SuccessfulRaids for Season2
plb3 = df2.iloc[260:403,-1].mean() #SuccessfulRaids for Season3
plb4 = df2.iloc[403:525,-1].mean() #SuccessfulRaids for Season4

print("Average SuccessfulRaids for Season1: ",plb1)
print("Average SuccessfulRaids for Season2: ",plb2)
print("Average SuccessfulRaids for Season3: ",plb3)
print("Average SuccessfulRaids for Season4: ",plb4)