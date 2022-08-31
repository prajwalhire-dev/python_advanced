#pip install textblob -- > install the textblob module
from textblob import TextBlob 

words = input('Enter the wrong words : ')
words = words.split(',') # converts the string into list
print(words)  #like this --- > words = ['Data Scence', 'Machine Learnin']
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("Wrong words: ", words)
print("Correct words : ",)
for i in corrected_words:
    print(i.correct(), end = ' ')
