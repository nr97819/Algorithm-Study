import sys
#sys.stdin=open('input.txt', 'rt')

n=int(input())
arr1=list(map(int, input().split()))

m=int(input())
arr2=list(map(int, input().split()))

temp=''

arr=arr1+arr2
arr.sort()
for n in arr:
    temp+=str(n)+' '

print(temp)

