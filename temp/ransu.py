import random

# 0から1.0の間の乱数を生成する
print(random.random())

# 1から10の範囲内の整数をランダムに生成する
print(random.randint(1, 10))

# ランダムに選択された要素を返す
colors = ["red", "blue", "green", "yellow"]
print(random.choice(colors))