function solution(str){

    str=str.toLowerCase()

    let temp=''
    for(e of str) {
        temp=e+temp
    }
    
    let flag=true
    for(i in str){
        if(str.charCodeAt(i)<97 || str.charCodeAt(i)>122){
            continue
        }
        if(temp.charCodeAt(i)<97 || temp.charCodeAt(i)>122){
            continue
        }

        if(str[i] == temp[i]){
            console.log(str[i]+', '+temp[i])
            continue
        }
        else{
            flag=false
            break
        }
    }

    console.log(str)
    console.log(temp)

    if(flag){
        return 'YES'
    }
    else{
        return 'NO'
    }
}
let str="found7, time: study; Yduts; emit, 7Dnuof"
console.log(solution(str))