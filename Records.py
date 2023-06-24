"""n = int(input())
a = [int(i) for i in input().split()]


def record(n, a):
    b = []
    result = 0
    for i in range(len(a)//n):
        for j in range(7):
            result += a[j]
            b.append(result)
    return b


print(record(n, a))"""

N = int(input().strip())
A = list(map(int, input().strip().split()))

weekly_steps = []

for i in range(N):
    weekly_steps.append(sum(A[i*7:(i+1)*7]))

print(' '.join(map(str, weekly_steps)))

N = int(input().strip()) # N を入力し、整数型に変換します。
strings = [input().strip() for _ in range(N)] # N 回ループし、各ループで新たな文字列を入力し、その文字列をリストに追加します。

strings_set = set(strings) # 文字列のリストをセットに変換します。これにより、特定の要素の存在を O(1) の時間で確認できます。

for string in strings: # strings リストの各文字列についてループします。
    if string[::-1] in strings_set: # 現在の文字列を逆順にしたものがセットに存在するかどうかを確認します。
        print("YES") # 逆順の文字列が存在するなら、"YES" を出力します。
        break # 回文を発見したので、ループを終了します。
else: # for ループが break せずに正常に終了した場合（すなわち、回文を見つけられなかった場合）、このブロックが実行されます。
    print("NO") # 回文を見つけられなかったので、"NO" を出力します。
