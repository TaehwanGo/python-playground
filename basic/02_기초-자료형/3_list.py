# 리스트 자료형
# 리스트명 = [요소1, 요소2, 요소3, ...]
# odd = [1, 3, 5, 7, 9]
# a = list() # 빈 리스트
# a = [1, 2, 3]
# print(a[-1]) # 3 => -1은 뒤에서부터 세어 첫 번째 요소를 나타냄
# a = [1, 2, 3, ['a', 'b', 'c']]
# print(a[-1][1]) # b
# 리스트를 중첩으로 사용하는 것은 혼란스럽기 때문에 자주 사용하지는 않음

# 리스트의 슬라이싱
# a = [1, 2, 'a', 4, 5]
# print(a[0:2]) # [1, 2] => 인덱스0부터 2번째 요소까지
# print(a[1:2]) # [2] => 인덱스1부터 2번째 요소까지

# 리스트 연산자
# 리스트 더하기(+)
# a = [1, 2, 3]
# b = [3, 4, 5]
# print(a + b) # [1, 2, 3, 3, 4, 5]

# 리스트 반복하기(*)
# a = [1, 2, 3]
# print(a * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 리스트 길이 구하기
# a = [1, 2, 3]
# print(len(a)) # 3

# 초보자가 범하기 쉬운 리스트 연산 오류
# a = [1, 2, 3]
# print(a[2] + 'hi') # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 정수와 문자열은 더할 수 없음
# print(str(a[2]) + 'hi') # 3hi

# 리스트의 수정과 삭제
# 리스트에서 값 수정하기
# a = [1, 2, 3]
# a[2] = 4
# print(a) # [1, 2, 4]

# del 함수 사용해 리스트 요소 삭제하기
# a = [1, 2, 3]
# del a[1]
# print(a) # [1, 3]

# 슬라이싱 기법을 사용하여 리스트의 요소 여러 개를 한꺼번에 삭제하기
# a = [1, 2, 3, 4, 5]
# del a[2:]
# print(a) # [1, 2]

# 리스트 관련 함수들
# 리스트에 요소 추가(append)
# a = [1, 2, 3]
# a.append(4)
# print(a) # [1, 2, 3, 4]
# a.append([5, 6])
# print(a) # [1, 2, 3, 4, [5, 6]]

# 리스트 정렬(sort)
# a = [1, 4, 3, 2]
# a.sort()
# print(a) # [1, 2, 3, 4]

# a = [1, 11, 10, 9]
# a.sort()
# print(a) # [1, 9, 10, 11]

# a = ['a', 'c', 'b']
# a.sort()
# print(a) # ['a', 'b', 'c']

# 리스트 뒤집기(reverse)
# a = ['a', 'c', 'b']
# a.reverse()
# print(a) # ['b', 'c', 'a']

# 위치 반환(index(x)) - 리스트에 x라는 값이 있으면 x의 위치 값을 돌려줌
# a = [1, 2, 3]
# print(a.index(3)) # 2
# print(a.index(1)) # 0
# a.index(0) # ValueError: 0 is not in list
# print(a.find(3)) # AttributeError: 'list' object has no attribute 'find' - find 함수는 문자열에서만 사용 가능

# 리스트에 요소 삽입(insert)
# a = [1, 2, 3]
# a.insert(0, 4) # a[0] 위치에 4를 삽입
# print(a) # [4, 1, 2, 3]

# 리스트 요소 제거(remove)
# a = [1, 2, 3, 1, 2, 3]
# a.remove(3) # 처음 나오는 3을 삭제
# print(a) # [1, 2, 1, 2, 3]

# 리스트 요소 끄집어내기(pop)
# a = [1, 2, 3]
# print(a.pop()) # 3
# print(a) # [1, 2]

# 리스트에 포함된 요소 x의 개수 세기(count)
# a = [1, 2, 3, 1]
# print(a.count(1)) # 2 - 1이라는 값이 리스트 a에 2개 들어있음

# 리스트 확장(extend) - push와 비슷
# a = [1, 2, 3]
# a.extend([4, 5])
# print(a) # [1, 2, 3, 4, 5]
