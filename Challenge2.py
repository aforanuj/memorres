n = list(map(int,input()))

for i in range(len(n)):
    if i==1 and n[i]==0:
        n[i] == None
    if i%2!=0:
        n[i] = None
    if i==0 and n[i]==2:
        n[i] = 0
    if i%2==0:
        n[i] = 0
    if n[i-1]==n[i]:
        n[i-1] = None
print(" ".join(map(str,n)))
