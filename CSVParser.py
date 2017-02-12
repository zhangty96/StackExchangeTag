import pandas as pd
import math as m
import numpy as np
import re

def y_cleaner(rawtext):
    #deals with weird things happening in the tags(y_train, y_test, y_valid), output a vector where each element is a sequence of strings
    y_output = []  # get the tags into list of list
    for y in rawtext:
        # print "========Type of y========="
        y = y[1:-1].split(',')
        # print y
        new_y = []

        for i in range(len(y)):
            word1 = " ".join(re.findall("[a-zA-Z]+", y[i]))
            new_y.append(word1)

        # print y[0]
        # print "expect y to be a list of strings", new_y
        y_output.append(new_y)
    return y_output


def parser(filepath):
    rawText = pd.read_csv(filepath)
    rawText = rawText.sample(frac=1)
    # change it to 65/15/20 for training/model selection/validation
    rawTraining = rawText[1:int(len(rawText)*0.65)]           #split data into 70% training
    rawTest = rawText[int(len(rawText)*0.65)-1:int(len(rawText)*0.8)]  # and 30% testing
    rawValid = rawText[int(len(rawText)*0.8)-81:len(rawText)]
    y_train = y_cleaner(rawTraining["tags"])                                            #get the tags into list of lists
    y_test = y_cleaner(rawTest["tags"])
    y_valid = y_cleaner(rawValid["tags"])
    # print y_test

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

    return np.array(y_train), np.array(y_test), np.array(y_valid), np.array(X_train), np.array(X_test), np.array(X_valid)

# [ y_train, y_test, y_valid, X_train, X_test, X_valid]=parser('./CleanData/cooking_light.csv')
# [ y_train, y_test, y_valid, X_train, X_test, X_valid]=parser('./CleanData/cooking_htmlclear.csv')
# print len(X_train)
# print len(y_train)
# print X_train[0]
# print y_train.shape

