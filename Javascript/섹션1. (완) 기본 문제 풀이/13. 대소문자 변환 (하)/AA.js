function solution(str){
    answer=''
    for(let x of str){
        if(x==x.toUpperCase()){
            answer+=x.toLowerCase()
        }
        else{
            answer+=x.toUpperCase()
        }
    }
    return answer
}
str="StuDY"
console.log(solution(str))