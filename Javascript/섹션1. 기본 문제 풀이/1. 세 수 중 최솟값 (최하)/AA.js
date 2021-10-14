// A, B, C 세 수만을 입력 받는 문제
function solution(a, b, c){
    let answer
    if(a<b) answer=a;
    else answer=b;
    if(c<answer) answer=c;
    
    return answer;
}

console.log(solution(6, 5, 11));