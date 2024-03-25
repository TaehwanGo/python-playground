# 4-4. 프로그램의 입출력

'''
명령 프롬프트를 사용해 본 독자라면 다음과 같은 일을 해 본 적이 있을 것이다.

type a.txt

type은 바로 뒤에 적힌 파일 이름을 인수로 받아 해당 파일의 내용을 출력해 주는 명령어 이다.

cat 아닌가? 라고 생각하는 독자도 있을 것이다. 맞다. 유닉스 계열의 운영체제에서는 cat이라는 명령어를 사용한다. 하지만 윈도우에서는 type을 사용한다.
'''

# 이러한 기능을 파이썬 프로그램에도 적용할 수 있다

# sys 모듈 사용하기

# sys 모듈을 사용하여 프로그램에 인수를 전달할 수 있다

import sys

# args = sys.argv[1:]
# for i in args:
#     print(i)

'''
위 프로그램 실행 시 전달받은 인수를 for 문으로 차례대로 하나씩 출력하는 예이다

python3 /Users/gotaehwan/projects/python-playground/basic/04_입출력/4-4_프로그램의-입출력.py aaa bbb ccc

위와 같이 실행하면 aaa, bbb, ccc가 차례대로 출력된다
'''

args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')

'''
python3 /Users/gotaehwan/projects/python-playground/basic/04_입출력/4-4_프로그램의-입출력.py life is too short, you need python

위와 같이 실행하면 LIFE IS TOO SHORT, YOU NEED PYTHON이 출력된다
'''
