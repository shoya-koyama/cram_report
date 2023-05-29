n = int(input())
s = input()
t = input()

def similar(n,s,t):
    for i in range(len(s)+1):
        for j in range(len(t)+1):
            if (i == j) or (i == 'o' and j == '0') or (i == '0' and j == 'o') or (i == 'l' and j == '1') or (i == '1' and j == 'l'):
                return 'Yes'
            else:
                return 'No'
            
print(similar(n,s,t))

def is_similar_string(n,s,t):
    if len(s) != len(t):
        return False
 
    for i in range(len(s)):
        a = s[i]
        b = t[i]
 
        if a == b:
            continue
 
        if (a == '1' and b == 'l') or (a == 'l' and b == '1'):
            continue
 
        if (a == '0' and b == 'o') or (a == 'o' and b == '0'):
            continue
 
        return False
 
    return True
 
result = is_similar_string(n, s, t)
print(result)  
