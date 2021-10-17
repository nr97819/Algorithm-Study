import sys
#sys.stdin=open('input.txt', 'rt')

num=int(input())
arr=[list(map(int,input().split())) for _ in range(num)]
# arr=[list(map(int,input().split()))] * num

# 테스트 출력용
# for x in arr:
#     print(x)

max=0
# 가로 합 (O(n))
# 세로 합 (O(n))
# -> 같이 진행되므로, O(2n^2)이 아닌, (n^2)의 복잡도
for i in range(num):
    sum1=sum2=0 # 한번에 초기화
    for j in range(num):
        sum1+=arr[i][j]
        sum2+=arr[j][i]
    if max<sum1:
        max=sum1
    if max<sum2:
        max=sum2

# 대각선 합 (O(2) - 상수 복잡도)
sum1=0
sum2=0
for i in range(num):
    sum1+=arr[i][i]
    sum2+=arr[num-i-1][i]
if max<sum1:
    max=sum1
if max<sum2:
    max=sum2

print(max)