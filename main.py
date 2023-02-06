import nltk
from nltk.book import *
text1.concordance("monstrous")
text3.concordance("lived")
text2.common_contexts(["monstrous", "very"])
text3.generate()
print(len(text3))

#here our set represents unique lemmas
def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total

print(lexical_diversity(text1))

print(percentage(text1.count('a'), len(text1)))

fdist1 = FreqDist(text1)
print(fdist1)
print(fdist1.most_common(50))
print(fdist1['whale'])

#words that occur only once
fdist1.hapaxes()