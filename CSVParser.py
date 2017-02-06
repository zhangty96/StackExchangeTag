import pandas as pd
import math as m


def parser(filepath):
    rawText = pd.read_csv(filepath)
    rawText = rawText.sample(frac=1)
    # change it to 65/15/20 for training/model selection/validation
    rawTraining = rawText[1:int(len(rawText)*0.65)]           #split data into 70% training
    rawTest = rawText[int(len(rawText)*0.65)-1:int(len(rawText)*0.8)]  # and 30% testing
    rawValid = rawText[int(len(rawText)*0.8)-81:len(rawText)]
    y_train = []                                            #get the tags into list of list
    for y in rawTraining["tags"]:
        y_train.append(y)
    y_test = []
    for y in rawTest["tags"]:
        y_test.append(y)
    y_valid =[]
    for y in rawValid["tags"]:
        y_valid.append(y)

    #for training X
    title = list(rawTraining['title'])
    content = list(rawTraining['content'])
    # print(title[1]+content[1]), 'testing if add works'
    X_train = []
    # now to combine the two content and title column
    for index in range(len(title)):
        X_train.append(title[index]+" " +content[index])


    # for testing X
    title = list(rawTest['title'])
    content = list(rawTest['content'])
    X_test = []
    # now to combine the two content and title column
    for index in range(len(title)):
        X_test.append(title[index]+" " +content[index])

    # for testing X
    title = list(rawValid['title'])
    content = list(rawValid['content'])
    X_valid = []
    # now to combine the two content and title column
    for index in range(len(title)):
        X_valid.append(title[index]+" " +content[index])

    return y_train, y_test, y_valid, X_train, X_test, X_valid

# [ y_train, y_test, y_valid, X_train, X_test, X_valid]=parser('./CleanData/cooking_light.csv')
# print y_train[4]

