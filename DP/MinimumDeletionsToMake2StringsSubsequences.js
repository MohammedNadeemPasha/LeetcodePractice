// Problem: Find the number of deleteions required to make a string subsequence of another string
// ex:- q = "acad" r = "acde" o/p -> 1

const miminumDeletions = (q,r) => {
    let dp = new Array(r.length+1).fill(0).map((x)=> new Array(q.length+1).fill(0));
    for(let i=1;i<r.length+1;i++){
        for(let j=1;j<q.length+1;j++){
            if (r[i-1]===q[j-1]){
                dp[i][j]=1+dp[i-1][j-1]
            }
            else dp[i][j]=Math.max(dp[i-1][j],dp[i][j-1])
        }
    }
    return r.length -dp[r.length][q.length]
}

console.log(miminumDeletions("acad","acde"))