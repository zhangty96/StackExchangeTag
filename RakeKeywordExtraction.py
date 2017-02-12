# Keyword Extraction using RAKE
# TODO: consider using Maui
from CSVParser import parser
import rake
import operator
# Available at: https://www.airpair.com/nlp/keyword-extraction-tutorial




def RakeExtract(text, stoppath = "SmartStoplist.txt"):
    """
    :param text: string type
    :param stoppath:  stopword list
    :return:    a list of tuples where the 1st index is the keyword and the second index the score
    """

    # Each word has at least 5 characters, each phrase has at most 3 words
    rake_object = rake.Rake(stoppath, 3, 2, 1)

    # Splits the text into sentences
    sentenceList = rake.split_sentences(text)
    stopwordpattern = rake.build_stop_word_regex(stoppath)

    # Generate Candidates
    phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern)
    # print "Candidate Keywords: ", phraseList

    wordscores = rake.calculate_word_scores(phraseList)
    keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)

    sortedKeywords = sorted(keywordcandidates.iteritems(), key=operator.itemgetter(1), reverse=True)
    totalKeywords = len(sortedKeywords)
    keywords = sortedKeywords[0:(totalKeywords / 3)]

    return keywords




def Extract():
    [y_train, y_test, y_valid, X_train, X_test, X_valid] = parser('./CleanData/cooking_htmlclear.csv')

    n = len(X_train)
    text_file = open("RakeCookingOutput.txt", "w")



    for i in range(n/2):
        text_file.write("=====blurb %d=====" %(i+1))
        text_file.write("\n")
        text_file.write("Text: %s" %X_train[i])
        text_file.write("\n")
        text_file.write("Tag: %s" %str(y_train[i]))
        text_file.write("\n")



        # print "=====blurb %d=====" %i
        # print "Text: ", X_train[i]
        # print "Tag: ",y_train[i]
        # print "\n"
        keywords = RakeExtract(X_train[i])
        for keyword in keywords:
            print "Keyword: ", keyword[0], ", score: ", keyword[1]
            text_file.write("Keyword: %s" % keyword[0])
            text_file.write("\t\t , score: %s" % str(keyword[1]))
            text_file.write("\n")

        text_file.write("\n")
        text_file.write("\n")


    text_file.close()

Extract()