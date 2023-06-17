n = int(input())
s = input()

"""
def echo(n,s):
    result = ''
    for i in range(len(s)):
        result.join(s[i])
        a = s[i] * 2
        result.join(a)
    return result

print(echo(n, s))
"""

def echo(n, s):
    result = ''
    for i in range(len(s)):
        a = s[i] * 2
        result += a
    return result


print(echo(n, s))



result = ""
for char in s:
    result += char * 2

print(result)
