// A, B, C 세 수만을 입력 받는 문제
function solution(arr){
    let answer
    
    answer=arr[0]
    for(let i=0;i<arr.length;i++){
        if(answer>arr[i]){
            answer=arr[i]
        }
    }
    return answer
}
let arr=[5, 999, 1024, 2048, 11, 2, 15, 17]
console.log(solution(arr))