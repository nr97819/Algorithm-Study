import sys
#sys.stdin=open('input.txt', 'rt')

n,m=map(int, input().split())

arr=[0]*100
for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i+j]+=1

# for i in range(100):
#     print(arr[i], end=', ')

# print()
# print()

max=max(arr)
for i in range(100):
    if max==arr[i]:
        print(i, end=' ')

print()