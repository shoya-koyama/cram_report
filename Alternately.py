def alternately(n,s):
    for i in range(0,n+1):
        if ((i%2==0)and(s[i] == 'M')) and ((i%2==1)and(s[i] == 'F')):
            return 'Yes'
        else:
            return 'No'

print(alternately(6,'MFMFMF'))
print(alternately(9,'FMFMMFMFM'))
print(alternately(1,'F'))