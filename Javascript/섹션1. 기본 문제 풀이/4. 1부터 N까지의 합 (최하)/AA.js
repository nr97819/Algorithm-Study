// A, B, C 세 수만을 입력 받는 문제
function solution(num){
    let answer=0
    
    for(let i=1; i<num+1; i++){
        answer+=i
    }
    return answer
}
console.log(solution(6))