import sys

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

def main(lines):


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
    s = str(lines)
    so = sorted(s)
    j = ''.join(so)
    i = int(j)
    return i

main(12212122212222)
