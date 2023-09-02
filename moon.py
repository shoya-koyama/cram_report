# 入力部
N, M, P = map(int, input().split())

result = []
count = 0
for i in range(M, N+1, P):
    result.append(i)
    count+= 1

print(count)