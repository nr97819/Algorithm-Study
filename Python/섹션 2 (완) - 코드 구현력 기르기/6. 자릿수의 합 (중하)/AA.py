import sys
import math as m
#sys.stdin=open('input.txt', 'rt')

n=int(input())
arr=list(map(int,input().split()))

max=0
maxIndex=-1
for i in range(n):
    sum=0
    temp=arr[i]
    while temp>0:  
        sum+=temp%10
        temp=m.floor(temp/10)

    if max<sum:
        max=sum
        maxIndex=i

print(arr[maxIndex])