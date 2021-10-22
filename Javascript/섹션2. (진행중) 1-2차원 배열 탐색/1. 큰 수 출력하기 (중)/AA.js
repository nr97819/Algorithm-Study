function solution(num, arr){
    let answer=[]
    
    // 문자열로 비교해서, '12'에는 '1'이 있어서, 사전 순서가 더 빠른 취급
    for(let i=0;i<arr.length;i++){
        preValue=parseInt(arr[i]) // 변환
        if(i==0) {
            answer.push(preValue)
            continue
        }
        lastValue=parseInt(arr[i-1]) // 변환 (에러 방지해서, 여기에서 parse 함 (감으로..))
        
        if(preValue>lastValue){
            answer.push(preValue)
        }
    }

    return answer // [7, 9, 6, 12] 배열로 출력
}
let str="7 3 9 5 6 12"
arr=str.split(' ')
console.log(solution(6, arr))