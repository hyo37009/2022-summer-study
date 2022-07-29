'''
3036 링
난이도 : 실4
'''

n = int(input())
rings = list(map(int, input().split()))

first = rings[0]
firstnums = []
now = 2
while first != 1:
    if first % now == 0:
        firstnums.append(now)
        first //= now
    else:
        now += 1

for i in range(1, n):
    first = rings[0]
    now = rings[i]
    for num in firstnums:
        if now % num == 0:
            first //= num
            now //= num
    print(f'{first}/{now}')

