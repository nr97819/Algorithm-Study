// A, B, C 세 수만을 입력 받는 문제
function solution(a, b, c){
    let answer;
    
    let cnt=0;
    if(a+b<c) cnt++;
    if(a+c<b) cnt++;
    if(b+c<a) cnt++;

    if(cnt>=1)
        answer='NO';
    else
        answer="YES";

    return answer;
}
console.log(solution(6,7,11));