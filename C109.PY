import random
import plotly.express as px
import statistics

diceResult=[]
count=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceResult.append(dice1+dice2)

mean=sum (diceResult)/len(diceResult)    
mode=statistics.mode(diceResult)
median=statistics.median(diceResult)

std_deviation=statistics.stdev(diceResult)

print(mean)
print(mode)
print(median)
print(std_deviation)