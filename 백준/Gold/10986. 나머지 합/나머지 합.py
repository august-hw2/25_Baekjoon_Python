import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

# 누적합을 담을 리스트
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + a[i]

# 나머지 카운트 배열
remainder_count = [0] * m
answer = 0

# 누적합을 m으로 나눈 나머지를 기반으로 카운트
for i in range(n + 1):
    remainder = s[i] % m
    answer += remainder_count[remainder]
    remainder_count[remainder] += 1

print(answer)