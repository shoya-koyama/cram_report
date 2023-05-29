def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_n_values(limit):
    prime_n_values = []
    for n in range(1, limit + 1):
        result = n**3 - 7*n + 9
        if is_prime(result):
            prime_n_values.append(n)
    return prime_n_values

n_values = find_n_values(100)
print("整数nの値:", n_values)