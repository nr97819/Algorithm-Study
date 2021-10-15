import sys
#sys.stdin=open('input.txt', 'rt')

n,m=map(int,input().split())
arr=list(map(int,input().split()))

cnt=0
sum=arr[0] # 첫 원소는 가지고 시작
lp=0 # right pointer
rp=1 # left pointer
while True:
    if sum<m:
        if rp<n:
            sum+=arr[rp]
            rp+=1
        else:
            break
    elif sum==m:
        if lp<rp: # 에러 방지
            cnt+=1
            sum-=arr[lp]
            lp+=1
    else: # sum>m
        if lp<rp: # 에러 방지
            sum-=arr[lp]
            lp+=1




print(cnt)