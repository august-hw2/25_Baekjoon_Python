n = input() #과목 개수
arr = list(map(int, input().split())) #과목 점수 리스트
m = max(arr)
s = sum(arr)

print(s/m*100/int(n))