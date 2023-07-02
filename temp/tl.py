"""box = [1,0,5]

for i in range(3,51):
    box.append(0)
    box[i] = box[i-1] + box[i-3]
    box.append(box[i])"""
"""    
sum = 0

for i in range(10000,100000):
    if 1629547920 % i == 0:
        sum += i

print(sum)"""

"""
sum = 0

for i in range(1,10000):
    if (i % 3 == 0) or (len(str(i)) == 3) or ('3' in str(i)):
        sum += i

print(sum)"""

"""
count = 0
a = ""

for i in range(1, 10000000):
    if (i % 3 != 0) or (i % 5 != 0):
       a.join(str(i))
for j in a:
    if j == '1':
        count += 1
        
print(count)"""

def count_one(n):
    count = 0
    for i in range(1, len(str(n)) + 1):
        count += ((n // (10 ** i)) * (10 ** (i - 1)) +
                 min(max((n % (10 ** i)) - 10 ** (i - 1) + 1, 0), 10 ** (i - 1)))
    return count

def count_fizz_buzz(n):
    count_fizz = n // 3
    count_buzz = n // 5
    count_fizz_buzz = n // 15
    return count_fizz + count_buzz - 2 * count_fizz_buzz

n = 10000000
print(count_one(n) - count_fizz_buzz(n))
