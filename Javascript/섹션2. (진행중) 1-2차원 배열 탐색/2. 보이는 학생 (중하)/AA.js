function solution(num, a, b){
    let answer=[]
    
    for(let i=0;i<num;i++){
        if(a[i]==b[i]){
            console.log('D')
        }
        else if(a[i]==1){
            if(b[i]==2){
                console.log('B')
            }
            else if(b[i]==3){
                console.log('A')
            }
        }
        else if(a[i]==2){
            if(b[i]==1){
                console.log('A')
            }
            else if(b[i]==3){
                console.log('B')
            }
        }
        else if(a[i]==3){
            if(b[i]==1){
                console.log('B')
            }
            if(b[i]==2){
                console.log('A')
            }
        }
    }

    return answer
}
let a=[2, 3, 3, 1, 3];
let b=[1, 1, 2, 2, 3];
// arr=str.split(' ')
//console.log(solution(5, a, b))
solution(5, a, b)