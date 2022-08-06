'''
11866 요세푸스 문제0
난이도 : 실5
'''
from collections import deque
n, k = map(int, input().split())
queue = deque([str(i) for i in range(1, n + 1)])
result = []
i = 1
while len(queue) > 1:
    if i < k:
        queue.append(queue.popleft())
        i += 1
    else:
        result.append(queue.popleft())
        i = 1
result.append(queue.pop())
print('<' + ', '.join(result) + '>')