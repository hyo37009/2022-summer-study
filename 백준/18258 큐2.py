'''
18258 큐2
map함수가 시간복잡도가 O(n)이라길래 없애도 계속 시간초과가 뜬다.
'''
import sys

if __name__ == "__main__":
    elements = []
    k = int(input())

    for i in range(k):
        now = list(sys.stdin.readline().rstrip().split())
        # print(now)

        what = now[0]
        if what == 'push':
            elements.append(int(now[1]))
        elif what == 'pop':
            if not elements:
                print(-1)
            else:
                print(elements.pop())
        elif what == 'size':
            print(len(elements))
        elif what == 'empty':
            if elements:
                print(0)
            else:
                print(1)
        elif what == 'front':
            if not elements:
                print(-1)
            else:
                print(elements[0])
        else:
            if not elements:
                print(-1)
            else:
                print(elements[-1])