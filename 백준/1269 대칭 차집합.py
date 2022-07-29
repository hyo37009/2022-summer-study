''''
1269 대칭 차집합
난이도 : 실3
'''

n, m = map(int, input().split())
setA = set(list(map(int, input().split())))
setB = set(list(map(int, input().split())))
print(len(setA ^ setB))