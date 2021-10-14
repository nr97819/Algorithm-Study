function solution(arr, num){
    let answer=''
    
    let tempStr=''
    let max=0
    for(let i=0;i<num;i++){
        s=arr[i]
        if(max<s.length){
            max=s.length
            tempStr=s
        }
    }
    answer=tempStr
    return answer
}
let arr=["teacher", "time", "student", "beautiful", "good"];
console.log(solution(arr, arr.length));