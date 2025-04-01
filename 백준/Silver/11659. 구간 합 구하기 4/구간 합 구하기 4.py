import sys
input = sys.stdin.readline 
#input으로 여러 줄을 받으면, 시간 초과 발생할 수 있음 따라서 해당 구문 넣어주기

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