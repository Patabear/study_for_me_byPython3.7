input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
# ord는 아스키코드값을 반환

steps = [ (-2,-1), (-1,-2), (-2,1), (1,-2), (-1,2), (2,-1), (1,2), (2,1) ]
count = 0

for step in steps:
    next_row = step[0] + row
    next_column = step[1] + column
    if 1 <= next_row and next_row <= 8 and 1 <= next_column and next_column <= 8:
        count += 1

print(count)