// Problem: We have to find common subsequence occurances in two Strings ex - "ac","ac" -> 'a','c','ac'
// Test case:- q='acayunc' , r = 'ac'

let q="acayunc",r="ac"

const CommonSubsequenceOfTwoStrings = (q,r) =>{
    let dp = new Array(r.length+1).fill(0).map((x)=> new Array(q.length+1).fill(0));
    for (let i=1;i<r.length+1;i++){
        for(let j=1;j<q.length+1;j++){
            if(r[i-1]===q[j-1]){
                dp[i][j]= 1+dp[i-1][j]+dp[i][j-1]
            }
            else{
                dp[i][j]= dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]
            }
        }
    }
    return dp[r.length][q.length],dp
}

console.table(CommonSubsequenceOfTwoStrings(q,r))