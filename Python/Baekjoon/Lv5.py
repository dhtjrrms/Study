# 5단계 문제풀이

# 1번 27866
'''
import sys
input = sys.stdin.readline

Strings = input().strip()
index = int(input().strip())

print(Strings[index-1])
'''

# 2번 2743
'''
import sys
input = sys.stdin.readline

Strings = input().strip()

print(len(Strings))
'''

# 3번 9086
'''
import sys
input = sys.stdin.readline

Testcase = int(input())

for _ in range(Testcase):
    Strings = input().strip()
    print(Strings[0]+Strings[-1])
'''

# 4번 11654
'''
import sys
input = sys.stdin.readline

word = input().strip()

print(ord(word))
'''

# 5번 11720
'''
import sys
input = sys.stdin.readline

NumInput = int(input())
NumArray = input().strip()

Total = 0

for i in range(NumInput):
    Total += int(NumArray[i])

print(Total)
'''

# 6번 10809
'''
word = input().strip()

alphabet_positions = [-1] * 26

for index, char in enumerate(word):
    alphabet_index = ord(char) - ord('a')
    if alphabet_positions[alphabet_index] == -1:
        alphabet_positions[alphabet_index] = index

print(' '.join(map(str, alphabet_positions)))
'''

# 7번 2675
'''
import sys
input = sys.stdin.readline

TestCase = int(input())

for _ in range(TestCase):
    r, s = input().split()
    r = int(r)

    result = ""
    for char in s:
        result += char * r

    print(result)
'''

# 8번 1152
'''
Sentence = input().strip()

if Sentence == "":
    print(0)
else:
    words = Sentence.split()
    print(len(words))
'''

# 9번 2908
'''
import sys
input = sys.stdin.readline

N1, N2 = input().split()

N1_reversed = N1[::-1]
N2_reversed = N2[::-1]

N1_reversed = int(N1_reversed)
N2_reversed = int(N2_reversed)

if N1_reversed > N2_reversed:
    print(N1_reversed)
else:
    print(N2_reversed)
'''

# 10번 5622
'''
Word = input()
DialNum = { 'A':3, 'B':3, 'C':3,
            'D':4, 'E':4, 'F':4,
            'G':5, 'H':5, 'I':5,
            'J':6, 'K':6, 'L':6,
            'M':7, 'N':7, 'O':7,
            'P':8, 'Q':8, 'R':8, 'S':8,
            'T':9, 'U':9, 'V':9,
            'W':10, 'X':10, 'Y':10, 'Z':10}
total_time = 0

for char in Word:
    total_time += DialNum[char]

print(total_time)
'''

# 11번 11718
'''
while True:
    try:
        sentence = input()
        print(sentence)
    except EOFError:
        break
'''