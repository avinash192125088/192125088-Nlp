import re
sentence = "The quick brown fox jumps over the lazy dog"
initial_tagging = {
    'The': 'DT',
    'quick': 'NN',
    'brown': 'NN',
    'fox': 'NN',
    'jumps': 'NN',
    'over': 'IN',
    'the': 'DT',
    'lazy': 'NN',
    'dog': 'NN'
}
transformation_rules = [
    (r'(\w+) DT (\w+)', r'\1 NN \2'),  
    (r'(\w+) IN (\w+)', r'\1 NN \2'),  
    (r'(\w+) NN (\w+)', r'\1 VB \2'),  
    (r'(\w+) NN (\w+)', r'\1 JJ \2'),  
]
improvement = True
while improvement:
    improvement = False
    previous_tagging = initial_tagging.copy()
    for rule in transformation_rules:
        pattern, replacement = rule
        for word in initial_tagging:
            initial_tagging[word] = re.sub(pattern, replacement, initial_tagging[word])
    if initial_tagging != previous_tagging:
        improvement = True
tagged_sentence = [(word, tag) for word, tag in initial_tagging.items()]
print(tagged_sentence)
