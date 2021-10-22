function solution(num, arr){
    let answer=[]
    
    for(let i=0;i<num;i++){
        if(i==0) {
            answer.push(parseInt(arr[i]))
            continue
        }
        value=parseInt(arr[i])
        lastValue=parseInt(arr[i-1])
        
        if(value>lastValue){
            answer.push(value)
        }
    }

    return answer
}
let str="130 135 148 140 145 150 150 153"
arr=str.split(' ')
console.log(solution(8, arr))