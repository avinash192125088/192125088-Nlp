import re

def rule_based_pos_tagging(sentence):
    # Define regular expression patterns for parts of speech
    patterns = [
        (r'\b(?:the|a|an)\b', 'DET'),  # Determiners
        (r'\b(?:is|am|are|was|were)\b', 'VERB'),  # Verbs
        (r'\b(?:quick|brown|lazy)\b', 'ADJ'),  # Adjectives
        (r'\b(?:fox|dog)\b', 'NOUN'),  # Nouns
        (r'\b(?:over|on|under)\b', 'PREP'),  # Prepositions
        (r'\b(?:jumps|runs|walks)\b', 'VERB'),  # More Verbs
        (r'\b(?:the|a|an)\b', 'DET'),  # Determiners
        # Add more patterns as needed
    ]

    tagged_sentence = []
    
    # Apply the patterns to tag words in the sentence
    for word in sentence.split():
        for pattern, pos_tag in patterns:
            if re.search(pattern, word, flags=re.IGNORECASE):
                tagged_sentence.append((word, pos_tag))
                break
        else:
            # If no pattern matches, default to 'UNKNOWN'
            tagged_sentence.append((word, 'UNKNOWN'))

    return tagged_sentence

# Example usage:
input_sentence = "The quick brown fox jumps over the lazy dog."
tagged_result = rule_based_pos_tagging(input_sentence)

print("Tagged Sentence:")
for word, pos_tag in tagged_result:
    print(f"{word}: {pos_tag}")
