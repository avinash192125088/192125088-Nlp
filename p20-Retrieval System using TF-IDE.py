import math
from collections import Counter

documents = [
    "This is the first document. It is a simple document.",
    "This document is the second one. It has more words.",
    "And this is the third document. It has even more words."
]

query = "simple document"

stopwords = set(["this", "is", "the", "and", "it", "has"])

tokenized_documents = []
for doc in documents:
    doc = doc.lower()
    doc = doc.split()
    doc = [word for word in doc if word not in stopwords and word.isalpha()]
    tokenized_documents.append(doc)

N = len(documents)
vocabulary = set(word for doc in tokenized_documents for word in doc)

tfidf_scores = []
for doc in tokenized_documents:
    tfidf_doc = {}
    for term in vocabulary:
        tf = doc.count(term)
        df = sum(1 for d in tokenized_documents if term in d)
        idf = math.log(N / (df + 1))
        tfidf = tf * idf
        tfidf_doc[term] = tfidf
    tfidf_scores.append(tfidf_doc)

query = query.lower().split()
query_vector = Counter(query)

ranked_documents = []
for i, doc in enumerate(tfidf_scores):
    dot_product = sum(doc[term] * query_vector[term] for term in query if term in doc)
    doc_length = math.sqrt(sum(score ** 2 for score in doc.values()))
    query_length = math.sqrt(sum(score ** 2 for score in query_vector.values()))
    
    if query_length == 0:
        similarity = 0
    else:
        similarity = dot_product / (doc_length * query_length)

    ranked_documents.append((i, similarity))

ranked_documents.sort(key=lambda x: x[1], reverse=True)

for i, similarity in ranked_documents:
    print(f"Document {i + 1} - Similarity: {similarity:.4f}")
