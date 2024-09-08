import nltk
arpabet = nltk.corpus.cmudict.dict()

sentences = [
    "The sun set behind the distant mountains",
    "She quickly finished her book before dinner",
    "The cat napped peacefully on the window",
    "We explored the hidden trails in the forest"
]

for sentence in sentences:
    words = sentence.split(" ")
    print(" ".join(["-".join(arpabet[word.lower()][0]) for word in words]))
    print("\n")
