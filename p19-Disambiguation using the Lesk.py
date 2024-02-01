import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')

def lesk_algorithm(context, target_word):
    context_tokens = word_tokenize(context)
    context_words = [word.lower() for word in context_tokens if word.lower() not in stopwords.words('english')]

    target_synsets = wordnet.synsets(target_word)

    if not target_synsets:
        return None  

    best_sense = None
    max_overlap = 0

    for sense in target_synsets:
        sense_definition = word_tokenize(sense.definition())
        sense_examples = [word.lower() for word in word_tokenize(' '.join(sense.examples()))]

        overlap = len(set(context_words).intersection(set(sense_definition + sense_examples)))

        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense

    return best_sense

context = "He saw the bat fly over the baseball field."
target_word = "bat"
result = lesk_algorithm(context, target_word)
if result:
    print(f"Word sense of '{target_word}' in the context: {result.name()} - {result.definition()}")
else:
    print(f"Unable to disambiguate the word '{target_word}' in the context.")
