import sys
sys.stdin=open('input.txt', 'rt')

n=int(input())
arr=list(map(int, input().split()))

temp=''
nums=[0]*100

def isPrime(a):
    flag=True
    for i in range(2, len(arr)+1):
        if a%i==0:
            flag=False
            break
    if flag:
        print(a, end=' ')

for i in range(len(arr)):
    num=arr[i]
    temp=str(num)
    temp2=''
    for j in range(len(temp)):
        temp2.__add__(temp[len(temp)-1:])
    reverse=int(temp2)

    isPrime(reverse)

