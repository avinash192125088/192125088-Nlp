from transformers import pipeline

# Load a pre-trained English-to-French translation model
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")

# Sample English text
text = "Hello, how are you?"

# Translate the text
translation = translator(text, max_length=40)

# Print the translated text
print(translation[0]['translation_text'])
