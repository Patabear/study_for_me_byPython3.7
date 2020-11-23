# 파이썬 기본코딩 print함수 사용

print('Hello Python!')
print("Hello Python!")
print('''Hello Python!''')
print("""Hello Python!""")

print()

# Seperator 옵션 사용

print('T', 'E', 'S', 'T', sep=' ')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')


# end 옵션 사용

print('Welcom To', end=' ')
print('the black parade', end=' ')
print('piano notes')


# format 사용 [] , {} , ()

print('{} and {}'.format('You','Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} are {b}".format(a='You', b='Me'))
print("%s's favorite number is %d" % ('HeeJung', 7)) # %s : 문자, %d : 정수, %f : 실수

print("Test1: %5d, Price: %4.2f" % (776, 6545.123))
print("Test1: {0: 5d}, Price:{1: 4.2f}".format(776,6534.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.123))



print("'print")
print('\'\'you\'')
print("""'you'""")
print('\tyou\nme')