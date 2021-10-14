function solution(str){
    let answer=''
    
    let temp=''
    let cnt=0
    for(let x of str){
        cnt++
        if(cnt==1 || cnt==str.length){
            continue
        }
        temp+=x
    }
    answer=temp
    return answer
}
let str="canyoulookatme?"
console.log(solution(str))