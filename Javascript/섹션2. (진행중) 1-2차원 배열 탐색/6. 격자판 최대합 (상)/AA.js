function solution(num, arr){
    
    let sum1=0
    let sum2=0
    let max=0

    // 수직,수평의 합
    for(let i=0;i<n;i++){
        for(let j=0;j<n;j++){
            sum1+=arr[i][j]
            sum2+=arr[i][j]
        }
        if(sum1>max) max=sum1
        if(sum2>max) max=sum2
        sum1=0
        sum2=0
    }

    // 대각선의 합
    for(let i=0;i<n;i++){
        sum1+=arr[i][i]
        sum2+=arr[i][n-i-1]
        if(sum1>max) max=sum1
        if(sum2>max) max=sum2
    }

    return max
}
let arr=[]
let n=5

arr.push([10, 13, 10, 12, 15])
arr.push([12, 39, 30, 23, 11])
arr.push([11, 25, 50, 53, 15])
arr.push([19, 27, 29, 37, 27])
arr.push([19, 13, 30, 13, 19])

console.log(solution(n, arr))