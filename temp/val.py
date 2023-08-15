lines = ["きま,し,200", "あい,す,10", "ま,つ,20"]  # サンプルデータ

result = 0
prev_a = None
for i, v in enumerate(lines):
    a = [i] + list(map(str, v.split(",")))  # インデックス番号をリストの先頭に追加
    if prev_a is not None and prev_a[1] != a[1]:  # 前の行と現在の行の動物名が異なる場合、前の動物の合計を出力
        print("{0}計 {1}".format(prev_a[1].strip(), result))
        result = 0  # resultをリセット
    print("* {0}".format(a[1].strip()))
    print("{0} {1}".format(a[2].strip(), a[3].strip()))
    result += int(a[3])  # 文字列から整数への変換
    prev_a = a  # 前の行を更新

# 最後の動物の合計を出力
if prev_a is not None:
    print("{0}計 {1}".format(prev_a[1].strip(), result))
