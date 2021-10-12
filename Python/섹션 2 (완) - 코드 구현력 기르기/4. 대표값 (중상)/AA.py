import sys
#sys.stdin=open('input.txt', 'rt')

n=input()
arr=list(map(int,input().split()))

sum=0
for e in arr:
    sum+=e
avg=sum/len(arr)
avg=round(avg)

resNum=0
min=float('inf')
maxValue=0
for i in range(len(arr)):
    if min > abs(avg-arr[i]):
        min = abs(avg-arr[i])
        resNum = i
        maxVal = arr[i]

    elif min == abs(avg-arr[i]):
        if maxVal < arr[i]: # 점수가 더 높은 학생
            min = abs(avg-arr[i])
            resNum = i
            maxVal = arr[i]
        elif  maxVal == arr[i]:
            if resNum > i: # 순서가 더 빠른 학생
                min = abs(avg-arr[i])
                resNum = i
                maxVal = arr[i]

# print(arr[resNum], resNum+1)
print(avg, resNum+1)
