def solution(number, k):
    maxindex = number.index(max(number))
    deleted = 0

    while k != 0:
        if maxindex - 1 > k:
            maxindex =
            continue
        k -= maxindex - deleted
        number = number[:deleted] + number[maxindex:]
        deleted += maxindex - deleted
        if k != 0:
            maxindex = number.index(max(number[deleted:]))

    answer = number
    return answer

if __name__ == '__main__':
    number = "1231234"
    k = 3

    print(solution(number, k))