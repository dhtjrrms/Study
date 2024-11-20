# 6단계 문제풀이

# 1번 25083
'''
print("         ,r\'\"7")
print("r`-_   ,\'  ,/")
print(" \\. \". L_r\'")
print("   `~\\/")
print("      |")
print("      |")
'''
# 2번 3003
'''
import sys
input = sys.stdin.readline

RightPieces = [1,1,2,2,2,8]
InputPieces = list(map(int, input().split()))

for i in range(6):
    print(RightPieces[i]-InputPieces[i], end=" ")
'''

# 3번 2444
'''
Num = int(input())

for i in range(Num):
    print(" " * (Num-i-1) + "*" * (2*i+1))

for i in range(Num-2, -1, -1):
    print(" " * (Num-i-1) + "*" * (2*i+1))
'''

# 4번 10988
'''
import sys
input = sys.stdin.readline

Word = input().strip()
WordReversed = Word[::-1]

if Word == WordReversed:
    print(1)
else :
    print(0)
'''

# 5번 1157
'''
import sys
input = sys.stdin.readline

Word = input().strip().upper()
count = { }

for char in Word:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

max = max(count.values())
common = [k for k, v in count.items() if v == max]

if len(common) > 1:
    print("?")
else:
    print(common[0])
'''

# 6번 2941
'''
alphabet = [ 'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ]
word = input()

for i in alphabet:
    word = word.replace(i, 'a')

print(len(word))
'''

# 7번 1316
'''
import sys
input = sys.stdin.readline

TestCase = int(input())
count = TestCase

for _ in range(TestCase):
    Word = input()
    for i in range(0, len(Word)-1):
        if Word[i] == Word[i+1]:
            pass
        elif Word[i] in Word[i+1:]:
            count -= 1
            break

print(count)
'''

# 8번 25206
'''
import sys
input = sys.stdin.readline

Rate =  [ 'A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F' ]
Grade = [ 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

Total = 0
Result = 0
for _ in range(20):
    subject, point, grade = input().split()
    point = float(point)

    if grade != 'P':
        Total += point
        Result += point * Grade[Rate.index(grade)]

print('%.6f' %(Result/Total))\
'''