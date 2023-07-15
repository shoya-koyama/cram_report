"""n = list(map(int, input().split()))
d = list(map(int, input().split()))
b = []
b.append(n[1])

for i in range(n[0]):
    b.append(d[i])
    d[i] += n[2]
    a = min(b)

print(a)"""

# 入力
n, P, Q = map(int, input().split())
d = list(map(int, input().split()))

# 割引券を使わない場合のドリンクの価格
no_discount = P

# 割引券を使う場合のドリンクと最も安い料理の価格
if d:  # 料理が存在する場合
    with_discount = Q + min(d)
else:  # 料理が存在しない場合
    with_discount = no_discount  # 割引券を使うことはできない

# 2つの価格の最小値を出力
print(min(no_discount, with_discount))