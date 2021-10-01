import sys
sys.stdin=open('input.txt', 'rt')

arr=[0]*200000
num=int(input())

for d in range(1, num+1):
    if num%d==0:
        arr[d]=1

for i in range(1, num+1):
    if arr[i]==1:
        print(i)
