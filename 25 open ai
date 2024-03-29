import openai

# Set your OpenAI API key here
api_key = 'YOUR_API_KEY'
openai.api_key = api_key

def generate_text(prompt, max_tokens=50, temperature=0.7):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature
    )
    return response.choices[0].text.strip()

# Example usage
prompt = "Once upon a time"
generated_text = generate_text(prompt)
print("Generated Text:")
print(generated_text)
