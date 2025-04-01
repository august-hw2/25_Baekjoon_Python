import sys
input = sys.stdin.readline

#n = 표의 크기, m = 합 횟수
n, m = map(int, input().split())
arr = [[0]*(n+1)]
s_arr = [[0]*(n+1) for _ in range(n+1)]

#각 줄 값 받기
for i in range(n):
    row = [0] + [int(x) for x in input().split()]
    arr.append(row)

#누적 합 구하기
for i in range(1, n+1):
    for j in range(1, n+1):
        s_arr[i][j] = s_arr[i][j-1] + s_arr[i-1][j] - s_arr[i-1][j-1] + arr[i][j]

#구간 합 구하기
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(s_arr[x2][y2]-s_arr[x1-1][y2]-s_arr[x2][y1-1]+s_arr[x1-1][y1-1])