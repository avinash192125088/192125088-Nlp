import re

def recognize_dialog_acts(dialog):
    dialog_acts = []
    for utterance in dialog.split('\n'):
        utterance = utterance.strip()
        if utterance:  # Skip empty lines
            act = None

            # Rule-based matching
            if utterance.startswith('what'):
                act = 'question'
            elif utterance.startswith('can you'):
                act = 'request'
            elif utterance.endswith('?'):
                act = 'question'
            elif re.match(r'^I would like to', utterance):
                act = 'request'
            elif utterance.startswith('yes') or utterance.startswith('no'):
                act = 'answer'
            else:
                act = 'statement'

            dialog_acts.append((utterance, act))

    return dialog_acts

# Sample dialog
dialog = """
Hello, how can I help you today?
I'm looking for a restaurant nearby.
What kind of food would you like?
I'm in the mood for Italian.
There's a great Italian restaurant just a few blocks away.
Can you give me the address?
Sure, it's 123 Main Street.
Thank you!
You're welcome!
"""

# Recognize dialog acts
dialog_acts = recognize_dialog_acts(dialog)

# Print results
print("Dialog Acts:")
for utterance, act in dialog_acts:
    print(f"- Utterance: {utterance}, Act: {act}")
