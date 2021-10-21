function solution(str){
    let temp=''
    let p=''
    
    str=str.toLowerCase()
    for(e of str) {
        temp=e+temp
    }
    if(str==temp){
        p=('YES')
    }
    else{
        p=('NO')
    }
    return p
}
let str="2gooG2"
console.log(solution(str))