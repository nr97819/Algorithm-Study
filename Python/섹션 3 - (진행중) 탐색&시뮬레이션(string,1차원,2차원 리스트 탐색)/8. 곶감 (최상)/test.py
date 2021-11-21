import sys
currentPath='C:\_Algorithm-Study-Folder\Algorithm-Study\Python\섹션 3 - (진행중) 탐색&시뮬레이션(string,1차원,2차원 리스트 탐색)\8. 곶감'
sys.stdin=open(currentPath+'\\input.txt', 'rt')

fnum=int(input())
fruits=[list(map(int,input().split())) for _ in range(fnum)]

inum=int(input())
insts=[list(map(int,input().split())) for _ in range(inum)]

# 명령어 수 만큼 반복
# arr=[[1,2,3,4,5,6,7,8,9]]
# inst=[[0,0,3]]

line=0
dir=1

# 이동 함수
def move(arr,line,dir,times):
    line-=1
    for i in range(times):
        # 좌측으로 이동
        if dir==0:
            temp=arr[line][0]
            for i in range(len(arr[line])-1):
                arr[line][i]=arr[line][i+1]
            arr[line][len(arr[line])-1]=temp
            
        # 우측으로 이동
        elif dir==1:
            temp=arr[line][len(arr[line])-1]
            for i in range(len(arr[line])-2,-1,-1):
                arr[line][i+1]=arr[line][i]
            arr[line][0]=temp

        else:
            print('error!!')

    return arr
    
def sum(arr):
    n=fnum
    sum=0
    
    sp=0
    times=n
    op=-2
    sop=1

    for i in range(n):
        if(times==1):
            op=2
            sop=-1
        for j in range(sp,sp+times):
            sum+=arr[i][j]
        times+=op
        sp+=sop
        
    return sum

# 명령어 대입 (instruments)
for i in range(len(insts)):
    move(fruits,insts[i][0],insts[i][1],insts[i][2])

# print(fruits)
print(sum(fruits))