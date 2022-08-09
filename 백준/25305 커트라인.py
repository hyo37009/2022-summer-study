'''
20305 커트라인
난이도 : 브2
'''
n, k = map(int, input().split())
scores = list(map(int, input().split()))

scores.sort()
print(scores[-k])
