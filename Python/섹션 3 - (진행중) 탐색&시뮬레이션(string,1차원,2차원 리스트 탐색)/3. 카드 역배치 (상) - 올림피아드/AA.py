import sys
#sys.stdin=open('input.txt', 'rt')

arr=list(range(1,21))

for i in range(10):
    ai, bi=map(int,input().split())
    ai-=1


    temp=arr[ai:bi]
    temp.reverse()
    j=0
    for i in range(ai, bi):
        arr[i]=temp[j]
        j+=1

for x in arr:
    print(x, end=" ")