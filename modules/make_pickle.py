import pickle

subject_list_dump = [
    {
        "idx": 1,
        "subject_title": "파이썬 프로그래밍 기초 Part 1",
        "subject_main_idea": """""",
        "subject_main_1": """""",
        "subject_main_2": """""",
        "subject_main_3": """""",
        "subject_goal": """""",
        "subject_goal_detail": """""",
    },
    {
        "idx": 2,
        "subject_title": "파이썬 프로그래밍 기초 Part 2",
        "subject_main_idea": """""",
        "subject_main_1": """""",
        "subject_main_2": """""",
        "subject_main_3": """""",
        "subject_goal": """""",
        "subject_goal_detail": """""",
    },
    {
        "idx": 3,
        "subject_title": "알고리즘과 프로그래밍 Part 1",
        "subject_main_idea": """- 문제를 효율적으로 해결하기 위해서는 문제를 추상화하고, 프로그래밍을 위한 알고리즘을 설계한다.
- 데이터 모델링을 하기 위해 문제 해결에 필요한 데이터 간의 관계를 분석하고, 정의한다.
- 프로그래밍을 통한 자동화는 다양한 학문 분야의 문제를 해결하는 데 도움을 준다.""",
        "subject_main_1": """- 문제 분해와 모델링
- 정렬, 탐색 알고리즘
- 자료형
- 표준입출력과 파일입출력
- 다차원 데이터 활용
- 제어 구조의 응용
- 클래스와 인스턴스""",
        "subject_main_2": """- 문제를 분해하고 모델링하기
- 알고리즘의 수행 과정 및 효율성 비교 · 분석하기
- 문제 해결에 적합한 자료형과 입출력 구조를 활용하여 프로그램 작성하기
- 복잡한 문제를 해결하기 위해 제어 구조와 다차원 데이터 구조를 복합적으로 활용하기
- 클래스를 정의하고 인스턴스를 생성하여 문제 해결에 적합한 객체를 구현하기""",
        "subject_main_3": """- 문제 해결 모델을 구성하고 적극적으로 표현하는 자세
- 알고리즘 효율의 가치와 영향력을 인식하고 적극적으로 탐구하는 태도
- 다양한 학문 분야의 문제 해결을 위해 설계한 알고리즘을 프로그램으로 구현하는 실천적 자세
- 디지털 사회의 민주시민으로서 협력적 문제 해결력의 중요성을 인식하는 자세""",
        "subject_goal": """1. 복잡한 문제를 해결 가능한 작은 문제로 분해하고 모델링한다.
2. 데이터를 정렬하는 다양한 알고리즘의 특징과 효율을 비교 · 분석한다.
3. 데이터를 탐색하는 다양한 알고리즘의 특징과 효율을 비교 · 분석한다.
4. 자료형의 종류와 특성을 알고, 접합한 자료형을 선택하여 프로그램을 작성한다.
5. 표준입출력과 파일입출력을 활용한 프로그램을 작성한다.
6. 다차원 데이터 구조를 활용한 프로그램을 작성한다.
7. 다양한 제어 구조를 복합적으로 활용한 프로그램을 작성한다.
8. 객체를 구현하는 클래스와 인스턴스를 활용하여 프로그램을 작성한다.
9. 실생활 및 다양한 학문 분야의 문제 해결을 위한 프로그램을 협력적으로 설계 · 구현한다.
10. 문제 해결을 위한 프로그램의 성능을 평가하고 공유한다.""",
        "subject_goal_detail": """- 복잡한 문제를 분석하는 단계에서 좀 더 작은 문제로 분해하는 과정을 수행하며, 해결하기 용이하도록 단순화나 구조화하는 모델링 단계를 수행할 수 있어야 한다. 작은 문제의 해결 결과를 종합하는 과정에서 작은 문제를 모두 수행했을 때 전체 문제 해결이 원활하게 이루어지는지, 오류가 없는지를 확인할 수 있어야 한다.
- 여러 가지 정렬, 탐색 알고리즘을 적용하여 실생활의 간단한 데이터의 정렬, 탐색 문제를 해결할 수 있어야 한다. 정렬, 탐색 알고리즘의 수행 과정을 분석해보고 문제에 따라 알고리즘의 효율성이 다를 수 있음을 설명할 수 있어야 한다.
- 실생활의 사례를 활용하여 객체 지향의 기본 개념을 이해하고 필요성을 설명할 수 있어야 한다. 클래스와 객체를 생성하고 문제 해결을 위한 프로그램 구현에 활용할 수 있어야 한다.""",
    },
    {
        "idx": 4,
        "subject_title": "알고리즘과 프로그래밍 Part 2",
        "subject_main_idea": """""",
        "subject_main_1": """""",
        "subject_main_2": """""",
        "subject_main_3": """""",
        "subject_goal": """""",
        "subject_goal_detail": """""",
    },
    {
        "idx": 5,
        "subject_title": "인공지능 Part 1",
        "subject_main_idea": """""",
        "subject_main_1": """""",
        "subject_main_2": """""",
        "subject_main_3": """""",
        "subject_goal": """""",
        "subject_goal_detail": """""",
    },
    {
        "idx": 6,
        "subject_title": "인공지능 Part 2",
        "subject_main_idea": """""",
        "subject_main_1": """""",
        "subject_main_2": """""",
        "subject_main_3": """""",
        "subject_goal": """""",
        "subject_goal_detail": """""",
    },
]

object_list_dump = [
    {
        "idx": 1,
        "subject_idx": 1,
        "object_title": "변수와 자료형",
        "object_detail": """- 변수와 자료형의 종류와 특성을 알고, 적합한 자료형을 선택하여 프로그램을 작성한다.
- 내용 1
- 내용 2

<b>HTML 태그가 될까?</b>

<p style="color:red; font-size:20px;">HTML 태그가 되는구나!!</p>

<table style="border:1px solid black; margin:10px;">
<tr>
<td>A</td>
<td>B</td>
<td>C</td>
</tr>
<tr>
<td>가</td>
<td>나</td>
<td>다</td>
</tr>
</table>

1. 보기 1
2. 보기 2
3. 보기 3

**할렐루야**

만세""",
    },
    {
        "idx": 2,
        "subject_idx": 1,
        "object_title": "연산자",
        "object_detail": """- 1차원 배열의 데이터 구조를 활용한 프로그램을 작성한다.""",
    },
    {
        "idx": 3,
        "subject_idx": 1,
        "object_title": "선택 제어문",
        "object_detail": """- 다양한 제어 구조를 복합적으로 활용한 프로그램을 작성한다.""",
    },
    {
        "idx": 4,
        "subject_idx": 1,
        "object_title": "반복 제어문",
        "object_detail": """- 다양한 제어 구조를 복합적으로 활용한 프로그램을 작성한다.""",
    },
    {
        "idx": 5,
        "subject_idx": 2,
        "object_title": "함수",
        "object_detail": """- 함수의 특성을 이해하고 함수를 활용한 프로그램을 작성한다.""",
    },
    {
        "idx": 6,
        "subject_idx": 2,
        "object_title": "클래스와 인스턴스",
        "object_detail": """- 객체를 구현하는 클래스와 인스턴스를 활용하여 프로그램을 작성한다.""",
    },
]

