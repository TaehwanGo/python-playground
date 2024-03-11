# 딕셔너리
# 대응 관계를 나타내는 자료형
# 연관 배열(Associative array) 또는 해시(Hash)라고도 한다.

# 기본 딕셔너리의 모습
# {Key1:Value1, Key2:Value2, Key3:Value3, ...}

a = {1: "hi"}
print(a)

# 딕셔너리 쌍 추가하기
a[2] = "hello"
print(a)

a["name"] = "pey"
print(a)

# 딕셔너리 요소 삭제하기
del a[1]  # 자바스크립트 delete와 비슷
print(a)

# 딕셔너리 주의사항
# 딕셔너리에서 Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다.
a = {1: "a", 1: "b"}
print(a)  # {1: 'b'}

# 딕셔너리 키로 리스트는 사용할 수 없다. 하지만 튜플은 사용할 수 있다.

# 딕셔너리 관련 함수들
# Key 리스트 만들기(keys)
a = {"name": "pey", "phone": "0119993323", "birth": "1118"}
print(a.keys())  # dict_keys(['name', 'phone', 'birth'])
# dict_keys 객체를 리스트로 변환하려면 다음과 같이 하면 된다.
print(list(a.keys()))  # ['name', 'phone', 'birth']

# Value 리스트 만들기(values)
print(a.values())  # dict_values(['pey', '0119993323', '1118'])

# Key, Value 쌍 얻기(items)
print(
    a.items()
)  # dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')]) # 튜플로 묶여서 리스트로 반환
print(
    list(a.items())
)  # [('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')] # 리스트로 변환

# Key: Value 쌍 모두 지우기(clear)
a.clear()
print(a)  # {}

# Key로 Value 얻기(get)
a = {"name": "pey", "phone": "0119993323", "birth": "1118"}
print(a.get("name"))  # pey

# Key로 Value 얻기(get) - 없는 키로 값을 가져오려고 할 때
print(a.get("nokey"))  # None
# print(a['nokey']) # KeyError: 'nokey'
print(a.get("foo", "bar"))  # bar # 디폴트 값 설정
print(a.get("nokey") == None)  # True

# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
print("name" in a)  # True
print(("name" in a) == True)  # True
print("email" in a)  # False
# python은 True, False를 대문자로 쓴다. true, false는 사용하지 않는다.
