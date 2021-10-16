import sys
sys.stdin=open('input.txt', 'rt')

n,m=map(int,input().split())
arr=list(map(int,input().split()))

cnt=0
tempSum=0
for i in range(n):
    tempSum=0
    for j in range(i,n):
        tempSum+=arr[j]
        if tempSum>m:
            break
        if tempSum==m:
            cnt+=1
            break
print(cnt)