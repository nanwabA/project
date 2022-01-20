import random
import plotly.express as px
diceResult=[]
count=[]
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceResult.append(dice1+dice2)
    count.append(i)
fig=px.bar(
    x=diceResult,
    y=count
    )    
fig.show()    
    