problem_list_dump = [
    {
        "object_idx": 1,
        "problem_level": 1,
        "problem_question": """다음은 파이썬에서 변수를 선언한 코드이다. 잘못 사용한 것을 고르시오.""",
        "problem_content": """""",
        "level_1_selection_answer": "1a = 5",
        "level_1_selection_1": "apple = 1",
        "level_1_selection_2": "Apple = 2",
        "level_1_selection_3": "___ = 3",
    },
    {
        "object_idx": 1,
        "problem_level": 1,
        "problem_question": """다음은 파이썬에서 변수를 선언한 코드이다. 잘못 사용한 것을 고르시오.""",
        "problem_content": """""",
        "problem_result": """""",
        "level_1_selection_answer": "True = 6",
        "level_1_selection_1": "변수 = 4",
        "level_1_selection_2": "ABC = 7",
        "level_1_selection_3": "a, b = 5, -3",
    },
    {
        "object_idx": 1,
        "problem_level": 1,
        "problem_question": """다음은 파이썬의 자료형의 종류를 출력하는 코드이다. 예상되는 실행 결과를 고르시오.""",
        "problem_content": """```python
a = 3.14
b = str(a)

print(type(a), type(b))
```""",
        "problem_result": """""",
        "level_1_selection_answer": "<class 'float'> <class 'str'>",
        "level_1_selection_1": "<class 'int'> <class 'str'>",
        "level_1_selection_2": "<class 'str'> <class 'str'>",
        "level_1_selection_3": "None None",
    },
    {
        "object_idx": 1,
        "problem_level": 1,
        "problem_question": """다음 중 파이썬 리스트의 표현 방법으로 잘못된 것을 고르시오.""",
        "problem_content": """""",
        "problem_result": """""",
        "level_1_selection_answer": "n3 = (1, 5, 10)",
        "level_1_selection_1": "n1 = [1, 5, 10]",
        "level_1_selection_2": "n2 = list()",
        "level_1_selection_3": "n4 = [1, 'a', 3>1]",
    },
    {
        "object_idx": 1,
        "problem_level": 1,
        "problem_question": """다음은 파이썬의 2차원 배열이다. 파이썬 코드의 예상되는 실행 결과로 올바른 것을 고르시오.""",
        "problem_content": """```python
m = [['A', 1], ['B', 2], ['C', 3]]

print(m[0][0] + m[1][0], m[1][1] + m[2][1])
```""",
        "problem_result": """""",
        "level_1_selection_answer": "AB, 5",
        "level_1_selection_1": "A1, B2",
        "level_1_selection_2": "5, AB",
        "level_1_selection_3": "에러",
    },
    {
        "object_idx": 1,
        "problem_level": 2,
        "problem_answer": """```python
fruit = '사과'
count = 5
price = 10000
print(fruit, count, '개', price, '원')
```""",
        "problem_question": """아래와 같은 실행 결과가 나오도록 파이썬 코드를 완성하세요.""",
        "problem_content": """""",
        "problem_result": """```text
사과 5 개 10000 원
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요
print(fruit, count, '개', price, '원')
```""",
        "level_2_num_of_answers": 0,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 1,
        "problem_level": 2,
        "problem_answer": """```python
one = '원주율'
pi = 3.141592
print(one, '=', pi)
```""",
        "problem_question": """아래와 같은 실행 결과가 나오도록 파이썬 코드를 완성하세요.""",
        "problem_content": """""",
        "problem_result": """```text
원주율 = 3.141592
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요
print(one, '=', pi)
```""",
        "level_2_num_of_answers": 0,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 1,
        "problem_level": 2,
        "problem_answer": """```python
a = '부울형'
b = True
c = False
print(a, '은', b, '또는', c, '를 갖는 자료형이다.')
```""",
        "problem_question": """아래와 같은 실행 결과가 나오도록 파이썬 코드를 완성하세요.""",
        "problem_content": """""",
        "problem_result": """```text
부울형 은 True 또는 False 를 갖는 자료형이다.
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요
print(a, '은', b, '또는', c, '를 갖는 자료형이다.')
```""",
        "level_2_num_of_answers": 0,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 1,
        "problem_level": 2,
        "problem_answer": """```python
m = [0, 1, 2, 3, 4]
n = ['A', 'E', 'H', 'L', 'O']
print(n[2]+n[1]+n[3]+n[3]+n[4], str(m[2])+str(m[0])+str(m[3])+str(m[0]))
```""",
        "problem_question": """다음은 파이썬 1차원 배열을 선언한 코드이다. 아래와 같은 실행 결과가 나오도록 배열(m, n)과 print문을 사용하여 파이썬 코드를 완성하세요.""",
        "problem_content": """""",
        "problem_result": """```text
HELLO 2030
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요
m = [0, 1, 2, 3, 4]
n = ['A', 'E', 'H', 'L', 'O']
```""",
        "level_2_num_of_answers": 0,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 1,
        "problem_level": 2,
        "problem_answer": """```python
서랍 = [['연필', '지우개'], ['가위', '풀'], ['공책', '색종이']]
print(서랍[2][0], 서랍[1][1])
```""",
        "problem_question": """2차원 배열은 2개의 인덱스를 사용하는 배열로, 1차원 배열을 여러 개 쌓아 놓은 구조를 가진다. 아래와 같은 실행 결과가 나오도록 배열(서랍)과 print문을 사용하여 파이썬 코드를 완성하세요.""",
        "problem_content": """""",
        "problem_result": """```text
공책 풀
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요
서랍 = [['연필', '지우개'], ['가위', '풀'], ['공책', '색종이']]
print(  )
```""",
        "level_2_num_of_answers": 0,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 1,
        "problem_level": 3,
        "problem_answer": """```python
school = '초월중학교'
hak, ban, bunho = 2, 3, 11
name = '강산들'
print(school)
print(hak, '학년', ban, '반', bunho, '번호')
print('이름:', name)
```""",
        "problem_question": """다음 사진은 초월 중학교 학생의 학생증이다. 주어진 자료형대로 변수를 선언하고 실행 결과와 같이 출력되도록 파이썬 print문을 사용하여 코드를 작성하세요.""",
        "problem_content": """<img src="https://github.com/upj53/shared/assets/27456270/7dce1df8-e724-454f-ad5a-7556ac08ead7" alt="" style="width:350px; height:auto;"/>

자료형

<table class="table table-bordered table-hover">
<thead class="table-light text-center">
<tr>
<td>자료</td>
<td>변수명</td>
<td>자료형</td>
</tr>
</thead>
<tbody>
<tr class="text-center">
<td>학교명</td>
<td>school</td>
<td>문자열</td>
</tr>
<tr class="text-center">
<td>학년</td>
<td>hak</td>
<td>정수</td>
</tr>
<tr class="text-center">
<td>반</td>
<td>ban</td>
<td>정수</td>
</tr>
<tr class="text-center">
<td>번호</td>
<td>bunho</td>
<td>정수</td>
</tr>
<tr class="text-center">
<td>이름</td>
<td>name</td>
<td>문자열</td>
</tr>
</tbody>
</table>""",
        "problem_result": """```text
초월중학교
2 학년 3 반 11 번
이름: 강산들
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 1,
        "problem_level": 3,
        "problem_answer": """```python
name = '태블릿'
memory = 2
weight = 480.5
discount = True
thick = 10
print('제품이름:', name, '\n메모리:', memory, 'GB')
print('무게:', weight, 'g\n두께:',thick, 'mm')
if discount:
  print('할인여부: 할인됨')
else:
  print('할인여부: 할인 안됨')
```""",
        "problem_question": """다음 태블릿의 특징을 관찰한 후, 그 값을 자료로 저장하고 실행 결과와 같이 출력되도록 파이썬 코드를 작성하시오.""",
        "problem_content": """<img src="https://github.com/upj53/shared/assets/27456270/87751e96-2b33-4554-9537-5f0a880e534b" alt="" style="width:450px; height:auto;"/>

<table class="table table-bordered table-hover">
<thead class="table-light text-center">
<tr>
<td>자료</td>
<td>변수명</td>
<td>관찰된 값</td>
<td>자료형</td>
</tr>
</thead>
<tbody>
<tr class="text-center">
<td>제품 이름</td>
<td>name</td>
<td>태블릿</td>
<td>문자열</td>
</tr>
<tr class="text-center">
<td>메모리(GB)</td>
<td>memory</td>
<td>2</td>
<td>정수</td>
</tr>
<tr class="text-center">
<td>무게(g)</td>
<td>weight</td>
<td>480.5</td>
<td>실수</td>
</tr>
<tr class="text-center">
<td>할인 여부</td>
<td>discount</td>
<td>예</td>
<td>불린형(참거짓형)</td>
</tr>
<tr class="text-center">
<td>두께(mm)</td>
<td>thick</td>
<td>10</td>
<td>정수</td>
</tr>
</tbody>
</table>""",
        "problem_result": """```text
제품 이름: 태블릿
메모리: 2 GB
무게: 480.5 g
두께: 10 mm
할인 여부: (참일 경우: 할인됨, 거짓일 경우: 할인 안됨) 으로 표시
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 1,
        "problem_level": 3,
        "problem_answer": """```python
name, amount = '튼튼 영양제', 1
vitamin_c, vitamin_d, ayeon = 54, 3.22, 3.63
company, phone = '건강 만만세', '080-999-3333'
print(name, '영양 기능 정보')
print()
print('1일 섭취량:', amount, '정')
print('1일 섭취 당 함량: 비타민C', vitamin_c, 'mg, 비타민D', vitamin_d, 'mg, 아연', ayeon, 'mg')
print()
print('판매원:', company)
print('소비자 상담:', phone)
```""",
        "problem_question": """다음은 튼튼 영양제의 영양 기능 정보를 나타낸 표이다. 영양 기능 정보를 관찰하여 실행 결과와 같이 출력되도록 해당되는 정보를 파이썬 변수로 저장하고 print문으로 출력하시오.""",
        "problem_content": """<img src="https://github.com/upj53/shared/assets/27456270/14038771-f583-45b0-86d2-c400312db444" alt="" style="width:150px; height:auto;"/>

<table class="table table-bordered table-hover">
<thead class="table-light text-center">
<tr>
<td>자료</td>
<td>변수명</td>
<td>관찰된 값</td>
<td>자료형</td>
</tr>
</thead>
<tbody>
<tr class="text-center">
<td>제품 이름</td>
<td>name</td>
<td>튼튼 영양제</td>
<td>문자열</td>
</tr>
<tr class="text-center">
<td>1일 섭취량</td>
<td>amount</td>
<td>1</td>
<td>정수</td>
</tr>
<tr class="text-center">
<td>1일 섭취 당 비타민C 함량</td>
<td>vitamin_c</td>
<td>54</td>
<td>정수</td>
</tr>
<tr class="text-center">
<td>1일 섭취 당 비타민D 함량</td>
<td>vitamin_d</td>
<td>3.22</td>
<td>실수</td>
</tr>
<tr class="text-center">
<td>1일 섭취 당 지방 함량</td>
<td>fat</td>
<td>0</td>
<td>정수</td>
</tr>
<tr class="text-center">
<td>1일 섭취 당 아연 함량</td>
<td>ayeon</td>
<td>3.63</td>
<td>실수</td>
</tr>
<tr class="text-center">
<td>판매원</td>
<td>company</td>
<td>건강 만만세</td>
<td>문자열</td>
</tr>
<tr class="text-center">
<td>소비자 상담 전화번호</td>
<td>phone</td>
<td>080-999-3333</td>
<td>문자열</td>
</tr>
<tr class="text-center">
<td>홈페이지</td>
<td>homepage</td>
<td>www.healthone.com</td>
<td>문자열</td>
</tr>
</tbody>
</table>""",
        "problem_result": """```text
튼튼 영양제 영양 기능 정보

1일 섭취량: 1 정
1일 섭취 당 함량: 비타민C 54 mg, 비타민D 3.22 mg, 아연 3.63 mg

판매원: 건강 만만세
소비자 상담: 080-999-3333
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 1,
        "problem_level": 3,
        "problem_answer": """```python
import random

menu = ['김밥', '떡볶이', '순대', '어묵', '가락국수', '튀김']
random.shuffle(menu)
for m in menu[:3]:
    print(m)
```""",
        "problem_question": """다음 분식 메뉴에서 무작위로 메뉴 3가지를 고르는 복불복 프로그램을 파이썬으로 작성한 후 print문을 사용하여 실행 결과와 같이 출력하시오. 단, 같은 메뉴는 중복해서 나올 수 없습니다.""",
        "problem_content": """(힌트)

- random 모듈의 random() 함수는 0.0 부터 1.0 사이의 실수를 반환합니다.
- random 모듈의 randint(a, b) 함수는 a이상 b이하의 정수를 반환합니다.
- random 모듈의 shuffle(c) 함수는 리스트 c의 원소를 무작위 순서로 섞습니다.

<table class="table table-bordered table-hover">
<thead class="table-light text-center">
<tr>
<td>분식 메뉴</td>
</tr>
</thead>
<tbody>
<tr>
<td>'김밥', '떡볶이', '순대', '어묵', '가락국수', '튀김'</td>
</tr>
</tbody>
</table>""",
        "problem_result": """```text
튀김
순대
어묵
```

```text
순대
가락국수
떡볶이
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 1,
        "problem_level": 3,
        "problem_answer": """```python
name = input("행성 이름을 입력하세요: ")
distance = input("행성까지의 거리(km)를 입력하세요: ")
speed = input("이동 속도(km/h)를 입력하세요: ")

totaltime = distance / speed
totaltime = int(totaltime)
year = totaltime / (365*24)
year = int(year)
month = (totaltime - (year*365*24))/(30*24)
month = int(month)
day = (totaltime - (year*365*24) - (month*30*24))/24
day = int(day)
time = totaltime - (year*365*24) - (month*30*24) - (day*24)

print("지구에서 ", name, "까지")
print("이동 시간:", totaltime, "시간")
print("환산된 이동 시간:", year, "년", month, "월", day, "일", time, "시간")
```""",
        "problem_question": """천체 관측에 관심이 많은 철수는 태양계의 다른 행성까지 이동하는 데 걸리는 시간을 계산해주는 프로그램을 만들려고 한다. 아래 수식을 참고하여 지구에서 행성까지의 거리와 이동속도를 입력하면 행성까지 가는 데 걸리는 시간을 자동으로 계산해주는 프로그램을 파이썬 코드로 작성하고 실행 결과와 같이 출력하시오.""",
        "problem_content": """지구에서 행성까지 이동하는데 걸리는 시간(h)을 거리(km)와 이동 속도(km/h)를 사용하여 구하는 계산식

<center><img src="https://github.com/upj53/shared/assets/27456270/8822cf8f-2b33-47bd-b33f-24b1f1c8817c" alt="" style="width:600px; height:auto; margin-bottom:20px;"/></center>

시간(hour)으로 계산된 이동 시간을 몇년 몇월 몇일에 해당하는지 환산할 수 있는 수식

<center><img src="https://github.com/upj53/shared/assets/27456270/4e5f0be1-58cb-44a6-a854-9c0068d3dd5a" alt="" style="width:450px; height:auto; margin-bottom:20px;"/></center>

<table class="table table-bordered table-hover">
<thead class="table-light text-center">
<tr>
<td>행성 이름</td>
<td>지구에서 행성까지의 거리</td>
</tr>
</thead>
<tbody>
<tr>
<td class="text-center">수성</td>
<td class="text-end">9170만 km</td>
</tr>
<tr>
<td class="text-center">금성</td>
<td class="text-end">4140만 km</td>
</tr>
<tr>
<td class="text-center">화성</td>
<td class="text-end">7840만 km</td>
</tr>
<tr>
<td class="text-center">목성</td>
<td class="text-end">6억 2870만 km</td>
</tr>
<tr>
<td class="text-center">토성</td>
<td class="text-end">12억 7740만 km</td>
</tr>
<tr>
<td class="text-center">천왕성</td>
<td class="text-end">27억 5040만 km</td>
</tr>
<tr>
<td class="text-center">해왕성</td>
<td class="text-end">43억 4740만 km</td>
</tr>
</tbody>
</table>""",
        "problem_result": """```text
[입력]
행성 이름을 입력하세요: 화성
행성까지의 거리(km)를 입력하세요: 7840000
이동 속도(km/h)를 입력하세요: 300

[출력]
지구에서 화성까지
이동 시간: 261333시간
환산된 이동 시간: 29년 10월 3일 21시간
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 2,
        "problem_level": 1,
        "problem_question": """다음은 파이썬에서 연산자를 사용한 코드이다. 예상되는 결과를 고르시오.""",
        "problem_content": """```python
print(30+12/4-45)
```""",
        "problem_result": """""",
        "level_1_selection_answer": "-12.0",
        "level_1_selection_1": "None",
        "level_1_selection_2": "-12",
        "level_1_selection_3": "12",
    },
    {
        "object_idx": 2,
        "problem_level": 1,
        "problem_question": """다음은 파이썬에서 연산자를 사용한 코드이다. 예상되는 결과를 고르시오.""",
        "problem_content": """```python
print(10 // 3, 10 % 3)
```""",
        "problem_result": """""",
        "level_1_selection_answer": "3 1",
        "level_1_selection_1": "None None",
        "level_1_selection_2": "3.0 1.0",
        "level_1_selection_3": "3.33333333333333335 1.0",
    },
    {
        "object_idx": 2,
        "problem_level": 1,
        "problem_question": """다음은 파이썬에서 연산자를 사용한 코드이다. 예상되는 결과를 고르시오.""",
        "problem_content": """```python
n = 3
print(1 < n < 5)
```""",
        "problem_result": """""",
        "level_1_selection_answer": "True",
        "level_1_selection_1": "None",
        "level_1_selection_2": "에러",
        "level_1_selection_3": "False",
    },
    {
        "object_idx": 2,
        "problem_level": 1,
        "problem_question": """다음은 파이썬에서 산술 연산자를 사용한 코드이다. 예상되는 결과를 고르시오.""",
        "problem_content": """```python
a = (34+12)/4
b = 10 % 4
print(a, b)
```""",
        "problem_result": """""",
        "level_1_selection_answer": "11.5  2",
        "level_1_selection_1": "11  2",
        "level_1_selection_2": "11.5  2.0",
        "level_1_selection_3": "11  2.0",
    },
    {
        "object_idx": 2,
        "problem_level": 1,
        "problem_question": """다음은 파이썬의 비교 연산자를 사용한 코드이다. 예상되는 결과를 고르시오.""",
        "problem_content": """```python
x = 15
a = x > 30
b = x <= 15
c = x == 7
d = x != 17
print(a, b, c, d)
```""",
        "problem_result": """""",
        "level_1_selection_answer": "False True False True",
        "level_1_selection_1": "False False True True",
        "level_1_selection_2": "True False True False",
        "level_1_selection_3": "True True False False",
    },
    {
        "object_idx": 2,
        "problem_level": 2,
        "problem_answer": """```python
print( (34+12)/4 )
```""",
        "problem_question": """아래와 같은 실행 결과가 나오도록 다음 수식을 계산하는 파이썬 코드를 완성하세요.""",
        "problem_content": """<img src="https://github.com/upj53/shared/assets/27456270/4f20d19b-7cb0-4cc6-bfac-619b9ad64a50" alt="" style="width:90px; height:auto;"/>

```python
# 코드를 완성하세요
print(   )
```""",
        "problem_result": """```text
11.5
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요

```""",
        "level_2_num_of_answers": 0,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 2,
        "problem_level": 2,
        "problem_answer": """```python
a = 11
b = 4
print('몫 =', a // b)
print('나머지 =', a % b)
```""",
        "problem_question": """다음과 같은 실행 결과가 나오도록 나누기 연산의 몫과 나머지를 계산하는 파이썬 코드를 완성하세요.""",
        "problem_content": """```python
# 코드를 완성하세요
a = 11
b = 4
print('몫 =',  )
print('나머지 =',  )
```""",
        "problem_result": """```text
몫 = 2
나머지 = 3
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요

```""",
        "level_2_num_of_answers": 0,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 2,
        "problem_level": 2,
        "problem_answer": """```python
a = 2
b = 10
print('결과 =', a ** b)
```""",
        "problem_question": """다음과 같은 실행 결과가 나오도록 제곱 연산을 계산하는 파이썬 코드를 완성하세요.""",
        "problem_content": """```python
# 코드를 완성하세요
a = 2
b = 10
print('결과 =',  )
```""",
        "problem_result": """```text
결과 = 1024
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요

```""",
        "level_2_num_of_answers": 0,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 2,
        "problem_level": 2,
        "problem_answer": """```python
a = 10
b = 3
print('덧셈 =', a+b)
print('뺄셈 =', a-b)
print('곱셈 =', a*b)
print('나눗셈 =', a/b)
print('몫 =', a//b)
print('나머지 =', a%b)
```""",
        "problem_question": """파이썬의 산술 연산을 사용하여 실행 결과와 같이 나오도록 코드를 완성하세요.""",
        "problem_content": """```python
# 코드를 완성하세요
a = 10
b = 3
print('덧셈 =',   )
print('뺄셈 =',   )
print('곱셈 =',   )
print('나눗셈 =',   )
print('몫 =',    )
print('나머지 =',   )
```""",
        "problem_result": """```text
덧셈 = 13
뺼셈 = 7
곱셈 = 30
나눗셈 = 3.3333333333333335
몫 = 3
나머지 = 1
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요

```""",
        "level_2_num_of_answers": 0,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 2,
        "problem_level": 2,
        "problem_answer": """```python
a = 10
b = 6
print('덧셈 =', a+b)
print('뺄셈 =', a-b)
print('곱셈 =', a*b)
print('제곱 =', a**b)
```""",
        "problem_question": """파이썬의 산술 연산을 사용하여 실행 결과와 같이 나오도록 코드를 완성하세요.""",
        "problem_content": """```python
# 코드를 완성하세요
a = 10
b = 6
print('덧셈 =',   )
print('뺄셈 =',   )
print('곱셈 =',   )
print('제곱 =',   )
```""",
        "problem_result": """```text
덧셈 = 16
뺼셈 = 4
곱셈 = 60
제곱 = 1000000
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요

```""",
        "level_2_num_of_answers": 0,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 2,
        "problem_level": 3,
        "problem_answer": """```python
a, b, c = 2, 3, 4
print('계산 결과:', (-a + b**2 - 4*a*c) / (2*a - b*c) )
```""",
        "problem_question": """아래 수식을 계산하는 코드를 파이썬으로 구현하고, a=2, b=3, c=4 변수를 선언한 후 계산 결과를 print문으로 출력하시오.""",
        "problem_content": """<img src="https://github.com/upj53/shared/assets/27456270/a06c851f-ab7a-4177-ad76-f26dc8df38d3" alt="" style="width:150px; height:auto;"/>""",
        "problem_result": """```text
계산 결과: 3.125
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 2,
        "problem_level": 3,
        "problem_answer": """```python
price = int(input("빵의 단가를 입력하세요: "))
count = int(input("빵의 개수를 입력하세요: "))
total = price * count
total = total - total * 0.1
print('전체 빵값 =', total)
```""",
        "problem_question": """아래 조건을 만족하는 빵값 계산 프로그램을 파이썬 코드로 작성하고 전체 빵값을 print문으로 출력하세요.""",
        "problem_content": """> 빵의 단가는 800원이고, 구매 개수는 10개이다.
> 전체 빵값은 '빵의 단가 × 구매 개수' 로 계산한다.
> 전체 빵값의 10% 를 할인해준다.""",
        "problem_result": """```text
[입력]
빵의 단가를 입력하세요: 700
빵의 개수를 입력하세요: 20

[출력]
전체 빵값 = 12600.0
```

```text
[입력]
빵의 단가를 입력하세요: 800
빵의 개수를 입력하세요: 15

[출력]
전체 빵값 = 10800.0
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 2,
        "problem_level": 3,
        "problem_answer": """```python
h = input('키(cm)를 입력하세요: ')
w = input('몸무게(kg)를 입력하세요: ')
h = int(h)
w = int(w)
bmi = (w / h**2) * 10000
print('체질량 지수는', bmi,'입니다.')
```""",
        "problem_question": """다음 수식을 참고하여 키(cm)와 몸무게(kg)를 입력 받아 체질량 지수를 구하는 파이썬 코드를 완성하고, 아래 실행 결과와 같이 출력하세요.""",
        "problem_content": """<img src="https://github.com/upj53/shared/assets/27456270/4e9cd267-5a63-44af-bb39-5eee854e0b34" alt="" style="width:200px; height:auto;"/>""",
        "problem_result": """```text
키(cm)를 입력하세요: 179
몸무게(kg)를 입력하세요: 67
체질량 지수는 20.910708155176177 입니다.
```

```text
키(cm)를 입력하세요: 170
몸무게(kg)를 입력하세요: 83
체질량 지수는 28.719723183391004 입니다.
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 2,
        "problem_level": 3,
        "problem_answer": """```python
adult = input('어른의 수를 입력하세요: ')
child = input('아이의 수를 입력하세요: ')
adult = int(adult)
child = int(child)
total = 7000 * adult + 2500 * child
total = total - total * 0.15
print('전체 입장료 =', total)
```""",
        "problem_question": """아래 조건을 만족하는 놀이동산 입장료 계산 프로그램을 파이썬 코드로 작성하고 전체 입장료를 print문으로 출력하세요.""",
        "problem_content": """> 어른 1명의 입장료는 7000원 이다.
> 아이 1명의 입장료는 2500원 이다.
> 전체 입장료는 '어른의 1명의 입장료 × 어른의 수' + '아이 1명의 입장료 × 아이의 수' 로 계산한다.
> 전체 입장료는 15% 를 할인해준다.""",
        "problem_result": """```text
[입력]
어른의 수를 입력하세요: 10
아이의 수를 입력하세요: 7

[출력]
전체 입장료 = 74375.0
```

```text
[입력]
어른의 수를 입력하세요: 5
아이의 수를 입력하세요: 57

[출력]
전체 입장료 = 150875.0
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 2,
        "problem_level": 3,
        "problem_answer": """```python
tax = 0.0675
tip = 0.15

meal = int(input('음식의 가격을 입력하세요: '))

meal_tax_price = meal + meal * tax
tip_price = meal_tax_price * tip

print(f'음식 가격: {meal:.2f} 원')
print(f'세금 포함 가격: {meal_tax_price:.2f} 원')
print(f'팁 금액: {tip_price:.2f} 원')
```""",
        "problem_question": """흥민이는 미국여행을 하는 동안 음식점에서 팁을 내는 문화를 경험하였다. 이 경험을 바탕으로 식당에서 음식을 사멱으면 팁과 세금을 자동으로 계산해주는 프로그램을 파이썬으로 만들려고 한다. 아래 표를 참고하여 실행 결과와 같이 나오도록 파이썬 코드를 작성하세요.""",
        "problem_content": """단, 모든 가격은 소수 둘째자리까지 출력하세요.

(hint)

- 파이썬 포멧 함수를 사용하면 출력 형식을 지정할 수 있습니다.
- print('{:.3f}'.format(변수)) 변수 값의 소수점 3째자리 까지 출력합니다
- print(f'{변수:.4f}') 변수 값의 소수점 4째자리 까지 출력합니다

<table class="table table-bordered table-hover">
<thead class="table-light text-center">
<tr>
<td>구성</td>
<td>비율</td>
<td>설명</td>
</tr>
</thead>
<tbody>
<tr class="text-center">
<td class="align-middle">세금</td>
<td class="align-middle">0.0675</td>
<td>순수 음식 값을 기준으로 부가되는 세금</td>
</tr>
<tr class="text-center">
<td class="align-middle">팁</td>
<td class="align-middle">0.15</td>
<td>세금이 부가된 음식값을 기준으로 부가되는 서비스 요금</td>
</tr>
</tbody>
</table>""",
        "problem_result": """```text
[입력]
음식의 가격을 입력하세요: 75000

[출력]
음식 가격: 75000.00 원
세금 포함 가격: 80062.50 원
팁 금액: 12009.38 원
```

```text
[입력]
음식의 가격을 입력하세요:

[출력]
음식의 가격을 입력하세요: 237650
음식 가격: 237650.00 원
세금 포함 가격: 253691.38 원
팁 금액: 38053.71 원
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 3,
        "problem_level": 1,
        "problem_question": """다음은 파이썬의 선택 제어문을 나타낸 코드이다. 연산자 비교식을 이용해서 올바르게 사용한 것을 고르시오.""",
        "problem_content": """""",
        "problem_result": """""",
        "level_1_selection_answer": "if a == 2:",
        "level_1_selection_1": "if a = 3:",
        "level_1_selection_2": "if a >> 5:",
        "level_1_selection_3": "if a << 1:",
    },
    {
        "object_idx": 3,
        "problem_level": 1,
        "problem_question": """다음은 파이썬의 선택 제어문을 나타낸 코드이다. 연산자 비교식을 잘못 사용한 것을 고르시오.""",
        "problem_content": """""",
        "problem_result": """""",
        "level_1_selection_answer": "if (n > 1) && (n < 5):",
        "level_1_selection_1": "if n != 2:",
        "level_1_selection_2": "if n >= 3:",
        "level_1_selection_3": "if 1 < n < 5:",
    },
    {
        "object_idx": 3,
        "problem_level": 1,
        "problem_question": """다음 순서도를 파이썬 코드로 바르게 나타낸 것을 고르시오.""",
        "problem_content": """<img src="https://github.com/upj53/shared/assets/27456270/8b352c1d-a36c-415a-ab53-756973b28887" alt="" style="width:300px; height:auto;"/>""",
        "problem_result": """""",
        "level_1_selection_answer": """```python
if a > 0:
    print('양수')
else:
    print('음수')
```""",
        "level_1_selection_1": """```python
if a < 0:
    print('양수')
if a > 0:
    print('음수')
```""",
        "level_1_selection_2": """```python
if a > 0:
    print('음수')
else:
    print('양수')
```""",
        "level_1_selection_3": """```python
if a < 0:
    print('양수')
else:
    print('음수')
```""",
    },
    {
        "object_idx": 3,
        "problem_level": 1,
        "problem_question": """다음은 파이썬의 선텍 제어문을 나타낸 코드이다. 연산자 비교식을 이용해서 올바르게 사용한 것을 고르시오.""",
        "problem_content": """""",
        "problem_result": """""",
        "level_1_selection_answer": "if a >= 1:",
        "level_1_selection_1": "if a <> 4:",
        "level_1_selection_2": "if a !! 7:",
        "level_1_selection_3": "if a >< 5:",
    },
    {
        "object_idx": 3,
        "problem_level": 1,
        "problem_question": """다음은 파이썬의 선택 제어문을 나타낸 코드이다. 연산자 비교식을 잘못 사용한 것을 고르시오.""",
        "problem_content": """""",
        "problem_result": """""",
        "level_1_selection_answer": "if (n + 10) or (n - 1):",
        "level_1_selection_1": "if (n > 1) and (n < 9):",
        "level_1_selection_2": "if True:",
        "level_1_selection_3": "if 0:",
    },
    {
        "object_idx": 3,
        "problem_level": 2,
        "problem_answer": """```python
a = input('숫자를 입력하세요: ')
a = int(a)
if a % 2 == 0:
    print('짝수입니다.')
else:
    print('홀수입니다.')
```""",
        "problem_question": """숫자를 입력 받고, 입력 받은 숫자가 짝수 인지 홀수인지 출력하는 파이썬 코드를 완성하세요.""",
        "problem_content": """""",
        "problem_result": """```text
숫자를 입력하세요: 5
홀수입니다.
```

```text
숫자를 입력하세요: 8
짝수입니다.
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요.
a = input('숫자를 입력하세요: ')
a = int(a)
if   :
  print('짝수입니다.')
else:
  print('홀수입니다.')
```""",
        "level_2_num_of_answers": 0,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 3,
        "problem_level": 2,
        "problem_answer": """```python
a = input('숫자를 입력하세요: ')
a = int(a)
if a == 0:
    print('0입니다.')
else:
    if a > 0:
        print('양수입니다.')
    else:
        print('음수입니다.')
```""",
        "problem_question": """다음 순서도를 파이썬 코드를 사용하여 완성하세요.""",
        "problem_content": """<img src="https://github.com/upj53/shared/assets/27456270/aa5ea11c-c206-4722-8f97-4eae3469c1b9" alt="" style="width:400px; height:auto;"/>""",
        "problem_result": """```text
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요
a = input('숫자를 입력하세요: ')
a = int(a)
if   :
  print('0입니다.')
else:
  if   :
    print('양수입니다.')
  else:
    print('음수입니다.')

```""",
        "level_2_num_of_answers": 0,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 3,
        "problem_level": 2,
        "problem_answer": """```python
m = input('몇월인가요? ')
m = int(m)
if 3 <= m <= 5:
    print('봄입니다.')
elif 6 <= m <= 8:
    print('여름입니다.')
elif 9 <= m <= 11:
    print('가을입니다.')
else:
    print('겨울입니다.')
```""",
        "problem_question": """다음 표를 참고하여 아래와 같은 실행 결과가 나오도록 파이썬 코드를 완성하세요.""",
        "problem_content": """<table class="table table-bordered table-hover">
<thead class="table-light text-center">
<tr>
<td>계절</td>
<td>월</td>
</tr>
</thead>
<tbody>
<tr>
<td>봄</td>
<td>3월, 4월, 5월</td>
</tr>
<tr>
<td>여름</td>
<td>6월, 7월, 8월</td>
</tr>
<tr>
<td>가을</td>
<td>9월, 10월, 11월</td>
</tr>
<tr>
<td>겨울</td>
<td>12월, 1월, 2월</td>
</tr>
</tbody>
</table>""",
        "problem_result": """```text
몇월인가요? 3
3 월은 봄입니다.
```

```text
몇월인가요? 12
12 월은 겨울입니다.
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요
m = input('몇월인가요? ')
m = int(m)
if  :
  print(m, '월은 봄입니다.')
elif   :
  print(m, '월은 여름입니다.')
elif   :
  print(m, '월은 가을입니다.')
else:
  print(m, '월은 겨울입니다.')
```""",
        "level_2_num_of_answers": 0,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 3,
        "problem_level": 2,
        "problem_answer": """```python
time = input("탑승 운행 시간을 입력하세요: ")
time = int(time)

total = 3000 + int(time/10) * 500
if time >= 60:
    total = total + total * 0.2

print("택시 요금 =", total)
```""",
        "problem_question": """다음은 택시 요금 정보입니다. 파이썬으로 규칙에 맞게 택시 요금을 계산하는 프로그램을 완성하고 실행 결과와 같이 택시 요금을 출력하세요.""",
        "problem_content": """> 택시 기본 요금은 3000원 입니다.
> 택시 요금은 탐승 운행 시간 10분 당 500원입니다.
> 10분 이하의 요금은 계산하지 않습니다.
> 탑승 운행 시간이 60분 이상이면 20%의 할증 요금이 추가됩니다.""",
        "problem_result": """```text
[입력]
탑승 운행 시간을 입력하세요: 35

[출력]
택시 요금 = 4500
```

```text
[입력]
탑승 운행 시간을 입력하세요: 77

[출력]
택시 요금 = 7800.0
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요
time = input("탑승 운행 시간을 입력하세요: ")
time = int(time)

total = 
if       :
  total = 

print("택시 요금 =", total)
```""",
        "level_2_num_of_answers": 0,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 3,
        "problem_level": 2,
        "problem_answer": """```python
adult = int(input("어른의 수를 입력하세요: "))
child = int(input("아이의 수를 입력하세요: "))
total = adult * 7000 + child * 4500

if total >= 50000:
    total = total - total * 0.1

print("영화 티켓 총액은 ", total,"원 입니다.")
```""",
        "problem_question": """다음은 영화 티켓의 가격 정보입니다. 파이썬으로 규칙에 맞게 영화 티켓 가격을 계산하는 프로그램을 완성하고 실행 결과와 같이 지불할 총액을 출력하세요.""",
        "problem_content": """> 어른 1명 영화 티켓의 가격은 7000원 입니다.
> 아이 1명 영화 티켓의 가격은 4500원 입니다.
> 전체 결제 금액이 50000원 이상이면 10% 할인을 합니다.""",
        "problem_result": """```text
[입력]
어른의 수를 입력하세요: 3
아이의 수를 입력하세요: 2

[출력]
영화 티켓 총액은 30000 원 입니다.
```

```text
[입력]
어른의 수를 입력하세요: 7
아이의 수를 입력하세요: 5

[출력]
영화 티켓 총액은 64350.0 원 입니다.
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요

```""",
        "level_2_num_of_answers": 0,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 3,
        "problem_level": 3,
        "problem_answer": """```python
point = input('점수를 입력하세요: ')
point = int(point)
if 90 <= point <= 100:
    print('A')
elif 80 <= point < 90:
    print('B')
elif 70 <= point < 80:
    print('C')
elif 60 <= point < 70:
    print('D')
else:
    print('F')
```""",
        "problem_question": """다음 표는 점수에 따른 성취도를 나타내고 있다. 아래 실행 결과를 참고하여 0점부터 100점 사이의 점수를 입력 받으면 성취도를 출력하는 파이썬 코드를 작성하세요.""",
        "problem_content": """<table class="table table-bordered table-hover">
<thead class="table-light text-center">
<tr>
<td>점수(점)</td>
<td>성취도</td>
</tr>
</thead>
<tbody>
<tr class="text-center">
<td>90점 이상 100점 이하</td>
<td>A</td>
</tr>
<tr class="text-center">
<td>80점 이상 90점 미만</td>
<td>B</td>
</tr>
<tr class="text-center">
<td>70점 이상 80점 미만</td>
<td>C</td>
</tr>
<tr class="text-center">
<td>60점 이상 70점 미만</td>
<td>D</td>
</tr>
<tr class="text-center">
<td>0점 이상 60점 미만</td>
<td>F</td>
</tr>
</tbody>
</table>""",
        "problem_result": """```text
점수를 입력하세요: 79
C
```

```text
점수를 입력하세요: 89.9
B
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 3,
        "problem_level": 3,
        "problem_answer": """```python
print('다음 보기 중 하나를 선택하시오. (1/2/3)')
n = int(input())
if n == 1:
    print('당신은 적극적인 성격의 사람입니다.')
elif n == 2:
    print('당신은 침착한 성격의 사람입니다.')
elif n == 3:
    print('당신은 긍정적인 성격의 사람입니다.')
else:
    print('잘못된 입력입니다.')
```""",
        "problem_question": """다음 심리 검사의 보기 중 하나를 선택하면 대답을 출력하는 심리 검사 프로그램을 만들려고 합니다. 아래 순서도대로 동작하는 프로그램을 파이썬 코드를 사용하여 완성하세요.""",
        "problem_content": """> 어느 날 다음과 같은 문자가 왔다.
> '친구 ○○○ 가 크게 다쳐서 현재 △△병원 응급실에서 치료를 받고 있습니다.'
> 문자를 확인하고 당신은 어떤 반응을 보일 것인가?
> 
> [보기]
> ① 빨리 다른 친구들에게 알려야겠다.
> ② 진짜 치료 중인지 확인부터 해야겠어.
> ③ 아마 큰일은 아닐 거야. 괜찮겠지.

<img src="https://github.com/upj53/shared/assets/27456270/75b69bac-73df-430c-b0fb-aa1b5ae4728a" alt="" style="width:300px; height:auto;"/>""",
        "problem_result": """```text
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 3,
        "problem_level": 3,
        "problem_answer": """```python
age = input('나이를 입력하세요: ')
age = int(age)
cost = 14000
if age >= 60:
    print('30% 할인 대상입니다.')
    cost = cost - cost * 0.3
elif age <= 10:
    print('20% 할인 대상입니다.')
    cost = cost - cost * 0.2
else:
    print('할인 대상이 아닙니다.')

print('찜질방 이용요금:', cost)
```""",
        "problem_question": """영미네 동네 찜질방에서는 나이에 따른 요금 할인을 해 주고 있다. 실행 결과를 참고하여 할인 조건이 아래 표와 같을 때, 요금을 계산해 주는 프로그램을 파이썬 코드를 만들어보세요.""",
        "problem_content": """<table class="table table-bordered table-hover">
<tbody>
<tr>
<td class="table-light text-center">기본 요금</td>
<td class="text-center">14000원</td>
</tr>
<tr>
<td class="table-light text-center">60세 이상</td>
<td class="text-center">30% 할인</td>
</tr>
<tr>
<td class="table-light text-center">10세 이하</td>
<td class="text-center">20% 할인</td>
</tr>
</tbody>
</table>""",
        "problem_result": """```text
나이를 입력하세요: 65

30% 할인 대상입니다.
찜질방 이용 요금: 9800원
```

```text
나이를 입력하세요: 7

20% 할인 대상입니다.
찜질방 이용 요금: 11200원
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 3,
        "problem_level": 3,
        "problem_answer": """```python
card = int(input('카드의 잔액을 입력하세요: '))
user = int(input('어른이면 '어른'을 입력하고, 아이이면 '아이'를 입력하세요: '))
if user == '어른':
    if card >= 1300:
            card -= 1300
            print('교통카드의 잔액', card, '원')
    else:
            print('교통카드의 잔액이 부족합니다.')
elif user == '아이':
    if card >= 700:
            card -= 700
            print('교통카드의 잔액이 부족합니다.')
    else:
            print('교통카드의 잔액', card, '원')
```""",
        "problem_question": """버스 교통카드 프로그램을 파이썬으로 만들려고 합니다. 아래 조건을 참고해서 실행 결과와 같이 작동하는 버스 교통카드 프로그램을 완성하세요.""",
        "problem_content": """> 교통카드 계산을 하기 전에 어른인지 아이인지 물어봅니다.
> 어른 버스요금은 1300원 입니다.
> 아이 버스요금은 700원 입니다.
> 교통카드의 잔액이 버스요금 이상 충전되어 있는지 체크합니다.
> 교통카드의 잔액이 버스요금 이상 충전되어 있으면 버스요금을 계산하고 그만큼을 차감합니다.
> 교통카드의 잔액이 버스요금 이상 충전되어 있지 않으면 버스 탑승이 불가합니다.

<img src="https://github.com/upj53/shared/assets/27456270/d0561743-89bd-4671-b143-da4db42ea327" alt="" style="width:300px; height:auto;"/>""",
        "problem_result": """```text
[입력]
카드의 잔액을 입력하세요: 1200
어른이면 '어른'을 입력하고, 아이이면 '아이'를 입력하세요: 어른

[출력]
교통카드의 잔액이 부족합니다.
```

```text
[입력]
카드의 잔액을 입력하세요: 2000
어른이면 '어른'을 입력하고, 아이이면 '아이'를 입력하세요: 어른

[출력]
교통카드의 잔액: 700 원
```

```text
[입력]
카드의 잔액을 입력하세요: 2000
어른이면 '어른'을 입력하고, 아이이면 '아이'를 입력하세요: 아이

[출력]
교통카드의 잔액: 1300 원
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 3,
        "problem_level": 3,
        "problem_answer": """```python
price = [1100, 1500, 1200, 800]
money = int(input('입력할 금액을 입력하세요: '))
menu = input('주문할 메뉴 이름을 입력하세요: ')

if menu == '사이다':
    if money >= price[0]:
        money -= price[0]
        print('사이다를 주문했습니다')
        print('거스름돈:', money)
    else:
        print('입력한 금액이 부족합니다.')
elif menu == '콜라':
    if money >= price[1]:
        money -= price[1]
        print('콜라를 주문했습니다')
        print('거스름돈:', money)
    else:
        print('입력한 금액이 부족합니다.')
elif menu == '환타':
    if money >= price[2]:
        money -= price[2]
        print('환타를 주문했습니다')
        print('거스름돈:', money)
    else:
        print('입력한 금액이 부족합니다.')
elif menu == '생수':
    if money >= price[3]:
        money -= price[3]
        print('생수를 주문했습니다')
        print('거스름돈:', money)
    else:
        print('입력한 금액이 부족합니다.')
```""",
        "problem_question": """자판기 물건을 주문하는 프로그램을 파이썬으로 만들려고 합니다. 아래 규칙을 보고 실행 결과와 같이 작동하는 자판기 물건 주문 프로그램을 완성하세요.""",
        "problem_content": """<img src="https://github.com/upj53/shared/assets/27456270/25c24bb6-d80d-48dd-ad83-e58a8e02651c" alt="" style="width:200px; height:auto;"/>

<table class="table table-bordered table-hover">
<thead class="table-light text-center">
<tr>
<td>메뉴명</td>
<td>가격</td>
</tr>
</thead>
<tbody class="text-center">
<tr>
<td>사이다</td>
<td>1100</td>
</tr>
<tr>
<td>콜라</td>
<td>1500</td>
</tr>
<tr>
<td>환타</td>
<td>1200</td>
</tr>
<tr>
<td>생수</td>
<td>800</td>
</tr>
</tbody>
</table>""",
        "problem_result": """```text
[입력]
입력할 금액을 입력하세요: 2000
주문할 메뉴 이름을 입력하세요: 콜라

[출력]
콜라를 주문했습니다.
거스름돈: 900 원
```

```text
[입력]
입력할 금액을 입력하세요: 1000
주문할 메뉴 이름을 입력하세요: 사이다

[출력]
사이다를 주문했습니다.
입력한 금액이 부족합니다.
```

```text
[입력]
입력할 금액을 입력하세요: 1000
주문할 메뉴 이름을 입력하세요: 생수

[출력]
생수를 주문했습니다.
거스름돈: 200 원
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 4,
        "problem_level": 1,
        "problem_question": """다음은 파이썬의 반복 제어문을 나타낸 코드이다. 잘못 사용한 것을 고르시오.""",
        "problem_content": """""",
        "problem_result": """""",
        "level_1_selection_answer": "for i in range(1 < 10):",
        "level_1_selection_1": "for i in range(5):",
        "level_1_selection_2": "for i in range(1, 10):",
        "level_1_selection_3": "for i in range(1, 10, 2):",
    },
    {
        "object_idx": 4,
        "problem_level": 1,
        "problem_question": """다음은 파이썬의 반복 제어문을 나타낸 코드이다. 잘못 사용한 것을 고르시오.""",
        "problem_content": """""",
        "problem_result": """""",
        "level_1_selection_answer": "while -1:",
        "level_1_selection_1": "while a <= 3:",
        "level_1_selection_2": "while 1:",
        "level_1_selection_3": "while True:",
    },
    {
        "object_idx": 4,
        "problem_level": 1,
        "problem_question": """다음은 파이썬의 반복 제어문을 나타낸 코드이다. 예상되는 실행 결과를 고르시오.""",
        "problem_content": """```python
for a in range(1, 10, 2):
    print(a, end=',')
```""",
        "problem_result": """""",
        "level_1_selection_answer": "1,3,5,7,9,",
        "level_1_selection_1": "1,2,3,4,5,6,7,8,9,10,",
        "level_1_selection_2": "2,4,6,8,10,",
        "level_1_selection_3": "1,2,3,4,5,6,7,8,9,",
    },
    {
        "object_idx": 4,
        "problem_level": 1,
        "problem_question": """다음 파이썬 코드의 예상되는 실행결과를 고르시오.""",
        "problem_content": """```python
for n in range(10):
  if n%2 == 0:
    continue
  print(n, end=' ')
```""",
        "problem_result": """""",
        "level_1_selection_answer": "1 3 5 7 9",
        "level_1_selection_1": "0 1 2 3 4 5 6 7 8 9",
        "level_1_selection_2": "1 2 3 4 5 6 7 8 9 10",
        "level_1_selection_3": "0 2 4 6 8",
    },
    {
        "object_idx": 4,
        "problem_level": 1,
        "problem_question": """다음 파이썬 코드의 예상되는 실행결과를 고르시오.""",
        "problem_content": """```python
num = 0
while num < 10:
  print(num, end=' ')
  if num == 5:
    break
  num += 1
```""",
        "problem_result": """""",
        "level_1_selection_answer": "0 1 2 3 4 5",
        "level_1_selection_1": "1 2 3 4 5 6",
        "level_1_selection_2": "0 2 4",
        "level_1_selection_3": "1 3 5 7 9",
    },
    {
        "object_idx": 4,
        "problem_level": 2,
        "problem_answer": """```python
total = 0
for i in range(1, 101):
    total += i
print(total)
```""",
        "problem_question": """파이썬의 for 반복 제어문을 사용해서 1부터 100까지 모든 숫자를 더하는 코드를 완성하세요.""",
        "problem_content": """""",
        "problem_result": """```text
총합 = 5050
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요
total = 0
for □□□-1번-□□□:
    □□□-2번-□□□
print('총합 =', total)
```""",
        "level_2_num_of_answers": 2,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 4,
        "problem_level": 2,
        "problem_answer": """```python
i, total = 1, 0
while i <= 100:
    total += i
    i += 1
print(total)
```""",
        "problem_question": """파이썬의 while 반복 제어문을 사용해서 1부터 100까지 모든 숫자를 더하는 코드를 완성하세요.""",
        "problem_content": """""",
        "problem_result": """```text
총합 = 5050
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요
i, total = 1, 0
while □□□-1번-□□□:
    □□□-2번-□□□
    i += 1

print('총합 =', total)
```""",
        "level_2_num_of_answers": 2,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 4,
        "problem_level": 2,
        "problem_answer": """```python
while True:
    n = input('종료 를 입력하면 프로그램을 종료합니다.')
    if n == '종료':
        print('프로그램 종료')
        break
```""",
        "problem_question": """파이썬의 무한 반복문을 다음 조건에서 종료하는 코드를 완성하세요.""",
        "problem_content": """- 종료 조건 : 콘솔에 '종료' 를 입력한다.""",
        "problem_result": """```text
종료 를 입력하면 프로그램을 종료합니다.
종료
프로그램 종료
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요
while True:
  n = input('종료 를 입력하면 프로그램을 종료합니다.')
  if □□□-1번-□□□:
    print('프로그램 종료')
    □□□-2번-□□□
```""",
        "level_2_num_of_answers": 2,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 4,
        "problem_level": 2,
        "problem_answer": """```python
num = 0
while num < 10:
    num += 1
    if num == 5:
        continue
    print(num)
```""",
        "problem_question": """파이썬의 반복문을 사용해서 아래 실행 결과와 같이 나오도록 코드를 완성하세요.""",
        "problem_content": """""",
        "problem_result": """```text
1
2
3
4
6
7
8
9
10
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요
num = 0
while num < 10:
    num += 1
    if □□□-1번-□□□:
        □□□-2번-□□□
    print(num)
```""",
        "level_2_num_of_answers": 2,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 4,
        "problem_level": 2,
        "problem_answer": """```python
for j in range(4):
    for i in range(5):
        print("*", end="")
    print("")
```""",
        "problem_question": """파이썬 반복문을 사용해서 실행 결과와 같이 나오도록 코드를 완성하세요.""",
        "problem_content": """""",
        "problem_result": """```text
*****
*****
*****
*****
```""",
        "level_2_initcodes": """```python
# 코드를 완성하세요
for         :
  for          :
    print("*", end="")
  print("")
```""",
        "level_2_num_of_answers": 2,
        "level_2_answer_1": "",
        "level_2_answer_2": "",
        "level_2_answer_3": "",
        "level_2_answer_4": "",
        "level_2_answer_5": "",
    },
    {
        "object_idx": 4,
        "problem_level": 3,
        "problem_answer": """```python
point = 0
total = 0
for i in range(1, 21, 1):
    text = str(i) + '회 다트 점수를 입력하세요: '
    point = input(text)
    point = int(point)
    print(i, '회 점수는', point)
    total = total + point
print('최종 점수는', total)
```""",
        "problem_question": """다트를 20번 던져 얻은 점수를 계속 출력하고, 점수를 모두 더한 최종 점수를 출력한 다음 종료하는 프로그램을 파이썬 for 반복문으로 만들어보세요.""",
        "problem_content": """> 다트 점수는 0점 부터 10점까지 있습니다.

<table class="table table-bordered table-hover">
<tbody>
<tr>
<td class="table-light text-center">시작값</td>
<td class="text-center">1</td>
</tr>
<tr>
<td class="table-light text-center">끝값</td>
<td class="text-center">21</td>
</tr>
<tr>
<td class="table-light text-center">증감값</td>
<td class="text-center">+1</td>
</tr>
<tr>
<td class="table-light text-center align-middle">게임에서 반복하는 일</td>
<td>
<ul>
<li>다트를 던지고 점수를 입력한다.</li>
<li>입력된 점수를 출력한다.</li>
<li>입력된 점수를 최종 점수에 더한다.</li>
</ul>
</td>
</tr>
</tbody>
</table>""",
        "problem_result": """```text
1회 다트 점수를 입력하세요: 7
1 회 점수는 7
2회 다트 점수를 입력하세요: 3
2 회 점수는 3
···
19회 다트 점수를 입력하세요: 1
19 회 점수는 1
20회 다트 점수를 입력하세요: 9
20 회 점수는 9
최종 점수는 117
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 4,
        "problem_level": 3,
        "problem_answer": """```python
kind = ''
basketball = 0
football = 0
baseball = 0
while kind != '종료':
    kind = input('입력하세요 [농구공, 축구공, 야구공, 종료]:')
    if kind == '농구공':
        basketball += 1
    elif kind == '축구공':
        football += 1
    elif kind == '야구공':
        baseball += 1
    elif kind == '종료':
        break
    else:
        print('잘못된 입력입니다.')
print('농구공의 개수:', basketball)
print('축구공의 개수:', football)
print('야구공의 개수:', baseball)
```""",
        "problem_question": """학교에 있는 공의 개수를 파악하는 데 사용할 프로그램을 만들려고 합니다. 파이썬의 while 반복문을 이용해서 다음 조건을 만족하는 프로그램을 만들어보세요.""",
        "problem_content": """> ◎ 프로그램이 입력 대기 상태에 있을 때
>   '농구공, 축구공, 야구공' 중 하나를 입력하면,
>   입력한 공의 개수가 1개씩 증가하고,
>   '종료' 를 입력하면 프로그램이 종료된다.
> 
> ◎ '농구공, 축구공, 야구공, 종료' 이외의 값을 입력하면
>   잘못된 입력임을 알리고, 다시 입력하도록 한다.

<table class="table table-bordered table-hover">
<tbody>
<tr>
<td class="table-light text-center">농구공</td>
<td class="text-center">농구공의 개수를 1 증가시킨다.</td>
</tr>
<tr>
<td class="table-light text-center">축구공</td>
<td class="text-center">축구공의 개수를 1 증가시킨다.</td>
</tr>
<tr>
<td class="table-light text-center">야구공</td>
<td class="text-center">야구공의 개수를 1 증가시킨다.</td>
</tr>
<tr>
<td class="table-light text-center">종료</td>
<td class="text-center">프로그램을 종료한다.</td>
</tr>
<tr>
<td class="table-light text-center">그 외의 입력</td>
<td class="text-center">정확한 입력을 요구한다.</td>
</tr>
</tbody>
</table>""",
        "problem_result": """```text
입력하세요 [농구공, 축구공, 야구공, 종료]:농구공
입력하세요 [농구공, 축구공, 야구공, 종료]:농구공
입력하세요 [농구공, 축구공, 야구공, 종료]:축구공
입력하세요 [농구공, 축구공, 야구공, 종료]:야구공
입력하세요 [농구공, 축구공, 야구공, 종료]:탁구공
잘못된 입력입니다.
입력하세요 [농구공, 축구공, 야구공, 종료]:야구공
입력하세요 [농구공, 축구공, 야구공, 종료]:종료
농구공의 개수: 2
축구공의 개수: 1
야구공의 개수: 2
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 4,
        "problem_level": 3,
        "problem_answer": """```python
mtime = 0
mcost = 0
ytime = 0
ycost = 0
for i in range(1, 13):
    text = str(i) + '월 통화 시간(분)을 입력하세요:'
    mtime = input(text)
    mtime = int(mtime)

    mcost = mtime * 60 * 2

    print(i, '월 통화 시간:', mtime)
    print(i, '월 사용 요금:', mcost)

    ytime = ytime + mtime
    ycost = ycost + mcost

print('1년 동안의 통화 시간:', ytime)
print('1년 동안의 사용 요금:', ycost)
```""",
        "problem_question": """○○텔레콤에서는 회원들의 통화 시간과 요금을 관리하기 위한 프로그램을 개발하려고 한다. 아래와 같이 월별 통화 시간을 입력하면 월별 사용 요금을 계산해서 출력하고, 최종적으로 1년 동안의 통화 시간과 사용 요금을 출력하는 프로그램을 만들어보세요.""",
        "problem_content": """> [프로그램의 실행 과정]
> ◎ 매월 통화 시간을 입력한다. (단위: 분)
> ◎ 월별 사용 요금은 (매월 통화시간 × 단위 요금) 으로 계산한다. (1초에 2원)
> ◎ 매월 통화한 시간과 요금을 출력한다.
> ◎ 1년 동안의 통화 시간과 사용 요금을 출력한다.""",
        "problem_result": """```text
1월 통화 시간(분)을 입력하세요: 210
1 월 통화 시간:  210
1 월 사용 요금:  25200
2월 통화 시간(분)을 입력하세요: 120
2 월 통화 시간:  120
2 월 사용 요금:  14400
···
10월 통화 시간(분)을 입력하세요: 170
10 월 통화 시간:  170
10 월 사용 요금:  20400
11월 통화 시간(분)을 입력하세요: 175
11 월 통화 시간:  175
11 월 사용 요금:  21000
12월 통화 시간(분)을 입력하세요: 195
12 월 통화 시간:  195
12 월 사용 요금:  23400
1년 동안의 통화 시간:  2044
1년 동안의 사용 요금:  245280
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 4,
        "problem_level": 3,
        "problem_answer": """```python
dan = input("구구단 몇단을 출력할까요? ")
check = "23456789"

if dan in check:
    for i in range(1, 10):
        print(dan, "x", i, "=", int(dan)*i)
else:
    print("입력값이 잘못되었습니다.")
```""",
        "problem_question": """구구단의 단(2단 ~ 9단)을 입력받고 해당 단의 구구단을 출력하는 프로그램을 파이썬으로 작성하세요.""",
        "problem_content": """""",
        "problem_result": """```text
[입력]
구구단 몇단을 출력할까요? 0

[출력]
입력값이 잘못되었습니다.
```

```text
[입력]
구구단 몇단을 출력할까요? a

[출력]
입력값이 잘못되었습니다.
```
```text
[입력]
구구단 몇단을 출력할까요? 3

[출력]
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
```

```text
[입력]
구구단 몇단을 출력할까요? 7

[출력]
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
    {
        "object_idx": 4,
        "problem_level": 3,
        "problem_answer": """```python
data = ["3", "apple", "5", "I", "python", "be", "7", "love"]

for i in data:
    if i.isdigit():
        if int(i) % 3 == 0:
            print(int(i) * 5)
        else:
            print(int(i) + 10)
    else:
        if len(i) > 3:
            print(i.upper())
```""",
        "problem_question": """다음과 같은 파이썬 리스트가 있다. 파이썬 반복 제어문을 사용해서 해당 리스트의 모든 원소를 탐색한 후 아래 조건에 따라 출력하는 파이썬 코드를 작성하세요.""",
        "problem_content": """```text
data = ["3", "apple", "5", "I", "python", "be", "7", "love"]
```

조건

- 리스트 원소의 값이 숫자일 때, 숫자가 3의 배수이면 5를 곱해서 출력한다.
- 리스트 원소의 값이 숫자일 때, 숫자가 3의 배수가 아니면 10을 더해서 출력한다.
- 리스트 원소의 값이 문자열일 때, 문자열의 길이가 4 이상인 문자열을 대문자로 바꿔서 출력한다.

(hint)

- len() 매서드는 문자열의 길이를 알 수 있습니다. (len("ABC") 는 3입니다.)
- isdigit() 매서드는 문자가 숫자인지 아닌지 체크합니다.(숫자이면 True)
- upper() 매서드는 문자열을 대문자료 변경합니다.""",
        "problem_result": """```text
15
APPLE
15
PYTHON
17
LOVE
```""",
        "level_3_initcodes": """```python
# 코드를 완성하세요

```""",
    },
]

classroom_list_dump = [
    {
        "idx": 1,
        "title": "변수와 자료형의 이해와 활용",
        "object_idx": 1,
        "previous_classroom_idx": 0,
        "level_1_problems": [1, 2, 3, 4],
        "level_2_problems": [6, 7, 8, 9],
        "level_3_problems": [11, 12],
    },
    {
        "idx": 2,
        "title": "연산자의 이해와 활용",
        "object_idx": 2,
        "previous_classroom_idx": 1,
        "level_1_problems": [16, 17, 18, 19],
        "level_2_problems": [21, 22, 23, 24],
        "level_3_problems": [26, 27],
    },
    {
        "idx": 3,
        "title": "선택 제어문의 이해와 활용",
        "object_idx": 3,
        "previous_classroom_idx": 2,
        "level_1_problems": [31, 32, 33, 34],
        "level_2_problems": [36, 37, 38, 39],
        "level_3_problems": [41, 42],
    },
    {
        "idx": 4,
        "title": "반복 제어문의 이해와 활용",
        "object_idx": 4,
        "previous_classroom_idx": 3,
        "level_1_problems": [46, 47, 48, 49],
        "level_2_problems": [51, 52, 53, 54],
        "level_3_problems": [56, 57],
    },
]

my_classroom_list_dump = [
    {
        "idx": 1,
        "userid": "user1",
        "classroom_idx": 1,
        'created_at': '2024-02-25 11:11:11',
        'updated_at': '',
    },
    {
        "idx": 2,
        "userid": "user1",
        "classroom_idx": 3,
        'created_at': '2024-03-25 11:11:11',
        'updated_at': '',
    },
    {
        "idx": 3,
        "userid": "user2",
        "classroom_idx": 3,
        'created_at': '2024-03-25 11:11:11',
        'updated_at': '',
    },
    {
        "idx": 4,
        "userid": "user1",
        "classroom_idx": 4,
        'created_at': '2024-04-25 11:11:11',
        'updated_at': '',
    },
]

with open("subject_list_dump.pickle", "wb") as f:
    pickle.dump(subject_list_dump, f, pickle.HIGHEST_PROTOCOL)

with open("object_list_dump.pickle", "wb") as f:
    pickle.dump(object_list_dump, f, pickle.HIGHEST_PROTOCOL)

with open("problem_list_dump.pickle", "wb") as f:
    pickle.dump(problem_list_dump, f, pickle.HIGHEST_PROTOCOL)

with open("classroom_list_dump.pickle", "wb") as f:
    pickle.dump(classroom_list_dump, f, pickle.HIGHEST_PROTOCOL)

with open("my_classroom_list_dump.pickle", "wb") as f:
    pickle.dump(my_classroom_list_dump, f, pickle.HIGHEST_PROTOCOL)
