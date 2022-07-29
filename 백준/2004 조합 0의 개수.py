'''
2004 조합 0의 개수
난이도 : 실2
'''

n, k = map(int, input().split())
if n // 2 < k:
    k = n - k
up = [0, 0]

for i in range(n, n - k, -1):
    while True:
        if i % 10 == 0:
            up[0] += 1
            up[1] += 1
            i //= 10
        else:
            break
    while True:
        if i % 2 == 0:
            up[0] += 1
            i //= 2
        else:
            break
    while True:
        if i % 5 == 0:
            up[1] += 1
            i //= 5
        else:
            break
for i in range(1, k + 1):
    while True:
        if i % 10 == 0:
            up[0] -= 1
            up[1] -= 1
            i //= 10
        else:
            break
    while True:
        if i % 2 == 0:
            up[0] -= 1
            i //= 2
        else:
            break
    while True:
        if i % 5 == 0:
            up[1] -= 1
            i //= 5
        else:
            break
print(up)

if up[0] == 0 or up[1] == 0:
    print(0)
else:
    print(up[0] if up[0] <= up[1] else up[1])
