# while 문
"""
while 조건:
    실행문
    실행문
"""
# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     # treeHit++  # 파이썬에서는 지원하지 않음, treeHit += 1로 사용은 가능
#     print("나무를 %d번 찍었습니다." % treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다.")

# while문 만들기
# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit
# Enter number: """
# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())  # input()은 사용자 입력을 받는 함수

# while문 강제로 빠져나가기
# coffee = 10
# money = 0
# while True:
#     money = money + int(input("돈을 넣어 주세요: "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee - 1
#         money = money - 300
#         print("남은 돈은 %d원 입니다." % money)
#         print("남은 커피의 양은 %d개 입니다." % coffee)
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
#         coffee = coffee - 1
#         money = money - 300
#         print("남은 돈은 %d원 입니다." % money)
#         print("남은 커피의 양은 %d개 입니다." % coffee)
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 돈은 %d원 입니다." % money)
#         print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         print("남은 돈은 %d원 입니다." % money)
#         break
