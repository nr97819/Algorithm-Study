function solution(text){
    let answer=''
    
    let c=''
    for(let i=0;i<text.length;i++){
        if(text[i]=='A')
            answer+=('#')
        else{
            answer+=(text[i])
        }
    }
    
    return answer
}
console.log(solution("BANANA"))
//console.log(solution("APPLICATION")) -> #PPLIC#TION