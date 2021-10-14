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