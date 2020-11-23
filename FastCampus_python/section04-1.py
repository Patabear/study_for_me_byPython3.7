# 데이터 타입

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "kim",
    "age" : 25
}
v_list = [3,5,7]
v_tuple = 3, 5, 7
v_set = {7,8,9}

print(type(v_tuple))
print(type(v_set))
print(type(v_float))


i1 = 39
i2 = 939
big_int1 = 9999999999999999999999999999999999999999999
big_int2 = 7777777777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2)
result = f3 + i2
print(result, type(result))

a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a+b
print(result2)

# 형변환

print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))

# 단항 연산자

y = 100
y += 100
print(y)
y *= 100
print(y)

print(abs(-7)) # 절대값
n ,m = divmod(100,8)
print(n, m)

import math

print(math.ceil(5.1)) # 가까운 위의정수
print(math.floor(3.873)) # 가까운 아래의 정수

# // 나누기(몫)
# ** 지수(제곱)