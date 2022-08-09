'''
20305 커트라인
난이도 : 브2
사용 : 퀵정렬
'''
def Quicksort(S):
    if len(S) <= 1:
        return S
    else:
        a = sorted([S[0], S[len(S)//2], S[-1]])
        pivot = a[1]
        S.remove(pivot)
        S1, S2 = [], []
        for s in S:
            if s <= pivot:
                S1.append(s)
            else:
                S2.append(s)
        S = []
        S1 = Quicksort(S1)
        S += S1
        S.append(pivot)
        S2 = Quicksort(S2)
        S += S2

        return S


n, k = map(int, input().split())
scores = list(map(int, input().split()))

scores = Quicksort(scores)
print(scores[-k])
