import sys
# sys.stdin=open('input.txt', 'rt')

n,k=map(int, input().split())
arr=list(map(int, input().split()))

result=set()
for i in range(n):
    for j in (range(i+1, n)):
        for m in range(j+1, n):
            temp=arr[i]+arr[j]+arr[m]
            result.add(temp)

result=list(result)
result.sort(reverse=True)
print(result[k-1])

# arr.sort(reverse=True)
# print(arr[2])