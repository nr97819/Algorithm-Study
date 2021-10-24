# 이동 함수
def move(arr,line,dir):
    # 좌측으로 이동
    if dir==0:
        temp=arr[line][0]
        for i in range(len(arr)-1):
            arr[line][i]=arr[line][i+1]
        arr[line][len(arr)-1]=temp
        
    # 우측으로 이동
    elif dir==1:
        temp=arr[line][len(arr)-1]
        for i in range(len(arr)-2):
            print(arr[line][i])
            arr[line][i+1]=arr[line][i]
        print(arr)
        arr[line][0]=temp
        print(arr)

    else:
        print('error!!')

    return arr
    

# 명령어 수 만큼 반복
arr=[[1,2,3,4,5,6,7,8,9]]
line=0
move(arr,line,1)

print(arr)
