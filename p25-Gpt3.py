import openai

openai.api_key = "YOUR_API_KEY"  # Replace with your actual API key

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use a powerful model for better results
        prompt=prompt,
        max_tokens=150,  # Adjust the maximum length of the generated text
        n=1,
        stop=None,
        temperature=0.7,  # Control the creativity of the generated text
    )
    return response.choices[0].text.strip()

# Sample prompt
prompt = "Write a poem about a robot who falls in love with a human."

# Generate text
generated_text = generate_text(prompt)

# Print the generated text
print(generated_text)
