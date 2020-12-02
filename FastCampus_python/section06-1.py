# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요

# 예제1
def hello(world):
    print("Hello", world)

hello("Python")
hello(7777)


# 예제2
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("Python!!!!!")
print(str)

# 예제3-1(다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(type(val1), val1, val2, val3)

# 예제3-2(데이터 타입 반환)
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

lt = func_mul2(100)
print(lt, type(lt))

# 예제4
# *args, *kwargs

# args  * 은 튜플 형태로 넘어감
def args_func(*args):
    # for t in args:
    #     print(t)
    for i,v in enumerate(args):
        print(i, v)

args_func('kim')
args_func('kim', 'Park')
args_func('kim', 'Park', 'Lee')

# kwargs  ** 은 딕셔너리 형태로 넘어감
def kwargs_func(**kwargs):
    for k,v in kwargs.items():
        print(k, v)

kwargs_func(name1 = 'Kim', name2 = 'Park', name3 = 'Lee')
kwargs_func(name1 = 'Kim')


# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', 'kim', age1=24, age2=35)

# 중첩함수(클로저)
# 데코레이터
def nested_func(num):
    def func_in_func(arg):
        print('>>>',arg)
    print("in func")
    func_in_func(num+10000)

nested_func(10000)
