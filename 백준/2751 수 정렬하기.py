'''
2751 수 정렬하기
난이도 : 실5
O(n lg n)에 정렬하는 문제, 머지 소트 사용.
'''
import sys

input = sys.stdin.readline

def merge(A:list, p:int, q:int, r:int)->list:
    n1 = q - p + 1
    n2 = r - q
    L = [None] * n1
    R = [None] * n2

    for i in range(0, len(L)):
        L[i] = A[p + i]
    for j in range(0, len(R)):
        R[j] = A[q + j + 1]
    L.append(float('inf'))
    R.append(float('inf'))

    i , j = 0, 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A

def mergesort(A, p, r) -> list:
    if p < r:
        q = (p + r) // 2
        A = mergesort(A, p, q)
        A = mergesort(A, q+1, r)
        A = merge(A, p, q, r)
    return A

if __name__ == '__main__':
    n = int(input().rstrip())
    A = [None] * n
    for i in range(n):
        A[i] = int(input().rstrip())

    A = mergesort(A, 0, len(A)-1)

    for num in A:
        print(num)