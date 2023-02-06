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

#words with at least 7 words occurring at least 7 times
fdist5 = FreqDist(text5)
sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)

#collocation is a sequence of words that occur together unusually often.
# Thus red wine is a collocation, whereas the wine is not.
text4.collocations()
list(bigrams(['more', 'is', 'said', 'than', 'done']))

#frequency of word lengths:
fdist = FreqDist(len(w) for w in text1)
print(fdist)
print(fdist.most_common())

#fdist = FreqDist(samples)	create a frequency distribution containing the given samples
#fdist[sample] += 1	increment the count for this sample
#fdist['monstrous']	count of the number of times a given sample occurred
#fdist.freq('monstrous')	frequency of a given sample
#fdist.N()	total number of samples
#fdist.most_common(n)	the n most common samples and their frequencies
#for sample in fdist:	iterate over the samples
#fdist.max()	sample with the greatest count
#fdist.tabulate()	tabulate the frequency distribution
#fdist.plot()	graphical plot of the frequency distribution
#fdist.plot(cumulative=True)	cumulative plot of the frequency distribution
#fdist1 |= fdist2	update fdist1 with counts from fdist2
#fdist1 < fdist2	test if samples in fdist1 occur less frequently than in fdist2


#In word sense disambiguation we want to work out which sense of a word was intended in a given context

#pronoun resolution is to detect the subjects and objects of verbs
#involves finding the antecedent of the pronoun
#techniques include
#anaphora resolution — identifying what a pronoun or noun phrase refers to — and
#semantic role labeling — identifying how a noun phrase relates to the verb (as agent, patient, instrument, and so on)

#To derive the vocabulary, collapsing case distinctions and ignoring punctuation, we can write set(w.lower() for w in text if w.isalpha())