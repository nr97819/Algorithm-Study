import sys 
# sys.stdin=open('input.txt', 'rt')

arr=[]
t = int(input())
for t in range(t):
    n,s,e,k = map(int, input().split())
    arr=list(map(int, input().split()))
    arr=arr[s-1:e]
    arr.sort(reverse=False)
    print('#%d %d' % (t+1, arr[k-1]))