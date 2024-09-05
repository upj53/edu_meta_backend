from dotenv import dotenv_values
from openai import OpenAI

config = dotenv_values('.env')

client = OpenAI(
  api_key = config['OPENAI_API_KEY'],
)

'''
# 코딩추월차선
역할(Role)을 지정 해줍니다. 역할은 이번에 공개된 ChatGPT API 에서 공개된 중요한 기능중 하나로서 용도에 따라 시스템(System), 보조자(Assistant), 사용자(User)로 구분 됩니다. 각 역할에 대해서 간단히 설명을 드려보겠습니다.

시스템(System)역할은 ChatGPT에게 어떻게 행동을 할지 지정하는 기능이라고 생각하시면됩니다. 위의 예제에서 처럼 xxx를 입력 했다면 ChatGPT에서 상황을 설정할때 주로 사용하는 Act as a ___ 와 유사한 명령을 내릴때 사용됩니다.

보조자(Assistant)역할은 질문을 요청 하기 보다는 이전 대화를 저장하고 연속성을 유지하기 위해 사용되며 이어지는 답변에 영향을 줄수 있습니다. 이전 내용을 바탕으로 프롬프트를 요청 하고자 할때 사용 하실 수 있습니다.

사용자(User)의 역할은 chatGPT에 일반적으로 질문하는 질문 내용입니다. 사용자의 역할은 보조자(Assistant)와 마찬가지로 이전 대화를 저장하고 연속성을 유지하기 위해 사용되며 이어지는 답변에 영향을 줄수 있습니다.

시스템(System), 보조자(Assistant), 사용자(User)역할에 대한 자세한 설명은 Open API 문서를 참고해주세요.

https://platform.openai.com

사용자 역할 말고도 중요하게 사용되는 입력 값으로 온도(temperature), 텍스트의 최대 길이(max_tokens) 를 활용하는 방법이 있습니다.

온도값의 경우 다양성(degree of diversity) 정도를 나타내며 높을수록 창의적인 결과물을 만들어줍니다.

온도(temperature)값이 높을수록 모델이 생성하는 문장이 더 다양해지고, 값이 낮을수록 더 일관성 있는 문장이 생성 됩니다. 조금더 자세히 말씀 드시면 온도(temperature)값이 높은 경우, 다양한 선택지를 고려하여 텍스트를 생성합니다. 반면에, temperature 값이 낮은 경우, 모델은 가능한 선택지 중에서 가장 확률이 높은 것을 선택하게 됩니다. 그래서 온도 값이 낮을 셩우 일관성 있는 텍스트 결과가 만들어지고 일반적이거나 예상 가능한 결과를 만들 수도 있습니다.

온도(temperature)값의 범위는 0에서 무한대이지만 일반적으로 0.5 ~ 1.0 사이의 값이을 주로 사용 한다고 합니다. 정보성 글일때는 낮은 온도를 사용하고 창의성이 필요한 경우에는 높은 온도로 설정하여 사용하면 됩니다. 참고로 지정 안했을 때의 기본 값은 0.7입니다.

텍스트의 최대 길이(max_tokens)는 생성되는 텍스트의 최대 길이를 지정하는 값입니다. 기본값은 256이며 최대값은 2048입니다.
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)
output_text = response.choices[0].message.content
print(output_text)
# The 2020 World Series was played at Globe Life Field in Arlington, Texas.
'''

'''
# Prompt engineering
https://platform.openai.com/docs/guides/prompt-engineering
https://cookbook.openai.com/

# Prompt examples
Calculate time complexity
  Find the time complexity of a function.
Explain code
  Explain a complicated piece of code.
Python bug fixer
  Find and fix bugs in source code.
Function from specification
  Create a Python function from a specification.
Improve code efficiency
  Provide ideas for efficiency improvements to Python code.
Single page website creator
  Create a single page website.
Natural language to SQL
  Convert natural language into SQL queries.
'''

'''
# Calculate time complexity
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with Python code, and your task is to calculate its time complexity."
    },
    {
      "role": "user",
      "content": "def foo(n, k):\n        accum = 0\n        for i in range(n):\n            for l in range(k):\n                accum += i\n        return accum"
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)
print(response.choices[0].message.content)
'''

