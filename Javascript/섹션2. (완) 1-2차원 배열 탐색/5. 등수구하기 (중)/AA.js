function solution(num, arr){
    
    let result=[]
    let cnt=0
    for(let i=0;i<num;i++){
        cnt=0
        now=arr[i]
        for(let j=0;j<num;j++){
            if(now==arr[j]) continue
            if(now<arr[j]){
                cnt++
            }
        }
        result.push(cnt+1) // 등수니까 +1
    }

    return result
}
let arr=[87, 89, 92, 100, 76];
console.log(solution(5, arr))