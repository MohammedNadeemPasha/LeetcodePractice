// Problem:- Given an array, coins, and amount, return minumim number of coins needed to reach the amount
// coins = [1,2,5]; amount = 11;

function minimumCoins(coins,amount){
    let dp = new Array(amount+1).fill(Infinity);
    dp[0]=0;
    for (coin of coins){
        for(let i=coin; i<=amount; i++){
            dp[i]=Math.min(dp[i],dp[i-coin]+1)
        }
    }
    if(dp[amount]===Infinity) return -1
    return dp[amount]
}

console.log(minimumCoins([1,2,5],11))
// o/p -> [ 0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3 ] , 3
// i/p -> [2,5]; o/p -> [ 0, Infinity, 1, Infinity, 2, 1, 3, 2, 4, 3, 2, 4 ], 4