import sys
#sys.stdin=open('input.txt', 'rt')

s=input()

temp=''
cnt=0
for c in s:
    if c.isdecimal():
        if cnt>0 or int(c)!=0:
            temp+=c
            cnt+=1

arr=[]
temp=int(temp)
for i in range(1, temp+1):
    if temp%i==0:
        arr.append(i)

print(temp)
print(len(arr))