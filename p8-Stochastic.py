import nltk
from nltk import word_tokenize
from collections import defaultdict
import random

class SimplePOSTagger:
    def _init_(self):
        self.word_pos_counts = defaultdict(lambda: defaultdict(int))
        self.pos_counts = defaultdict(int)
        self.pos_probabilities = defaultdict(lambda: defaultdict(float))

    def train(self, tagged_corpus):
        for sentence in tagged_corpus:
            for word, pos in sentence:
                self.word_pos_counts[word][pos] += 1
                self.pos_counts[pos] += 1

        # Calculate probabilities
        for word, pos_counts in self.word_pos_counts.items():
            total_pos_count = sum(pos_counts.values())
            for pos, count in pos_counts.items():
                self.pos_probabilities[word][pos] = count / total_pos_count

    def tag_sentence(self, sentence):
        tagged_sentence = []
        for word in sentence:
            if word in self.word_pos_counts:
                pos_probabilities = self.pos_probabilities[word]
                most_probable_pos = max(pos_probabilities, key=pos_probabilities.get)
                tagged_sentence.append((word, most_probable_pos))
            else:
                # If word not seen during training, assign a random POS tag
                tagged_sentence.append((word, random.choice(list(self.pos_counts.keys()))))
        return tagged_sentence

# Example usage:
tagged_corpus = [
    [('This', 'DT'), ('is', 'VBZ'), ('a', 'DT'), ('sample', 'NN'), ('sentence', 'NN')],
    [('Another', 'DT'), ('example', 'NN'), ('is', 'VBZ'), ('given', 'VBN')]
]

# Train the POS tagger
pos_tagger = SimplePOSTagger()
pos_tagger.train(tagged_corpus)

# Tag a new sentence
new_sentence = "This is another sample sentence."
tokenized_sentence = word_tokenize(new_sentence)
tagged_sentence = pos_tagger.tag_sentence(tokenized_sentence)

print("Original Sentence:")
print(new_sentence)
print("\nTagged Sentence:")
print(tagged_sentence)
