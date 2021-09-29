import sys
#sys.stdin=open('input.txt', 'rt')

num=int(input())
arr=[0]*(num+1)

for i in range(2, num+1):
    if arr[i]==0:
        for j in range(2, num):
            if i*j > num:
                break
            arr[i*j]+=1

cnt=0
for i in range(2, num+1):
    if arr[i]==0:
        cnt+=1

print(cnt)