n = int(input())
p = list(map(int, input().split()))

if p[0] != max(p):
    print(max(p) + 1 - p[0])
elif p[0] == max(p):
    print(0)
else:
    print(all(val == p[0] for val in p))


