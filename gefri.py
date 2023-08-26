# 入力部
N, H, X = map(int, input().split())
P = list(map(int, input().split()))

# 目標となる体力
target = X - H

# 傷薬を走査
for i in range(N):
    # 体力が目標以上になる傷薬を見つけた場合、その傷薬の番号を出力
    if P[i] >= target:
        print(i + 1)
        break
