import openai
openai.api_key = "YOUR_API_KEY"

def generate_story(prompt):
    # Set the GPT-3 parameters
    model_engine = "text-davinci-002"
    max_tokens = 1024
    temperature = 0.5

    # Generate the story
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature
    )

    return response.choices[0].text

story_prompt = "A group of explorers find an ancient temple deep in the jungle."
story = generate_story(story_prompt)

print(story)
