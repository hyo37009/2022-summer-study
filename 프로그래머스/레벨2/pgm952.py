def solution(s):
    answer = ''
    numlist = list(map(int, s.split()))
    answer = str(min(numlist)) + ' ' + str(max(numlist))
    return answer

if __name__ == '__main__':
    s = "1 2 3 4"

    print(solution(s))