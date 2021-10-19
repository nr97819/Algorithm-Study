import sys
# currentPath='C:\\_Algorithm-Study-Folder\\Algorithm-Study\\Python\\섹션 3 - (진행중) 탐색&시뮬레이션(string,1차원,2차원 리스트 탐색)\\7. 사과나무'
# sys.stdin=open(currentPath+'\\input.txt', 'rt')

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
# arr=[list(map(int,input().split()))] * num

rFlag=False
cFlag=False
sum=0
repeat=1
middle=int(n/2) #배열은 0부터이므로, -1 안 해줘도 됨
cursor=middle
for i in range(n):
    nowLoc=cursor
    for _ in range(repeat):
        sum+=arr[i][nowLoc]
        nowLoc+=1
        
    if repeat==n:
        rFlag=True
    if(rFlag):
        repeat-=2
        if repeat<0:
            break
    else:
        repeat+=2

    if cursor==0:
        cFlag=True
    if(cFlag):
        cursor+=1
    else:
        cursor-=1
print(sum)