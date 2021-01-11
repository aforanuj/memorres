str = input()
z = len(str)
count = 0
if str[0]=='a' and str[z-1]=='d':
    print("mango")
for i in range(z):
    if str[i] == 'o' or str[i]=='u':
        str.upper()
        print(str)

for i in range(z):
    if str[i]=='i':
        count+=1
        break
for i in range(z):
    if str[i]=='f':
        count+=1
        break
if count==2:
    for i in range(z):
        if str[i]=='i':
            str[i].upper()
            print(str)
            break
        elif str[i]=='f':
            str[i].upper()
            print(str)
            break

#input 1:  ansfdhjnd
#Output 1: mango