# 4-1. 함수
## 파이썬 함수의 구조

'''
def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
    ...
# def는 함수를 만들 때 사용하는 예약어이며, 함수명은 함수를 만드는 사람이 임의로 만들 수 있다.
'''

# def add(a, b):  # a, b는 매개변수(parameter)
#     return a + b

# print(add(3, 4))  # 3, 4는 인수(argument)

## 매개변수를 지정하여 호출하기
# def sub(a, b):
#     return a - b

# print(sub(a=3, b=7))  # a에 3, b에 7을 전달 -> 3 - 7 = -4
# print(sub(b=3, a=7))  # b에 3, a에 7을 전달 -> 7 - 3 = 4
# - 매개변수를 지정하면 순서에 상관없이 사용 가능

## 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
'''
def 함수이름(*매개변수):  # *args와 같이 사용
    <수행할 문장>
    ...
'''
## 여어 개의 입력값을 받는 함수 만들기
# def add_many(*args):  # *args는 입력값을 전부 모아서 튜플로 만들어 준다.
#     result = 0
#     for i in args:
#         result = result + i
#     return result

# print(add_many(1, 2, 3))  # 1 + 2 + 3 = 6

# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result
# print(add_mul("add", 1, 2, 3, 4, 5))  # 1 + 2 + 3 + 4 + 5 = 15
# print(add_mul("mul", 1, 2, 3, 4, 5))  # 1 * 2 * 3 * 4 * 5 = 120

## 키워드 매개변수
# - 키워드 파라미터를 사용할 때는 매개변수 앞에 별 두 개(**)를 붙인다.
# def print_kwargs(**kwargs):
#     print(kwargs)

# print_kwargs(a=1)  # {'a': 1}
'''
함수의 입력값으로 a=1이 사용되면 {'a': 1}이라는 딕셔너리가 만들어진다.
'''

## 함수의 결과값은 언제나 하나이다.
def add_and_mul(a, b):
    return a + b, a * b  # return의 결과값은 튜플값 하나로 돌려준다.
print(add_and_mul(3, 4))  # (7, 12)

# return은 함수를 빠져나갈 때에도 사용할 수 있다.

## 매개변수에 초깃값 미리 설정하기