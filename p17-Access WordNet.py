import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

word_synsets = wordnet.synsets("example")

for synset in word_synsets:
    print(f"Synset: {synset.name()}")
    print(f"Definition: {synset.definition()}")
    print(f"Examples: {synset.examples()}")
    print()

word = "happy"
synonyms = []
for syn in wordnet.synsets(word):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

print(f"Synonyms for '{word}': {synonyms}")
