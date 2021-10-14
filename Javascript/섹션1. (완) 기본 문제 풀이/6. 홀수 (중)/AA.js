// A, B, C 세 수만을 입력 받는 문제
function solution(arr){
    let min=100

    let sum=0
    for(let i=0;i<arr.length;i++){
        if(arr[i]%2==1){
            sum+=arr[i]
            if(min>arr[i]){
                min=arr[i]
            }
        }
    }
    console.log(sum)

    return min
}
str="12 77 38 41 53 92 85"
arr=str.split(" ")
for(let i=0;i<arr.length;i++){
    arr[i]=parseInt(arr[i])
}
console.log(solution(arr))