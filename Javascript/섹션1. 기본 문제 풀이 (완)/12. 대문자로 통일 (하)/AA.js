function solution(str){
    answer=''
    for(let x of str){
        answer+=(x.toUpperCase())
    }
    return answer
}
str="ItisTimeToStudy"
console.log(solution(str))