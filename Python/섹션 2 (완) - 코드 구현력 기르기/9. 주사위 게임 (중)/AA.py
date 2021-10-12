import sys
#sys.stdin=open('input.txt', 'rt')

# 개수 n 입력 받기
n=int(input())

result=list()
for i in range(n):
    # 입력 3개 리스트에 받기
    arr=list(map(int, input().split()))

    cnt=0
    temp=0
    if arr[0]==arr[1]:
        cnt+=1
        if arr[1]==arr[2]:
            cnt+=1
        else:
            if arr[0]==arr[2]:
                cnt+=1
    else:
        if arr[1]==arr[2]:
            cnt+=1
            temp=arr[1]
        if arr[0]==arr[2]:
            cnt+=1
            temp=arr[0]

                
    if cnt==2:
        result.append(10000+arr[0]*1000)
    elif cnt==1:
        result.append(1000+temp*100)
    elif cnt==0:
        result.append(100*max(arr))
    else:
        print("에러 발생!")

print(max(result))
