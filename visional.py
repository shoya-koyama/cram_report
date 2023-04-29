import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    for i, v, m in enumerate(lines):
        print("line[{0}]: {1} {2}".format(i, v, m))
        if m % i == 0:
            return v
        if (m % 3 == 0) and (m % 5 == 0):
            return v + v
        else:
            return m

if __name__ == '__main__':
    lines = [3:piyo 5:hogera 5]
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    if lines <= 8:
        s = str(lines)
        so = sorted(s)
        j = ''.join(so)
        i = int(j)

    return i

main(12212122212222)

