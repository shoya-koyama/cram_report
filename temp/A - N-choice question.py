def choice(n,a,b,c):
    1 <= n <= 300
    1 <= a
    b <= 1000
    for i in range(n+1):
        1 <= c[i] <= 2000
        if a + b == c[i]:
            return i + 1
        
print(choice(3,125,175,[200,300,400]))
print(choice(1,1,1,[2]))
print(choice(5,123,456,[135,246,357,468,579]))