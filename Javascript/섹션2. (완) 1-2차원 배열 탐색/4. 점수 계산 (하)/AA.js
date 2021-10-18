function solution(num, arr){
    let sum=0
    let cnt=0

    let score=0
    for(let i=0;i<num;i++){
        score=arr[i]
        if(score==1){
            cnt++
            sum+=cnt
        }
        else if(score==0){
            cnt=0
        }
    }

    return sum
}
let arr=[1, 0, 1, 1, 1, 0, 0, 1, 1, 0];
console.log(solution(10, arr))