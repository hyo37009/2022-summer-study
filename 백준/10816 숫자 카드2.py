'''
10816 숫자 카드2
난이도 : 실4
'''
import sys
input = sys.stdin.readline

n = int(input())
sangun = list(input().split())
m = int(input())
cards = list(input().split())
output = []

for card in cards:
    output.append(str(sangun.count(card)))

print(' '.join(output))