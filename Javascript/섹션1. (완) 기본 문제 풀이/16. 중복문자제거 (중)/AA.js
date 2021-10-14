function solution(str){
    let answer=''
    let flag=false
    let temp=''
    for(let i in str){
        flag=false
        for(let j=0;j<i;j++){
            if(str[i]==str[j]){
                flag=true
                break
            }
        }
        if(flag){
            continue
        }
        temp+=str[i]
    }
    answer=temp
    return answer
}
let str="ksekksetttssseeeaaaaaaaaaaaaaaaht" // ksetah
console.log(solution(str))