def solution(n, k):
    answer = 0

    #n진수로 변환합니다
    knum = []
    while n > k:
        knum.append(str(n % k))
        n //= k
    knum.append(str(n))
    knum = ''.join(knum[::-1])

    # 조건에 맞는 모든 수를 구합니다
    tem = 0
    allnum = []
    for i in range(len(knum)):
        if knum[i] == '0':
            allnum.append(int(knum[tem:i]))
            tem = i
    allnum.append(int(knum[tem:]))

    # 검사할 소수를 구합니다
    primes = []
    n = max(allnum)
    a = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False

    for num in allnum:
        if num in primes:
            answer += 1


    return answer

print(solution(10000, 10))