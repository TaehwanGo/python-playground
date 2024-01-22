# 문자열을 만드는 방법
# 1. 큰 따옴표(")로 양쪽 둘러싸기
# 2. 작은 따옴표(')로 양쪽 둘러싸기
# 3. 큰 따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
# 4. 작은 따옴표 3개를 연속(''')으로 써서 양쪽 둘러싸기

# a = "Hello World a"
# b = 'Hello World b'
# c = """Hello World
# c
# """
# d = '''Hello World
# d'''

# print(a)
# print(b)
# print(c)
# print(d)

# ''' 또는 """ 를 이용하면 여러 줄에 걸쳐서 문자열을 표현할 수 있다.

# 이스케이프 코드 : 특수한 의미를 가진 문자를 표현할 때 사용한다.
# \n : 문자열 안에서 줄을 바꿀 때 사용
# \t : 문자열 사이에 탭 간격을 줄 때 사용
# \\ : 문자 \를 그대로 표현할 때 사용
# \' : 작은 따옴표(')를 그대로 표현할 때 사용
# \" : 큰 따옴표(")를 그대로 표현할 때 사용
# \r : 캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
# \f : 폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
# \a : 벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)
# \b : 백 스페이스
# \000 : 널 문자
# 이 중에서 활용 빈도가 높은 것은 \n, \t, \\, \', \" 이다.

# 문자열 인덱싱과 슬라이싱
# 인덱싱 : 가리킨다는 의미
# 슬라이싱 : 잘라낸다는 의미

# 인덱싱 예시
# a = "Life is too short, You need Python"
# print(a[3]) # e

# 슬라이싱 예시
# a = "Life is too short, You need Python"
# print(a[0:4]) # Life
# 슬라이싱 기법은 뒤에서 배울 자료형인 리스트나 튜플에서도 사용할 수 있다.

# a[시작_번호:끝_번호]에서 끝 번호 부분을 생략하면 시작 번호부터 그 문자열의 끝까지 뽑아 낸다.
# print(a[19:]) # You need Python

# a[시작_번호:끝_번호]에서 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 뽑아 낸다.
# print(a[:17]) # Life is too short

# a[시작_번호:끝_번호]에서 시작 번호와 끝 번호를 생략하면 문자열의 처음부터 끝까지 뽑아 낸다.
# print(a[:]) # Life is too short, You need Python

# 슬라이싱에서도 인덱싱과 마찬가지로 -(빼기) 기호를 사용할 수 있다.
# print(a[19:-7]) # You need

# 슬라이싱으로 문자열 나누기
# a = "20230331Rainy"
# date = a[:8]
# weather = a[8:]
# print(date) # 20230331
# print(weather) # Rainy

# 문자열 포매팅 따라 하기
# 1. 숫자 바로 대입
# print("I eat %d apples." % 3) # I eat 3 apples.

# 2. 문자열 바로 대입
# print("I eat %s apples." % "five") # I eat five apples.

# 3. 숫자 값을 나타내는 변수로 대입
# number = 3
# print("I eat %d apples." % number) # I eat 3 apples.

# 4. 2개 이상의 값 넣기
# number = 10
# day = "three"
# print("I ate %d apples. so I was sick for %s days." % (number, day)) # I ate 10 apples. so I was sick for three days.

# 문자열 포맷 코드
# %s : 문자열(String)
# %c : 문자 1개(character)
# %d : 정수(Integer)
# %f : 부동소수(floating-point)
# %o : 8진수
# %x : 16진수
# %% : Literal % (문자 % 자체)

# 여기에서 재미있는 것은 %s 포맷 코드인데, 이 코드에는 어떤 형태의 값이든 변환해 넣을 수 있다.
# print("I have %s apples" % 3) # I have 3 apples
# print("rate is %s" % 3.234) # rate is 3.234

# %를 나타내려면 반드시 %%를 써야 한다
# print("Error is %d%%." % 98) # Error is 98%.

# 포맷 코드와 숫자 함께 사용하기
# 1. 정렬과 공백
# print("%10s" % "hi") #         hi # 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨 두라는 의미이다.
# print("%-10sjane." % "hi") # hi         jane. # 전체 길이가 10개인 문자열 공간에서 대입되는 값을 왼쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨 두라는 의미이다.

# 2. 소수점 표현하기
# print("%0.4f" % 3.42134234) # 3.4213 # 소수점 네 번째 자리까지만 나타내고 싶은 경우에는 위와 같이 사용한다.
# print("%10.4f" % 3.42134234) #     3.4213 # 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 소수점 네 번째 자리까지만 표시하라는 의미이다.
# print("%0.2f" % 3.6666) # 3.67 # 소수점 둘째 자리까지만 표시하라는 의미이다. - 반올림해서 표시된다.

# format 함수를 사용한 포매팅
# 숫자 바로 대입하기
# print("I eat {0} apples".format(3)) # I eat 3 apples
# print("I eat {0} apples".format("five")) # I eat five apples

# 2개 이상의 값 넣기
# number = 10
# day = "three"
# print("I ate {0} apples. so I was sick for {1} days.".format(number, day)) # I ate 10 apples. so I was sick for three days.

# 이름으로 넣기
# print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)) # I ate 10 apples. so I was sick for 3 days.

# 인덱스와 이름을 혼용해서 넣기
# print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3)) # I ate 10 apples. so I was sick for 3 days.

# TODO : 왼쪽 정렬 부터 이어서 하기