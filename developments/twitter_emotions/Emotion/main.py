'''
1. cleaning text file, take text from there
2. converts letters to lower case
3. remove punctuations
'''
import string
from collections import Counter
import matplotlib.pyplot as plt

text = open('read.txt', encoding='utf-8').read()
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

emotion_list=[]
with open('emotions.txt','r') as emotion_file:
    for line in emotion_file:
        clear_line = line.replace('\n','').replace(',','').replace("'","").strip()
        word,emotion =clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w=Counter(emotion_list)
print(w)
'''
fig,ax1 =plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
'''

''' 
GetOldTweets3 similar to twitter api but a bit more easy to access.
GetOldTweets3 is package need to be installed
'''