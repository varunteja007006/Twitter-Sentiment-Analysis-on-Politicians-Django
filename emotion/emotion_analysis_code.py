import pandas as pd
import numpy as np
import nltk
import re
import pickle
import itertools
from nltk.stem.wordnet import WordNetLemmatizer 
from django.conf import settings
import os
import string
from collections import Counter
#import matplotlib.pyplot as plt

class emotion_analysis_code():

    def predict_emotion(self, tweet):

        text = tweet
        lower_case_text=text.lower()
        cleaned_text= lower_case_text.translate(str.maketrans('','',string.punctuation))
        #print(cleaned_text)

        '''
        str1 = specifies the list of chars that need to be replaced
        str2 = specifies the list of chars with which the chars need to be replaced
        str3 = specifies the list of chars that need to be deleted
        '''

        tokenized_words = cleaned_text.split()

        stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                      "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                      "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
                      "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
                      "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                      "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                      "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
                      "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
                      "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
                      "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

        final_words= []
        for word in tokenized_words:
            if word not in stop_words:
                final_words.append(word)
        #print(final_words)

        '''
        1. Check if word in final_words is present in emotions.txt
        _Loop through each line and clear it
        _Extract the word and emotion using split
        2. if word present >> add emotion to Emotion List
        3. Finally count each emotion  in Emotion List
        '''

        '''
        NOTE: In order to have better results emotions like love, hate, happiness, sadness, worry should only be 
        given as emotions to the words. Therefore it is necessaary to edit the emotions.txt file. 

        '''
        emotion_list=[]
        with open('emotion/emotions.txt','r') as emotion_file:
            for line in emotion_file:
                clear_line = line.replace('\n','').replace(',','').replace("'","").strip()
                word,emotion =clear_line.split(':')
                #print(word,emotion)
                if word in final_words:
                    #print(word)
                    emotion_list.append(emotion)

        return emotion_list[0]
      
        #w=Counter(emotion_list)
        #return w
'''
        predicted_sentiment = model.predict(test)
        final_sentiment = (predicted_sentiment[0])
        if final_sentiment == 'worry':
            return 'Worry'
        elif final_sentiment == 'sadness':
            return 'Sadness'
        elif final_sentiment == 'happiness':
            return 'Happiness'
        elif final_sentiment == 'love':
            return 'Love'
        elif final_sentiment == 'hate':
            return 'Hate'
            

if __name__ == "__main__":
    tweet = 'Layin n bed with a headache ughhhh...waitin for you call my loved one...'
    eac=emotion_analysis_code()
    x=eac.predict_emotion(tweet)
'''
