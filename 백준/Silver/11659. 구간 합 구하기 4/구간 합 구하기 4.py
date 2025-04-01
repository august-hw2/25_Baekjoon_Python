import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0]
tmp = 0

#구간 합 배열 -> 누적 합 배열
for i in arr:
    tmp += i
    sum_arr.append(tmp)

#구간 합 공식 -> a ~ b => 배열[b]-배열[a-1]
for i in range(m):
    a, b = map(int, input().split())
    print(sum_arr[b]-sum_arr[a-1])