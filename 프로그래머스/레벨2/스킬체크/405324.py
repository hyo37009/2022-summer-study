def solution(s):
    answer = [0, 0]

    while s != '1':
        ones = s.count('1')
        answer[0] += 1
        answer[1] += len(s) - ones
        s = str(bin(ones))[2:]

    return answer

s = "1111111"
print(solution(s))