import os
import sys
import operator
import re
import nltk
from nltk.stem.wordnet import WordNetLemmatizer

lmtzr = WordNetLemmatizer()

class ArgumentError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def word_freq(text):
    text = re.sub(r'[^A-Za-z0-9 ]', '', text)
    words = text.split()
    freq = {}
    for word in words:
        word = word.lower()
        word = lmtzr.lemmatize(word)
        if word in freq.keys():
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def word_filter(freq_list, threshold):
    freq = dict((k,v) for k, v in freq_list.items() if v >= threshold)
    return freq

def filter_stop_words(freq):
    f = open(os.path.join(os.path.dirname(__file__),'stop_words.txt'))
    raw = f.read()
    stop_words = raw.split()
    filtered = []
    words = freq.keys()
    freqn = freq.copy()
    for word in words:
        if word in stop_words:
            freqn.pop(word, None)
    return freqn


def count_words(text):
    freq = filter_stop_words(word_filter(word_freq(text), 2))
    freq_sorted = sorted(freq.items(), key=operator.itemgetter(1))
    return freq_sorted