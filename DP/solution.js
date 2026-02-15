// Problem:- Find the number of ways the target can be achieved using each of the given coins at most once
// ex - coins=[1,2,4,5,6]; target=18;

function targetCount(coins,target){
    let waysCount=new Array(target+1).fill(0);
    waysCount[0]=1;
    for (i of coins){
        for(let j=target;j>=i;j--){
            if(waysCount[j-i]!==0){
                waysCount[j]+=waysCount[j-i]
            }
        }
    }
    return waysCount[target]
}

console.log(targetCount([1,2,4,5,6],18))
// ans = [ 1, 1, 1, 1, 1, 2, 3, 3, 2, 2, 2, 3, 3, 2, 1, 1, 1, 1, 1], 1