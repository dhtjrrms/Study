# 3단계 문제풀이

# 1번 2739
'''
num = int(input())

for i in range(1, 10):
    print(f"{num} * {i} = {num*i}")
'''

# 2번 10950
'''
Test = int(input())

for _ in range(Test):
    a,b = map(int, input().split())
    print(a+b)
'''

# 3번 8393
'''
num = int(input())

for i in range(1,num):
    num+=i

print(num)
'''
# 4번 25304
'''
Receipt = int(input())
StuffType = int(input())
TotalCost = 0

for _ in range(StuffType):
    cost, num = map(int, input().split())
    TotalCost = TotalCost + (cost * num)

if Receipt == TotalCost:
    print("Yes")
else:
    print("No")
'''

# 5번 25314
'''
LongNum = int(input())
TrueNum = LongNum // 4
Result = "long " * TrueNum + "int"
print(Result)
'''

# 6번 15552
'''
import sys
TestCase = int(sys.stdin.readline())

for _ in range(TestCase):
    N1, N2 = map(int, sys.stdin.readline().split())
    print(N1+N2)
'''

# 7번 11021
'''
import sys
TestCase = int(sys.stdin.readline())

for x in range(1, TestCase+1):
    N1, N2 = map(int, sys.stdin.readline().split())
    print(f"Case #{x}: {N1+N2}")
'''

# 8번 11022
'''
import sys
TestCase = int(sys.stdin.readline())

for x in range(1, TestCase+1):
    N1, N2 = map(int, sys.stdin.readline().split())
    print(f"Case #{x}: {N1} + {N2} = {N1+N2}")
'''

# 9번 2438
'''
import sys
LineNum = int(sys.stdin.readline())

for i in range(1, LineNum+1):
    print('*' * i)
'''

# 10번 2439
'''
import sys
TestCase = int(sys.stdin.readline())

for i in range(1, TestCase + 1):
    print(" " * (TestCase - i) + "*" * i)
'''

# 11번 10952
'''
import sys
while True:
    N1, N2 = map(int, sys.stdin.readline().split())
    if N1 == 0 and N2 == 0:
        break
    print(N1+N2)
'''

# 12번 10951
'''
import sys

for line in sys.stdin:
    N1, N2 = map(int, line.split())
    print(N1+N2)
'''