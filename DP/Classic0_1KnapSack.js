// Problem:- Given an array of weights w[] and its associated values v[], calculate the maximum value for the capacity c.
//weights = [1,3,4,5], values = [1,4,5,7], capacity = 7

function knapSack(weights,values,capacity){
    let dp = new Array(capacity+1).fill(0);
    for(let i=0;i<weights.length;i++){
        for(j=capacity;j>=weights[i];j--){
            dp[j]=Math.max(dp[j],dp[j-weights[i]]+values[i])
        }
    }
    return dp[capacity],dp
}

console.log(knapSack([1,3,4,5],[1,4,5,7],7))
// o/p-> [0, 1, 1, 4, 5, 7, 8, 9]