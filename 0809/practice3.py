from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="海為什麼是藍的"
)

print(interaction.output_text)