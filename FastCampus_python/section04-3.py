# 리스트
# 파이썬 데이터 타입(자료형)

# 리스트 (순서, 중복, 수정, 삭제 가능)

a = []
b = list()
c = [1,2,3,4]
d = [10,100,'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:2])
print(e[2][1:3])  # e의 두번째의 0뛰고 1부터 3까지인데 2까지만있으니 두개 출력

# 연산
print(c+d)
print(c*3)
print(str(c[0])+'hi')


# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a','b','c']
print(c)

del c[1]
print(c)
del c[-1]
print(c)

# 리스트 함수
y = [5,2,3,1,4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2,7) # 2번 인덱스에 7 추가
print(y)
y.remove(2) # 값 2를 지움 2번인덱스를 지우는건 del
y.remove(7)
print(y)
y.pop() # LIFO
print(y)
ex = [88,77]
y.extend(ex)
print(y)

# 삭제 : del, remove, pop 


# 튜플 (순서, 중복 가능,   수정X, 삭제X)

a = ()
b = (1,)
c = (1,2,3,4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][0:2])

print(c+d)
print(c*3)
print()

# 튜플 함수

z = (5,2,1,3,1)

print(z)
print(3 in z)
print(z.index(5)) # 내가 찾고자하는 값의 인덱스를 출력
print(z.count(1))