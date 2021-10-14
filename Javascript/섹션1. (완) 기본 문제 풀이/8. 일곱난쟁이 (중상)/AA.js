// A, B, C 세 수만을 입력 받는 문제
function solution(arr){
    let answer=""
    
    let sum=0
    for(let i=0;i<arr.length;i++){
        sum+=arr[i]
    }
    let minus=sum-100

    let a=0
    let b=0
    let plus=0
    for(let i=0;i<arr.length;i++){
        for(let j=i+1;j<arr.length;j++){
            if(plus=arr[i]+arr[j] == minus){
                a=arr[i]
                b=arr[j]       
            }
            plus=0
        }
    }
    console.log(a)
    console.log(b)
    let temp=[]
    for(let i=0;i<arr.length;i++){
        if(arr[i]==a || arr[i]==b){
            continue
        }
        temp.push(arr[i])
    }
    console.log(temp)
    for(let i=0;i<temp.length+6;i++){ // 이거 어떻게함?
        answer+=temp.pop()
        answer+=' '
    }
    return answer
}
//str="12 12 13 13 18 18 14 3 4" -> 3,4
str="20 7 23 19 10 15 25 8 13"
arr=str.split(" ")
for(let i=0;i<arr.length;i++){
    arr[i]=parseInt(arr[i])
}
console.log(solution(arr))