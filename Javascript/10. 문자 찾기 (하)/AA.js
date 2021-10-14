function solution(text, char){

    let cnt=0
    let c=''
    for(let i=0;i<text.length;i++){
        if(text[i]==char)
            cnt++
    }
    
    return cnt
}
console.log(solution("BANANA", 'A'))
//console.log(solution("APPLICATION")) -> 2