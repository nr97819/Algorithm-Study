function solution(num, arr){

    let cnt=0
    for(let i=0;i<n;i++){
        for(let j=0;j<n;j++){

            let left=false
            let up=false
            let right=false
            let down=false

            if(i==0){ left=true }
            if(j==0){ up=true }
            if(i==n-1){ right=true }
            if(j==n-1) { down=true }

            mine=arr[i][j]
            if(!left){
                if(arr[i-1][j]<mine){
                    left=true
                }
                else{
                    left=false
                }
            }
            if(!up){
                if(arr[i][j-1]<mine){
                    up=true
                }
                else{
                    up=false
                }
            }
            if(!right){
                if(arr[i+1][j]<mine){
                    right=true
                }
                else{
                    right=false
                }
            }
            if(!down){
                if(arr[i][j+1]<mine){
                    down=true
                }
                else{
                    down=false
                }
            }
            if(left&&up&&right&&down){
                cnt++
            }
        }
    }
    return cnt
}
let arr=[]
let n=5
arr.push([5, 3, 7, 2, 3])
arr.push([3, 7, 1, 6, 1])
arr.push([7, 2, 5, 3, 4])
arr.push([4, 3, 6, 4, 1])
arr.push([8, 7, 3, 5, 2])
console.log(solution(n, arr))