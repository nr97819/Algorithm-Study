import sys
#sys.stdin=open('input.txt', 'rt')

n=int(input())
arr=list(map(int,input().split()))

cnt=0
result=0
for i in range(len(arr)):
    if arr[i]==1:
        cnt+=1
        result+=cnt
    else:
        cnt=0

print(result)