'''
# Explain code
response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with a piece of code, and your task is to explain it in a concise way."
    },
    {
      "role": "user",
      "content": "class Log:\n        def __init__(self, path):\n            dirname = os.path.dirname(path)\n            os.makedirs(dirname, exist_ok=True)\n            f = open(path, \"a+\")\n    \n            # Check that the file is newline-terminated\n            size = os.path.getsize(path)\n            if size > 0:\n                f.seek(size - 1)\n                end = f.read(1)\n                if end != \"\\n\":\n                    f.write(\"\\n\")\n            self.f = f\n            self.path = path\n    \n        def log(self, event):\n            event[\"_event_id\"] = str(uuid.uuid4())\n            json.dump(event, self.f)\n            self.f.write(\"\\n\")\n    \n        def state(self):\n            state = {\"complete\": set(), \"last\": None}\n            for line in open(self.path):\n                event = json.loads(line)\n                if event[\"type\"] == \"submit\" and event[\"success\"]:\n                    state[\"complete\"].add(event[\"id\"])\n                    state[\"last\"] = event\n            return state"
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)
'''

'''
# Python bug fixer
response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with a piece of Python code, and your task is to find and fix bugs in it."
    },
    {
      "role": "user",
      "content": "import Random\n    a = random.randint(1,12)\n    b = random.randint(1,12)\n    for i in range(10):\n        question = \"What is \"+a+\" x \"+b+\"? \"\n        answer = input(question)\n        if answer = a*b\n            print (Well done!)\n        else:\n            print(\"No.\")"
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)
'''

'''
# Function from specification
response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {
      "role": "user",
      "content": "Write a Python function that takes as input a file path to an image, loads the image into memory as a numpy array, then crops the rows and columns around the perimeter if they are darker than a threshold value. Use the mean value of rows and columns to decide if they should be marked for deletion."
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)
'''

'''
# Improve code efficiency
response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with a piece of Python code, and your task is to provide ideas for efficiency improvements."
    },
    {
      "role": "user",
      "content": "from typing import List\n                \n                \n    def has_sum_k(nums: List[int], k: int) -> bool:\n        \"\"\"\n        Returns True if there are two distinct elements in nums such that their sum \n        is equal to k, and otherwise returns False.\n        \"\"\"\n        n = len(nums)\n        for i in range(n):\n            for j in range(i+1, n):\n                if nums[i] + nums[j] == k:\n                    return True\n        return False"
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)
'''

'''
# Single page website creator
response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {
      "role": "user",
      "content": "Make a single page website that shows off different neat javascript features for drop-downs and things to display information. The website should be an HTML file with embedded javascript and CSS."
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)
'''

'''
# Natural language to SQL
response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "Given the following SQL tables, your job is to write queries given a user’s request.\n    \n    CREATE TABLE Orders (\n      OrderID int,\n      CustomerID int,\n      OrderDate datetime,\n      OrderTime varchar(8),\n      PRIMARY KEY (OrderID)\n    );\n    \n    CREATE TABLE OrderDetails (\n      OrderDetailID int,\n      OrderID int,\n      ProductID int,\n      Quantity int,\n      PRIMARY KEY (OrderDetailID)\n    );\n    \n    CREATE TABLE Products (\n      ProductID int,\n      ProductName varchar(50),\n      Category varchar(50),\n      UnitPrice decimal(10, 2),\n      Stock int,\n      PRIMARY KEY (ProductID)\n    );\n    \n    CREATE TABLE Customers (\n      CustomerID int,\n      FirstName varchar(50),\n      LastName varchar(50),\n      Email varchar(100),\n      Phone varchar(20),\n      PRIMARY KEY (CustomerID)\n    );"
    },
    {
      "role": "user",
      "content": "Write a SQL query which computes the average total order value for all orders on 2023-04-01."
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)
'''



'''
response = client.chat.completions.create(
  model='gpt-3.5-turbo-1106',
  response_format={'type': 'json_object'},
  messages = [
    {
      'role': 'system',
      'content': 'You are a helpful assistant designed to output JSON.'
    },
    {
      'role': 'user',
      'content': 'Who won the world series in 2020?'
    }
  ],
)
print(response.choices[0].message.content)
'''

prompt_text = '''
I'm a junior programmer.
I'm going to build an chat application using openai api for education.
I'll use python Flask for back-end, and Javascript for front-end.
Tell me about the process of this development. 
'''

'''
response = openai.Completion.create(
  engine = 'text-davinci-003',
  prompt = prompt_text,
  max_tokens = 100
)

print(response.choices[0].text.strip())
'''