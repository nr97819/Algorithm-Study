import sys
#sys.stdin=open('input.txt', 'rt')

# 개수 입력
n=int(input())

# 문자열 여러 줄 입력 [신기술]
arr=[input() for _ in range(n)]

for i in range(len(arr)):
    temp=''
    for c in arr[i]:
        temp=c+temp

    # 형식 출력    
    print('#%d'%(i+1), end=' ') 
    
    # 대소문자 구분 제거
    if arr[i].lower() == temp.lower():
        print('YES')
    else:
        print('NO')