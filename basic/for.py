# for 문
"""
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...

- 리스트나 튜플, 문자열의 첫 번째 요소부터 마지막 요소까지 차례로 변수에 대입되어 "수행할 문장1", "수행할 문장2" 등이 수행된다.
"""

# 1. 전형적인 for
# test_list = ['one', 'two', 'three']
# for I in test_list:
#     print(i)

# 2. 다양한 for 사용
# a = [(1, 2), (3, 4), (5, 6)]
# for (first, last) in a:
#     print(first + last)
# - 위 예는 리스트 a의 요소값이 튜플이기 때문에 각각의 요소들이 자동으로 (first, last)라는 변수에 대입된다.
# - 이 예는 각 튜플의 합인 3, 7, 11이라는 결과값을 출력한다.

# 3. for 문의 응용

"""
총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다.
합격, 불합격 결과를 보여 주시오.
"""
# marks = [90, 25, 67, 45, 80]
# number = 0
# for score in marks:
#     if score >= 60:
#         print("%d번 학생은 합격입니다." % (number + 1))
#     else:
#         print("%d번 학생은 불합격입니다." % (number + 1))

# for 문과 continue

# marks = [90, 25, 67, 45, 80]
# number = 0
# for score in marks:
#     number = number + 1
#     if score < 60:
#         continue
#     print("%d번 학생 축하합니다. 합격입니다. " % number)

# for 문과 함께 자주 사용하는 range 함수
# a = range(10)  # 0부터 10 미만의 숫자를 포함하는 range 객체를 만들어 준다.
# print(a)  # range(0, 10)
#
# marks = [90, 25, 67, 45, 80]
# for number in range(len(marks)):
#     if marks[number] < 60:
#         continue
#     print("%d번 학생 축하합니다. 합격입니다." % (number + 1))

# for와 range를 이용한 구구단
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i * j, end=" ")
#     print("")  # print()는 줄바꿈

# # 리스트 컴프리헨션 사용하기
# a = [1, 2, 3, 4]
# result = []
# for num in a:
#     result.append(num * 3)
# print(result)  # [3, 6, 9, 12]

result = [x*y for x in range(2, 10)
            for y in range(1, 10)]
print(result)