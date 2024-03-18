# 4-2. 사용자 입출력
# python3 ./basic/04_입출력/4-2_사용자입출력.py

# 사용자 입력 활용하기
# - 사용자가 입력한 값을 어떤 변수에 대입하고 싶을 때 input() 함수를 사용한다.

# a = input()
# print(a)

# 프롬프트를 띄워 사용자 입력받기
# - input()의 괄호 안에 질문을 입력하여 프롬프트를 띄울 수 있다.
# - input("안내 문구")
# number = input("숫자를 입력하세요: ")
# print(number)

# 큰 따옴표로 둘러싸인 문자열은 + 연산과 동일하다.
# print("life" "is" "too short")
# print("life"+"is"+"too short")

# 문자열 띄어쓰기는 콤마로 한다.
# print("life", "is", "too short") # life is too short

# 한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end = ' ')  # end = ' ' : print 함수는 두 번째 줄로 넘어가지 않고 그 줄에 계속해서 출력하게 한다.
# 한 줄에 결괏값을 계속 이어서 출력하려면 매개변수 end를 사용해 끝 문자를 지정해야 한다.