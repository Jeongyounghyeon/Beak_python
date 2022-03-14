import sys, itertools

input = sys.stdin.readline

N, K = map(int, input().split())
answer = 0 

if K < 5:
    print(0)
    exit()

if K == 26:
    print(N)
    exit()

first_word = {'a', 'n', 't', 'i', 'c'}

remain_alphabet = set(chr(i) for i in range(97, 123)) - first_word
data = [sys.stdin.readline().rstrip()[4:-4] for _ in range(N)]

def countReadableWords(data, learned):
    cnt = 0
    for word in data:
        canRead = 1
        for w in word:
            if learned[ord(w)] == 0:
                canRead = 0
                break
        if canRead == 1:
            cnt += 1
    return cnt

if K >= 5:
    learned = [0] * 123
    for x in first_word:
        learned[ord(x)] = 1

    for teach in list(itertools.combinations(remain_alphabet, K-5)):
        for t in teach:
            learned[ord(t)] = 1
        cnt = countReadableWords(data, learned)

        if cnt > answer:
            answer = cnt
        for t in teach:
            learned[ord(t)] = 0
    print(answer)

else:
    print(0)