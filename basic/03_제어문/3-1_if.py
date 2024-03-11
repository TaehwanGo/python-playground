# if 문
"""
if 조건:
    실행문
elif 조건:
    실행문
else:
    실행문
"""
"""
비교 연산자
x < y : x가 y보다 작다
x > y : x가 y보다 크다
x == y : x와 y가 같다
x != y : x와 y가 다르다
x >= y : x가 y보다 크거나 같다
x <= y : x가 y보다 작거나 같다
"""
pocket = ["paper", "cellphone"]
card = True
if "money" in pocket:
    print("현금으로 택시 타기")
elif card:
    print("신용카드로 택시 타기")
else:
    print("걷기")
# 신용카드로 택시 타기 출력 됨
