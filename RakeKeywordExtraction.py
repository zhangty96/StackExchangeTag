# Keyword Extraction using RAKE
# TODO: consider using Maui

from CSVParser import parser
import rake
import operator
# Available at: https://www.airpair.com/nlp/keyword-extraction-tutorial

stoppath = "SmartStoplist.txt"

# parse csv file
[ y_train, y_test, y_valid, X_train, X_test, X_valid]=parser('./CleanData/cooking_htmlclear.csv')
text = X_train[1]

# Each word has at least 5 characters, each phrase has at most 3 words
rake_object = rake.Rake(stoppath,3,2,1)

# Splits the text into sentences
sentenceList = rake.split_sentences(text)
stopwordpattern = rake.build_stop_word_regex(stoppath)

# Generate Candidates
phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern)

wordscores = rake.calculate_word_scores(phraseList)
keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)

sortedKeywords = sorted(keywordcandidates.iteritems(), key=operator.itemgetter(1), reverse=True)
totalKeywords = len(sortedKeywords)

# Compare
print "Text: ", text
print "Tag: ",y_train[1]
print "Candidate Keywords: ",phraseList

for keyword in sortedKeywords[0:(totalKeywords / 3)]:
    print "Keyword: ", keyword[0], ", score: ", keyword[1]