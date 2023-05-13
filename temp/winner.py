def winner(n,s):
    1 <= n <= 100
    if s.count('T') < s.count('A'):
        return 'A'
    elif s.count('T') > s.count('A'):
        return 'T'
    else:
        if s[-1]=='T':
            return 'A'
        elif s[-1] == 'A':
            return 'T'
        
print(winner(5,'TTAAT'))
print(winner(6,'ATTATA'))
print(winner(1,'A'))