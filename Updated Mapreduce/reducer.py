from operator import itemgetter
import sys
from collections import Counter

current_word = None
current_count = 0
word = None
word_list = []
wordcount={}

for line in sys.stdin:
    line = line.strip()

    word, count = line.split('\t', 1)
    word_list.append(word)
for word in word_list:
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    print k, v

print("--"*100)
filtered_sentence = []
stop_words = ["all","the","a"]
for w in word_list:
    if w not in stop_words:
        filtered_sentence.append(w)



print("--"*100)

wordcount_filtered={}

for word1 in filtered_sentence:
    if word1 not in wordcount_filtered:
        wordcount_filtered[word1] = 1
    else:
        wordcount_filtered[word1] += 1
for k1,v1 in wordcount_filtered.items():
    print k1, v1