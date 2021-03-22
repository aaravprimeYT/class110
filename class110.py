import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("class110.csv")

tempList = df["temp"].tolist()

fig = ff.create_distplot([tempList],["Temperature"],show_hist = False)
fig.show()

def randomSetOfMeans(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(tempList)-1)
        value = tempList[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

def showFig(meanList):
    df = meanList
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["Temperature"],show_hist=False)
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0,1],mode = "lines",name = "mean"))
    fig.show()

def main():
    meanList = []
    for i in range(0,1000):
        setOfMeans = randomSetOfMeans(100)
        meanList.append(setOfMeans)
    showFig(meanList)
    mean = statistics.mean(meanList)
    deviation2 = statistics.stdev(meanList)
    print(deviation2)
    print(mean)

deviation = statistics.stdev(tempList)
print(deviation)

populationMean = statistics.mean(tempList)
print (populationMean)

main()