import pandas as pd
import math as m


def parser(filepath):
    rawText = pd.read_csv(filepath)
    rawText = rawText.sample(frac=1)
    rawTraining = rawText[1:int(len(rawText)*0.7)]           #split data into 70% training
    rawTest = rawText[int(len(rawText)*0.7)-1:len(rawText)]  # and 30% testing
    y_train = list(rawTraining['tags'])
    y_test = list(rawTest['tags'])

    #for training X
    title = list(rawTraining['title'])
    print len(title), "title length"
    content = list(rawTraining['content'])
    print len(content), "content length"
    X_train = list()
    # now to combine the two content and title column
    for index in range(len(title)):
        X_train = X_train.append(title[index]+content[index])


    # for testing X
    title = list(rawTest['title'])
    content = list(rawTest['content'])
    X_test = list()
    # now to combine the two content and title column
    for index in range(len(title)):
        X_test[index] = X_test.append(title[index]+content[index])

    return y_train, y_test, X_train, X_test

[y_train, y_test, X_train, X_test]=parser('./CleanData/cooking_light.csv')
print y_train

