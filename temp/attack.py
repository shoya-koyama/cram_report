a = int(input())
b = int(input())

#def attack(a,b):
#    for i in range(10**18):
#        a -=  b * i
#        if a < 0:
#            break
#    return i + 1
#    
#print(attack(a, b)


#a, b = map(int, input().split())
print((a + b - 1) // b)