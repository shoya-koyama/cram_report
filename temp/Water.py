n = int(input())

def water(n):
    if n % 5 != 0:
        if n % 5 == 1:
            return n - 1
        elif n % 5 == 2:
            return n - 2
        elif n % 5 == 3:
            return n + 2
        elif n % 5 == 4:
            return n + 1
    else:
        return n

print(water(n))


