import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def evaluate_coherence(text):
    # Tokenize text into sentences
    sentences = sent_tokenize(text)

    # Calculate lexical diversity (ratio of unique words to total words)
    num_unique_words = len(set(word.lower() for sentence in sentences for word in sentence.split()))
    num_total_words = sum(len(sentence.split()) for sentence in sentences)
    lexical_diversity = num_unique_words / num_total_words

    # Calculate entity repetition (frequency of named entities)
    entities = set()
    for sentence in sentences:
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence))):
            if hasattr(chunk, 'label'):
                entities.add(chunk.label())
    entity_repetition = len(entities) / len(sentences)

    # Calculate semantic similarity scores between sentences
    stemmer = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    similarity_scores = []
    for i in range(len(sentences) - 1):
        sentence1_stems = [stemmer.stem(word.lower()) for word in sentences[i].split() if word.lower() not in stop_words]
        sentence2_stems = [stemmer.stem(word.lower()) for word in sentences[i + 1].split() if word.lower() not in stop_words]
        overlap = len(set(sentence1_stems) & set(sentence2_stems))
        similarity_score = overlap / len(set(sentence1_stems) | set(sentence2_stems))
        similarity_scores.append(similarity_score)

    # Combine scores into a coherence score
    coherence_score = 0.5 * lexical_diversity + 0.25 * entity_repetition + 0.25 * sum(similarity_scores) / len(similarity_scores)

    return coherence_score

# Sample text
text = """
The cat sat on the mat. It was a sunny day. The cat was happy. It purred contentedly.
"""

# Evaluate coherence
coherence_score = evaluate_coherence(text)
print("Coherence Score:", coherence_score)
