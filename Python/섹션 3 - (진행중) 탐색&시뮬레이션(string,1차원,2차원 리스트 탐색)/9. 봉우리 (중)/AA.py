import sys
# currentPath='C:\_Algorithm-Study-Folder\Algorithm-Study\Python\섹션 3 - (진행중) 탐색&시뮬레이션(string,1차원,2차원 리스트 탐색)\9. 봉우리'
# sys.stdin=open(currentPath+'\\input.txt', 'rt')

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
# arr=[list(map(int,input().split()))] * num

# print(arr)

cnt=0
for i in range(len(arr)):
    for j in range(len(arr)):
        left=999
        right=999

        up=999
        down=999

        if i==0:
            up=0
        else:
            up=arr[i-1][j]

        if j==0:
            left=0
        else:
            left=arr[i][j-1]

        if i==len(arr)-1:
            down=0
        else:
            down=arr[i+1][j]

        if j==len(arr)-1:
            right=0
        else:
            right=arr[i][j+1]

        if arr[i][j] > left:
            if arr[i][j] > right:
                if arr[i][j] > down:
                    if arr[i][j] > up:
                        cnt+=1
print(cnt)

        

