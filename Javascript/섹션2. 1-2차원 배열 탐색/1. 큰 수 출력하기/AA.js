function solution(num, arr){
    let answer=[]
    
    for(let i=0;i<arr.length;i++){
        console.log(i)
        if(i==0) {
            answer.push(arr[i])
            continue
        }
        console.log(arr[i], arr[i-1])
        console.log(arr[i] > arr[i-1])
        
        if(arr[i+100]>arr[i-1]){
            answer.push(arr[i])
            console.log(answer)
        }
    }

    return answer
}
let str="7 3 9 5 6 12"
arr=str.split(' ')
console.log(solution(6, arr))