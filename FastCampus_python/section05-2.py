# Section 05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
while v1<11:
    print("v1 is :", v1)
    v1 += 1

for v2 in range(10):
    print("v2 is :", v2) # 0~9

for v3 in range(1,11):
    print("v3 is :", v3) # 1~11


# 1~100 합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1~100 : ', sum1)
print('1~100 : ', sum(range(1,101))) # list를 받아서 합을구함 = sum
print('1~100 : ', sum(range(1,101,2))) # 1~100 2씩 건너뛰며 더함


# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable : range, reverse, enumerate, filter, map, zip

names = ["Kim", "Park", "Cho", "Choi", "Yoo"]

for v in names:
    print("You are : ", v)

word = "dreams"

for s in word:
    print("Word : ", s)


my_info = {
    "name": "Kim",
    "age" : 33,
    "city": "Seoul"
}

# 기본값은 키
for key in my_info:
    print("my_info", key)

# 값
for key in my_info.values():
    print("my_info", key)

# 키
for key in my_info.keys():
    print("my_info", key)

# 키 and 값
for k, v in my_info.items():
    print("my_info", k, v)

name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())


# break
numbers = [14,3,4,7,10,24,17,2,33,15,34,36,38]

# for - else 구문  for문 내에 break 미실행시 else 실행 = 온전히 반복문을 다 돌았다
for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found : 33!")
else:
    print("Not found 33......")


# continue

It  = ["1", 2, 5, True, 4.3, complex(4)]

for v in It:
    if type(v) is float:
        continue
    print("타입 : ", type(v))

