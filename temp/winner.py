n = int(input())
s = input()

def winner(n,s):
    if s.count('T') < s.count('A'):
        return 'A'
    elif s.count('T') > s.count('A'):
        return 'T'
    else:
        if s[-1]=='T':
            return 'A'
        elif s[-1] == 'A':
            return 'T'
print(winner(n, s))