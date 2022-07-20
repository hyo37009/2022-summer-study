'''
18258 큐2
map함수가 시간복잡도가 O(n)이라길래 없애도 계속 시간초과가 뜬다.
'''
import sys

if __name__ == "__main__":
    elements = []
    k = int(input())
    leng = 0

    for i in range(k):
        now = list(sys.stdin.readline().rstrip().split())
        printing = []

        what = now[0]
        if what == 'push':
            elements.append(now[1])
            leng += 1
        elif what == 'pop':
            if not elements:
                printing.append(-1)
            else:
                printing.append(elements[0])
                elements = elements[1:]
        elif what == 'size':
            printing.append(str(leng))
        elif what == 'empty':
            if elements:
                printing.append(0)
            else:
                printing.append(1)
        elif what == 'front':
            if not elements:
                printing.append(-1)
            else:
                printing.append(elements[0])
        else:
            if not elements:
                printing.append(-1)
            else:
                printing.append(elements[-1])

    print(printing)