# 불 자료형 - True, False
# - 불 자료형은 참과 거짓을 나타내는 자료형이다.
# - True와 False 두 가지 값만을 가질 수 있다.
# - True, False는 파이썬의 예약어로 true, false와 같이 작성하면 안되고 첫 문자를 항상 대문자로 작성해야 한다

# 불 자료형은 어떻게 사용할까?
# a = True
# b = False
# print(type(a))  # <class 'bool'>

# 불 자료형은 조건문의 반환 값으로도 사용된다.
# print(1 == 1)  # True
# print(2 > 1)  # True
# print(2 < 1)  # False

# 자료형의 참과 거짓
# print(bool("python"))  # True
# print(bool(""))  # False
# print(bool([1, 2, 3]))  # True
# print(bool([]))  # False
# print(bool((1, 2, 3)))  # True
# print(bool(()))  # False
# print(bool({'a': 1}))  # True
# print(bool({}))  # False
# print(bool(1))  # True
# print(bool(0))  # False
# print(bool(None))  # False

# a = [1,2,3,4]
# while a:
#     print(a.pop())

# if []:
#     print("참")
# else:
#     print("거짓")

# 불 연산
# - 참 거짓 판별
print(bool(1))
