function solution(num, arr){
    let answer=[]
    
    for(let i in arr){
        flag=false

        s=arr[i]
        for(let j=0;j<i;j++){
            if(s==arr[j]){
                flag=true
                break        
            }
        }
        if(flag){
            continue
        }
        answer.push(s)
    }

    return answer
}
let arr=['good',
    'time',
    'good',
    'time',
    'student',
    'fruit',
    'student',
    'time']
console.log(solution(5, arr))