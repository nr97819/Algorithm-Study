function solution(day, arr){
    let answer=0
    let cnt=0
    for(let i=0;i<arr.length;i++){
        if (arr[i]%10==day){
            cnt++
        }
    }
    answer=cnt
    return answer
}

arr=[12, 20, 54, 30, 87, 91, 30]
console.log(solution(0, arr))