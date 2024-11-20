# 2단계 문제풀이

# 1번 1330
'''
A,B = map(int, input().split())
if A > B :
    print(">")
elif A < B :
    print("<")
else :
    print("==")
'''

# 2번 9498
'''
Score = int(input())
if Score >= 90:
    print("A")
elif Score >= 80:
    print("B")
elif Score >= 70:
    print("C")
elif Score >= 60:
    print("D")
else:
    print("F")
'''

# 3번 2753
'''
year = int(input())
if ((year % 4 == 0) and (year % 100 != 0)) or year % 400 == 0 :
    print("1")
else:
    print("0")
'''

# 4번 14681
'''
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
else :
    print("4")
'''

# 5번 2884
'''
Hour, minute = map(int, input().split())

if minute-45 < 0:
    Hour = Hour-1
    if Hour < 0 :
        Hour = 23
    minute = 60 + (minute-45)
else :
    minute = minute - 45

print(Hour, minute)
'''

# 6번 2525
'''
h, m = map(int, input().split())
t = int(input())

m+=t

if m >= 60:
    h += m // 60
    m = m % 60

if h >= 24:
    h = h % 24

print(h, m)
'''

# 7번 2480
'''
a,b,c = map(int, input().split())

if a == b == c:
    print(10000 + (a * 1000))

if a == b and (a != c and b != c):
    print(1000 + (a * 100))
elif b == c and (b != a and c != a):
    print(1000 + (b * 100))
elif c == a and (c != b and a != b):
    print(1000 + (c * 100))

if a != b and b != c and c != a:
    if a > b and a > c:
        print(a * 100)
    elif b > a and b > c:
        print(b * 100)
    elif c > a and c > b:
        print(c * 100)
'''
