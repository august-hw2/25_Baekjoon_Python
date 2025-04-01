import sys
input = sys.stdin.readline

# n개의 수, m으로 나누어 떨어지는...
n, m = map(int, input().split())

# 원본 리스트
a = list(map(int, input().split()))

# 누적합
r = [0] * m
tmp = 0
r[0] = 1  # 중요! 누적합이 0인 경우 포함

for i in a:
    tmp += i
    r[tmp % m] += 1  # 나머지 수 카운팅

res = 0
for i in r:
    res += i * (i - 1) // 2  # 조합 공식 nC2

print(res)