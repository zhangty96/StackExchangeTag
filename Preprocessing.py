# -*- coding: utf-8 -*-

# Data Loading and Preprocessing
# 1. Removing html tags and URL formatting
# 2. Removing punctuation and lower-casing
# 3. Removing stopwords
# 4. Convert tags to list of tags
# Credit to: MatteoTosi


import pandas as pd
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import nltk
import re
import string
import os


def stripTagsAndUris(x):
    url_re = r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))'

    if x:
        # BeautifulSoup on content
        soup = BeautifulSoup(x, "html.parser")
        # Stripping all <code> tags with their content if any
        if soup.code:
            soup.code.decompose()
        # Get all the text out of the html
        text =  soup.get_text()
        # Returning text stripping out all uris
        return re.sub(url_re, "", text)
    else:
        return ""


def removePunctuation(x):
    # Lowercasing all words
    x = x.lower()
    # Removing non ASCII chars
    x = re.sub(r'[^\x00-\x7f]',r' ',x)
    # Removing (replacing with empty spaces actually) all the punctuations
    return re.sub("["+string.punctuation+"]", " ", x)


def removeStopwords(x):
    stops = set(stopwords.words("english"))
    # Removing all the stopwords
    filtered_words = [word for word in x.split() if word not in stops]
    return " ".join(filtered_words)


def preprocess():
    path = os.path.join(os.getcwd(), "Data");

    # loading .csv files
    dataframes = {
        "cooking": pd.read_csv(path + "/cooking.csv"),
        "crypto": pd.read_csv(path + "/crypto.csv"),
        "robotics": pd.read_csv(path + "/robotics.csv"),
        # "biology": pd.read_csv(path + "/biology.csv"),
        # "travel": pd.read_csv(path + "/travel.csv"),
        # "diy": pd.read_csv(path + "/diy.csv"),
    }

    # print dataframes["cooking"].iloc[100]

    for df in dataframes.values():
        df["content"] = df["content"].map(stripTagsAndUris)


    for df in dataframes.values():
        df["title"] = df["title"].map(removePunctuation)
        df["content"] = df["content"].map(removePunctuation)


    for df in dataframes.values():
        df["title"] = df["title"].map(removeStopwords)
        df["content"] = df["content"].map(removeStopwords)

    for df in dataframes.values():
        # From a string sequence of tags to a list of tags
        df["tags"] = df["tags"].map(lambda x: x.split())

    for name, df in dataframes.items():
        # Saving to file
        df.to_csv(name + "_light.csv", index=False)



preprocess()