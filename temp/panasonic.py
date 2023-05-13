def winner(n,s):
    1 <= n <= 100
    count_t = 0
    count_a = 0
    for i in s:
        if i == 'T':
            count_t += 1
        elif i == 'A':
            count_a += 1
    if count_t < count_a:
        return 'A'
    elif count_t > count_a:
        return 'T'
    else:
        if s[n]=='T':
            return 'A'
        elif s[n] == 'A':
            return 'T'
        
print(winner(5,'TTAAT'))
print(winner(6,'ATTATA'))
print(winner(1,'A'))