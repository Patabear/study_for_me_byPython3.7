# Section 07-1
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 떄 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인슨턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명:
#     함수
#     함수
#     함수


# 예제1
class UserInfo:
    def __init__(self, name):  # 매직 메소드
        self.name = name
    def user_info_p(self):
        print("Name : ", self.name)

# 네임스페이스
user1 = UserInfo("Kim")
user1.user_info_p()
user2 = UserInfo("Park")
user2.user_info_p()

print(id(user1)) # 메모리 주소값
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)


# 예제2
# self의 이해
class SelfTest():
    def function1(): # self 인자 없으므로 인스턴스에서 출력X
        print('function1 called!')
    def function2(self):
        print(id(self))
        print('function2 called!')

self_test = SelfTest()
# self_test.function1()  - 실행안됨
SelfTest.function1()

self_test.function2()

print(id(self_test))
SelfTest.function2(self_test)


# 예제3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수 - 모든 인스턴스가 공유
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1
    

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)

print(user1.name)
print(user2.name)
print(user3.name)

# 자기 네임스페이스에 없으면 클래스의
print(user1.stock_num)