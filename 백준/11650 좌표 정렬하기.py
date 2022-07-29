'''
11650 좌표 정렬하기
난이도 : 실5
'''

n = int(input())
points = []
for _ in range(n):
    points.append(input())

points.sort(key= lambda x: list(map(int, x.split())))
print('\n'.join(points))