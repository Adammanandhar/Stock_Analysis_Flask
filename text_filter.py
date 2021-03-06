import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob
import re
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class news_filter:
    def __init__(self):
        self.data=None
        self.clean_text=None
    def combine_text_data(self,data):
        extracted_paragraph = ' '.join([str(elem) for elem in data])
        self.data=extracted_paragraph
        return extracted_paragraph

    def clean_data(self,data, stemmer=PorterStemmer(), stop_words=set(stopwords.words('english'))):
        # Converts to lower case and splits up the word
        self.combine_text_data(data)
        words=word_tokenize(self.data.lower())
        filtered_words= []
        # comparing all the words that is extracted with the list of stop word ( like, to, is , etc)
        for word in words:
            if word not in stop_words and word.isalpha():
                filtered_words.append(stemmer.stem(word))

        filtered_string = ' '.join([str(elem) for elem in filtered_words])
        self.clean_text=filtered_string
        return filtered_string

    def getSubjectivity(self):
        return TextBlob(self.clean_text).sentiment.subjectivity
    def getPolarity(self):
        return TextBlob(self.clean_text).sentiment.polarity
    def getSIA(self):
        sia=SentimentIntensityAnalyzer()
        sentiment=sia.polarity_scores(self.clean_text)
        return sentiment
