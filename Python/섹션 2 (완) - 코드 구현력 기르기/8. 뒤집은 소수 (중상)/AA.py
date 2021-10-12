import sys
# sys.stdin=open('input.txt', 'rt')

n=int(input())
arr=list(map(int, input().split()))

def isPrime(a):
    flag=True
    for i in range(2, a):
        if a%i==0:
            flag=False
            break
    if flag:
        if a!=1: 
            print(a, end=' ')

for i in range(len(arr)):
    num=arr[i]
    s=str(num)
    temp=''
    for c in s :
        temp=c+temp
    
    reverse=int(temp)
    isPrime(reverse)