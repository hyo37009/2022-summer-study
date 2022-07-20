'''
1620 나는야 포켓몬 마스터 이다솜
난이도: 실4

문제 : 뭐 이런게 다 있담?
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
pokemon = []
for i in range(n):
    pokemon.append(input().rstrip())

for i in range(m):
    inp = input().rstrip()
    if inp.isdigit():
        print(pokemon[int(inp) - 1])
    else:
        print(pokemon.index(inp) + 1)

