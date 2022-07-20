'''
10815 숫자 카드
난이도 : 실5
'''

n = int(input())
set1 = set(list(map(int, input().split())))
m = int(input())
sangun = list(map(int, input().split()))

for i in range(m):
    if sangun[i] in set1:
        print(1, end=' ')
    else:
        print(0, end=' ')