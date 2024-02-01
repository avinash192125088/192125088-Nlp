import nltk
from nltk.corpus import wordnet as wn

def extract_noun_phrases_and_meanings(sentence):
    """Extracts noun phrases and their meanings from a sentence."""

    tokenized_text = nltk.word_tokenize(sentence)
    tagged_text = nltk.pos_tag(tokenized_text)

    noun_phrases = []
    for chunk in nltk.ne_chunk(tagged_text):
        if hasattr(chunk, 'label') and chunk.label() == 'NP':
            noun_phrase = " ".join(c[0] for c in chunk)
            meanings = []
            for word in noun_phrase.split():
                synsets = wn.synsets(word)
                if synsets:
                    meanings.append(synsets[0].definition())  # Get the first definition
            noun_phrases.append((noun_phrase, meanings))

    return noun_phrases

# Example usage
sentence = "The quick brown fox jumped over the lazy dog."
noun_phrases_and_meanings = extract_noun_phrases_and_meanings(sentence)
print("Noun phrases and their meanings:")
for noun_phrase, meanings in noun_phrases_and_meanings:
    print(f"Noun phrase: {noun_phrase}")
    print("Meanings:")
    for meaning in meanings:
        print(f"- {meaning}")
