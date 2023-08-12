N = int(input())
pi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'

result = ''
for i in range(N+3):
    result += i


if (result[N+2] == '1') or (result[N+2] == '2') or (result[N+2] == '3') or (result[N+2] == '4'):
    result[N+1] += 1
else:
    result[N+1] += 0


print(result)

#四捨五入
def rounded_pi(N):
    pi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
    
    # piからN+1文字取得
    integer_part = pi[:1]  # "3"
    decimal_part = pi[2:N+2]  # N digits after the decimal point

    # N+1 位の数字を確認して四捨五入
    if pi[N+2] in ['5', '6', '7', '8', '9']:
        decimal_part = str(int(decimal_part) + 1)
    # If the rounding caused it to carry over
    if len(decimal_part) < N:
        integer_part = str(int(integer_part) + 1)
        decimal_part = "0" * (N - len(decimal_part)) + decimal_part

    result = integer_part + "." + decimal_part

    return result

# For demonstration purposes
N = 5  # Example input
rounded_pi(N)

"""pi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
N = int(input())
for i in range(N + 2):
    print(pi[i], end='')"""