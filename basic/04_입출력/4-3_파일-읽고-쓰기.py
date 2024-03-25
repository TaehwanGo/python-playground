# 4-3. 파일 읽고 쓰기

# 파일 생성하기
# f = open("새파일.txt", 'w')
# f.close()

'''
open : 파이썬 내장 함수
파일_객체 = open(파일 이름, 파일 열기 모드)

파일 열기모드
r : 읽기모드 - 파일을 읽기만 할 때 사용
w : 쓰기모드 - 파일에 내용을 쓸 때 사용
a : 추가모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용
'''

# 파일을 쓰기 모드로 열어 내용 쓰기

# f = open("새파일.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# 비교 - print vs write
# for i in range(1, 11):
#     print("%d번째 줄입니다." % i)

'''
차이: 모니터 화면에 출력하는 것 vs 파일에 기록하는 것
'''

# 파일을 읽는 여러 가지 방법

# readline() 함수 이용하기
# f = open("새파일.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

# 만약 모든 줄을 읽어 화면에 출력하고 싶다면
# f = open("새파일.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# readlines 함수 사용하기
# f = open("새파일.txt", 'r')
# lines = f.readlines()
# # print(lines)  // ["1번째 줄입니다.\n", "2번째 줄입니다.\n", ..., "10번째 줄입니다.\n"]
# for line in lines:
#     print(lines)
# f.close()

# read 함수 사용하기
# f = open("새파일.txt", 'r')
# data = f.read()
# print(data)
# f.close()

'''
f.read()는 파일의 내용 전체를 문자열로 돌려준다.
'''

# 파일 객체를 for 문과 함께 사용하기

# f = open("새파일.txt", 'r')
# # print(f)
# for line in f:
#     print(line)
# f.close()

'''
파일 객체(f)는 기본적으로 위와 같이 for문과 함께 사용하여 파일을 줄 단위로 읽을 수 있다
'''

# 파일에 새로운 내용 추가하기
# f = open("새파일.txt", 'a')  # 'a' : 추가모드
# for i in range(11, 20):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# with문과 함께 사용하기
# 열고 닫는 것을 자동으로 처리할 수 있다면 편리하지 않을까?
with open("foo.txt", 'w') as f:
    f.write("Life is too short, you need python")

'''
위와 같이 with 문을 사용하면 with블록(with문에 속해 있는 문장)을 벗어나는 순간
열린 파일 객체 f가 자동으로 close 된다.
'''