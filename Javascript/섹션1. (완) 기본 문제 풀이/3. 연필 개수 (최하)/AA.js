// A, B, C 세 수만을 입력 받는 문제
function solution(num){
    let answer
    
    if(num%12==0){
        answer=parseInt(num/12)
    }
    else{
        answer=parseInt(num/12)+1
    }
    
    return answer
}
console.log(solution(178))