
# Sample Code to perform multi-labeling on small data set
# Toy Data Example Availability: http://stackoverflow.com/questions/10526579/use-scikit-learn-to-classify-into-multiple-categories


import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.naive_bayes import MultinomialNB as MNB
from sklearn.naive_bayes import BernoulliNB as BNB
from CSVParser import parser

# X_train = np.array(["new york is a hell of a town",
#                     "new york was originally dutch",
#                     "the big apple is great",
#                     "new york is also called the big apple",
#                     "nyc is nice",
#                     "people abbreviate new york city as nyc",
#                     "the capital of great britain is london",
#                     "london is in the uk",
#                     "london is in england",
#                     "london is in great britain",
#                     "it rains a lot in london",
#                     "london hosts the british museum",
#                     "new york is great and so is london",
#                     "i like london better than new york"])


[y_train, y_test, y_valid, X_train, X_test, X_valid]=parser('./CleanData/cooking_light.csv')
[y_train, y_test, y_valid, X_train, X_test, X_valid] = [y_train[:165], y_test[:20], y_valid[:15], X_train[:165], X_test[:20], X_valid[15]]

# Multilabel Binarizer
mlb = MultiLabelBinarizer()
print "===========y_train=============="
print y_train
print type(y_train[0])
# print y_train[1]
# print y_train[2]
# y_train = [['New York'],['New York'],['New York'],['New York'],['New York'],['New York'],['London'],['London'], ['London'],['London'],['London'],['London'],['New York', 'London'],['New York', 'London'] ]
y_train = mlb.fit_transform(y_train)
# print y_train
print "classes",list(mlb.classes_)
# print "-----Binarize y_train----------"
# print y_train


# Pipeline(vectorization, tfid weighting and classifier)
ppl = Pipeline([
    ('vectorizer', HashingVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', OneVsRestClassifier(LinearSVC()))])



ppl.fit(X_train, y_train)


# # Test
# X_test = np.array(['nice day in nyc',
#                    'welcome to london',
#                    'hello welcome to new york. enjoy it here and london too'])
# target_names = ['New York', 'London']     # index--> names
y_predict = ppl.predict(X_test)
labels_predicted = mlb.inverse_transform(y_predict)
print labels_predicted
# print "\tInverting binary encoding......"
# print "=============y_predicted============"
# print labels_predicted


for item, labels in zip(X_test, labels_predicted):
    print '%s => %s' % (item, ', '.join(x for x in labels))
