def alternately(n,s):
    for i in range(0,n+1):
        if ((s[2*i] == 'M')) and ((s[2*i+1] == 'F')):
            return 'Yes'
        else:
            return 'No'

"""N=int(input())
S=input()
for i in range(N-1):
  if S[i]==S[i+1]:
    print("No")
    exit()
print("Yes")"""

print(alternately(6,'MFMFMF'))
print(alternately(9,'FMFMMFMFM'))
print(alternately(1,'F'))

