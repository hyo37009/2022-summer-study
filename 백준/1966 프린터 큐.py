'''
1966 프린터 큐
난이도 : 실3
'''
from collections import deque
import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    printQueue = list(input().rstrip().split())

    print(printQueue)
    now = 0
    while True:
        if max(printQueue) != printQueue[0]:
            printQueue.append(printQueue.pop(0))
        else:
            printed = printQueue.pop(0)
            now += 1
            if m == 1:
                print(now)
                break

        m -= 1
        if m < 0:
            m = len(printQueue)
