

def Interview(n,s):
    if (n>=1) and (n<=100):
        for i in range(len(s)):
            if (s[i] == "o") and ("x" not in s):
                return "Yes"
            else:
                return "No"
            
print(Interview(4,"oo--"))
print(Interview(3,"---"))
print(Interview(1,"o"))
print(Interview(100,"ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooox"))