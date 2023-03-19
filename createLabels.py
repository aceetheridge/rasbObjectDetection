import re
import pandas

def createLabels(path):
    columns = ['id', 'name', 'part', 'count']
    labels = {}
    csv = pandas.read_csv(path, header=0,usecols=columns)
    for index, row in csv.iterrows():
        labels[index] = csv['name'][index]
    # print(labels)
    return labels