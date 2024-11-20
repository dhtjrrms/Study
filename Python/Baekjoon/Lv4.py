# 4번 문제풀이

# 1번 10807
'''
import sys
ArrayCount = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
FindNum = int(sys.stdin.readline())
count = array.count(FindNum)

print(count)
'''

# 2번 10871
'''
import sys
ArrayNum, ThanSmaller = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

for num in array:
    if num < ThanSmaller:
        print(num, end=' ')
'''

# 3번 10818
'''
import sys
Case = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

min = min(array)
Max = max(array)

print(min, Max)
'''

# 4번 2562
'''
import sys

Max_value = -1
Max_index = -1

for i in range(1, 10):
    num = int(input().strip())

    if num > Max_value:
        Max_value = num
        Max_index = i

print(Max_value)
print(Max_index)
'''    

# 5번 10810
'''
import sys
input = sys.stdin.readline

Case, throwin = map(int, input().split())

baskets = [0] * (Case+1)

for _ in range(throwin):
    start, last, putin = map(int, input().split())
    for index in range(start, last+1):
        baskets[index] = putin

for count in baskets[1:]:
    print(count, end=' ')
'''

# 6번 10813
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

baskets = list(range(1, n+1))

def swap_positions(baskets, i, j):
    baskets[i], baskets[j] = baskets[j], baskets[i]

for _ in range(m):
    a, b = map(int, input().split())
    swap_positions(baskets, a-1, b-1)

print(' '.join(map(str, baskets)))
'''

# 7번 5597
'''
import sys
input = sys.stdin.readline

students = set(range(1, 31))                        # 전체 학생 번호 집합

submitted_students = set()                          # 제출한 학생 번호 집합 초기화
for _ in range(28):
    student_number = int(input())
    submitted_students.add(student_number)          # 제출한 학생 번호 집합에 추가

missing_students = students - submitted_students    # 제출하지 않은 학생 번호 집합

for student in sorted(missing_students):            # 제출하지 않은 학생 번호를 정렬하여 출력
    print(student)
'''

# 8번 3052
'''
remainders = set()

for _ in range(10):
    Num = int(input())
    remainder = Num % 42
    if remainders != 0:
        remainders.add(remainder)

print(len(remainders))
'''

# 9번 10811
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

baskets = list(range(1, n+1))

for _ in range(m):
    a, b = map(int, input().split())
    baskets[a-1:b] = reversed(baskets[a-1:b])

print(' '.join(map(str, baskets)))
'''

# 10번 1546
'''
import sys
input = sys.stdin.read

data = input().split()
SubjectType = int(data[0])
scores = list(map(float, data[1:]))

max_score = max(scores)

adjusted_scores = [(score / max_score) * 100 for score in scores]
average_score = sum(adjusted_scores) / SubjectType

print(average_score)
'''
