from dotenv import dotenv_values
from openai import OpenAI

config = dotenv_values('.env')

client = OpenAI(
  api_key = config['OPENAI_API_KEY'],
)

def get_feedback(msg):
  response = client.chat.completions.create(
    model=config['OPENAI_MODEL'],
    messages=msg,
    temperature=0.7,
    max_tokens=1000
  )
  output_text = response.choices[0].message.content
  return output_text

def get_dialog(msg):
  response = client.chat.completions.create(
    model=config['OPENAI_MODEL'],
    messages=msg,
    temperature=0.7,
    max_tokens=1000
  )
  output_text = response.choices[0].message.content
  return output_text
