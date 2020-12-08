# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r , 쓰기 모드(기존파일삭제) : w , 추가모드(파일생성 또는 추가) : a
# .. : 상대경로, . : 절대경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open

# 파일 읽기
# 예제1 이거 왜 안돼 슈바..
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)