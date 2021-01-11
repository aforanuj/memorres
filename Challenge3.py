s = list(input())
arr=[0]*36
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','zero','one','two','three','four','five','six','seven','eight','nine']



for i in range(len(s)):
    if ord(s[i])<=90 and ord(s[i])>=65: #Uppercase
        arr[ord(s[i])-ord('A')] = arr[ord(s[i])-ord('A')]+2
    if ord(s[i])<=122 and ord(s[i])>=97: #lowercase
        arr[ord(s[i])-ord('a')] = arr[ord(s[i])-ord('a')] + 1
    if ord(s[i]) <= 57 and ord(s[i]) >= 48:     #numbers
        arr[ord(s[i]) - ord('0') + 26] = arr[ord(s[i]) - ord('0') + 26] + 1
for i in range(len(arr)):
    if arr[i] > 0:
        print(alphabet[i],"=",arr[i])

#Input : Anuj@123
#output :
# a = 2
# j = 1
# n = 1
# u = 1
# one = 1
# two = 1
# three = 1
