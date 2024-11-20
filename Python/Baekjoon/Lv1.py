# 1단계 문제 풀이

# 1번 2557
'''
print('Hello World!')
'''

# 2번 1000
'''
a, b = map(int, input().split())
print (a+b)
'''

# 3번 1001
'''
a, b = map(int, input().split())
print(a-b)
'''

# 4번 10998
'''
a, b = map(int, input().split())
print(a*b)
'''

# 5번 1008
'''
a, b = map(int, input().split())
print(a/b)
'''

# 6번 10869
'''
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
'''

# 7번 10926
'''
input_str = input()
print(input_str + "??!")
'''

# 8번 18108
'''
year = int(input())
Thai_year = year - 543
print(Thai_year)
'''

# 9번 10430
'''
a,b,c = map(int, input().split())

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
'''

# 10번 2588
'''
a = int(input())
b = int(input())
hun_b = b // 100            # 백의 자리

b1 = b - (hun_b * 100)      # 백의 자리를 제외한 나머지 숫자
ten_b = b1 // 10            # 십의 자리

one_b = b1 - (ten_b * 10)   # 일의 자리

print(a * one_b)
print(a * ten_b)
print(a * hun_b)
print(a * b)
'''

# 11번 11382
'''
a,b,c = map(int, input().split())
print(a+b+c)
'''

# 12번 10171
'''
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")
'''

# 13번 10172
'''
print("|\\_/|")
print("|q p|  /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")
'''