# 자료형의 값을 저장하는 공간, 변수

# 변수를 만들 때는 =을 사용한다.
# 변수명 = 변수에 저장할 값

# 리스트를 복사하고자 할 때
# a = [1, 2, 3]
# b = a
# print(id(a))
# print(id(b)) # a와 b의 주소값이 같다
# print(a is b)  # a와 b가 가리키는 객체는 동일한가? True
# a[1] = 4
# print(a)  # [1, 4, 3]
# print(b)  # [1, 4, 3]

# b 변수를 생성할 때 a 변수의 값을 가져오면서 a와는 다른 주소를 가리키도록 만드는 방법
# 1. [:] 이용
# a = [1, 2, 3]
# b = a[:]
# a[1] = 4
# print(a)  # [1, 4, 3]
# print(b)  # [1, 2, 3]

# 2. copy 모듈 이용
# from copy import copy

# a = [1, 2, 3]
# b = copy(a)  # b = a[:]와 동일
# a[1] = 4
# print(a)  # [1, 4, 3]
# print(b)  # [1, 2, 3]

# copy함수 사용하기
# a = [1, 2, 3]
# b = a.copy()
# print(b is a)  # False

# 쉽게 변수 바꾸기
# a = 3
# b = 5
# a, b = b, a
# print(a)  # 5
# print(b)  # 3
