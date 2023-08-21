l = input()
l = l.replace(',', '')

y = ''
for i in range(len(l)):
    if i % 2 == 0 or (i % 2 == 1 and l[i] == l[i-1]):
        y += l[i]
        if i != len(l) - 1:  # 最後の文字以外の場合
            y += ','

print(y.rltrip(','))  # 末尾のコンマを取り除く

unique_chars = set()
for y in t:
    if y.isupper() or y.isdigit():
        unique_chars.add(y)

print(len(unique_chars))

