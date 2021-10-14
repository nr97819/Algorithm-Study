// A, B, C 세 수만을 입력 받는 문제
function solution(str){
 
    let cnt=0
    for(let x of str){
        if(x==x.toUpperCase()){
            cnt++
        }
    }
    
    return cnt
}
str="KoreaTimeGood"
console.log(solution(str))