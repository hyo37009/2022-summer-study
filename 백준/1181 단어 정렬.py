'''
1181 단어 정렬
난이도 : 실5

문제 :
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
    길이가 짧은 것부터
    길이가 같으면 사전 순으로
'''

n = int(input())
words = []
for _ in range(n):
    words.append(input())

words = list(set(words)) # 중복 제거
words.sort(key= lambda x: [len(x), x])
print('\n'.join(words))