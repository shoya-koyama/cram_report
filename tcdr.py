s = input()

result = ''
for i in range(0, len(s)):
    if (s[i] != 'a') and (s[i] != 'i') and (s[i] != 'u') and (s[i] != 'e') and (s[i] != 'o'):
        result += s[i]

print(result)