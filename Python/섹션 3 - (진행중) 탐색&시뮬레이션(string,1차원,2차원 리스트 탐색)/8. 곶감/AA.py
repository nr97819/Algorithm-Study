import sys
currentPath='C:\_Algorithm-Study-Folder\Algorithm-Study\Python\섹션 3 - (진행중) 탐색&시뮬레이션(string,1차원,2차원 리스트 탐색)\8. 곶감'
sys.stdin=open(currentPath+'\\input.txt', 'rt')

fnum=int(input())
fruits=[list(map(int,input().split())) for _ in range(fnum)]
inum=int(input())
insts=[list(map(int,input().split())) for _ in range(inum)]

print(fruits)
print()
print(insts)





# 이동 함수
def move(arr,line,dir,times):
    # 좌측으로 이동
    if dir==0:
        temp=arr[line][0]
        for i in range(len(arr)-1):
            arr[line][i]=arr[line][i+1]
        arr[line][len(arr)-1]=temp
        
    # 우측으로 이동
    elif dir==2:
        temp=arr[line][len(arr)-1]
        for i in range(len(arr)-2):
            arr[line][i+1]=arr[line][i]
        print(arr)
        arr[line][0]=temp
        print(arr)

    else:
        print('error!!')
    

# 명령어 수 만큼 반복
for i in range(inum):
    move(fruits,insts[i][0]-1,insts[i][1],insts[i][2])    