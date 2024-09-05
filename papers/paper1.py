from dotenv import dotenv_values
from openai import OpenAI

config = dotenv_values('.env')

client = OpenAI(
  api_key = config['OPENAI_API_KEY'],
)

'''
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
'''
'''
    {
      'role': '',
      'content': ''
    },
'''
def get_test():
  response = client.chat.completions.create(
    model=config['OPENAI_MODEL'],
    messages=[
      {
        'role': 'system',
        'content': 'You are a teacher of Python programming. Your task is answering the following questions.'
      },
      {
        'role': 'system',
        'content': 'Translate all answers in korean.'
      },
      {
        'role': 'user',
        'content': 'Make 2 basic excercise questions for loop programming in the form of stories using real-life topics base on only input, output, and for loop.'
      },
    ],
    temperature=0.7,
    max_tokens=1000
  )
  output_text = response.choices[0].message.content
  print(output_text)

def get_chatgpt(msg):
  response = client.chat.completions.create(
    model=config['OPENAI_MODEL'],
    messages=msg,
    temperature=0.7,
    max_tokens=1000
  )
  output_text = response.choices[0].message.content
  return output_text