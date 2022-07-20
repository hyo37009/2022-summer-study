'''
10816 숫자 카드2
난이도 : 실4
'''
import sys
input = sys.stdin.readline

n = int(input())
sangun = list(input().split())
output = {}
outlist = []
for i in range(n):
    output[sangun[i]] = 0

for i in sangun:
    output[i] += 1

m = int(input())
cards = list(input().split())

for card in cards:
    if card not in output.keys():
        outlist.append('0')
        continue
    outlist.append(str(output[card]))

print(' '.join(outlist))