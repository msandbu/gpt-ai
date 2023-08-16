import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "OPENAIKEY"
HELICONE_API_KEY="HELICONEAPI"
from helicone.openai_proxy import openai

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "You are an AI assistant that helps the users with getting answers to their questions."
    },
    {
      "role": "user",
      "content": "What is the best way to get started with OpenAI?"
    }
  ],
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  user="alice@bob.com",
  cache=True,
	properties={"conversation_id": 12},
	rate_limit_policy={"quota": 100, "time_window": 60, "segment": "user"}
)

print(response)