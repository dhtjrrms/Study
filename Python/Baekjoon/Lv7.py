# 7단계 문제풀이

# 1번 2738
'''
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

Matrix1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    Matrix1.append(row)

Matrix2 = []
for _ in range(n):
    row = list(map(int, input().split()))
    Matrix2.append(row)

result = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(Matrix1[i][j] + Matrix2[i][j])
    result.append(row)

for row in result:
    print(' '.join(map(str, row)))
'''

# 2번 2566
'''
import sys
input = sys.stdin.readline

A = []

for _ in range(9):
    row = list(map(int, input().split()))
    A.append(row)

max_value = -1
max_position = (0,0)

for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j] > max_value:
            max_value = A[i][j]
            max_position = (i,j)

print(max_value)
print(max_position[0]+1, max_position[1]+1)
'''

# 3번 10798
'''
lines = []
for _ in range(5):
    lines.append(input())

result = ''

max_length = max(len(lines) for lines in lines)

for i in range(max_length):
    for line in lines:
        if i < len(line):
            result += line[i]

print(result)
'''

# 4번 2563
