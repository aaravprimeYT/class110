import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import random
import statistics

df = pd.read_csv("class110-2.csv")

avgList = df["average"].tolist()

def randomSetOfMeans(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(avgList)-1)
        value = avgList[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

def showFig(meanList):
    df = meanList
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["Averages"],show_hist=False)
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0,12],mode = "lines",name = "mean"))
    fig.show()

def main():
    meanList = []
    for i in range(0,1000):
        setOfMeans = randomSetOfMeans(100)
        meanList.append(setOfMeans)
    showFig(meanList)
    mean = statistics.mean(meanList)
    deviation = statistics.stdev(meanList)
    print(deviation)
    print(mean)

deviation2 = statistics.stdev(avgList)
print(deviation2)

populationMean = statistics.mean(avgList)
print(populationMean)

main()