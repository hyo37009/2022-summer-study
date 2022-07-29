'''
1934 최소공배수
난이도 : 브1
'''
import sys
input = sys.stdin.readline


n = int(input().rstrip())
numsets = []
for _ in range(n):
    numsets.append(list(map(int, input().rstrip().split())))

for numset in numsets:
    a, b = numset[0], numset[1]
    lista, listb = [], []
    now = 2
    while a != 1:
        if a % now == 0:
            lista.append(now)
            a //= now
        else:
            now += 1
    now = 2
    while b != 1:
        if b % now == 0:
            listb.append(now)
            b //= now
        else:
            now += 1

    # print(lista)
    # print(listb)
    result = 1
    for num in set(lista + listb):
        counta = lista.count(num)
        countb = listb.count(num)
        if counta >= countb:
            result *= num ** counta
        else:
            result *= num ** countb

    print(result)