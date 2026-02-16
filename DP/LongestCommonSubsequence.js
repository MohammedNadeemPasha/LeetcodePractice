// Problem: Find the longest common subsequence of the given strings
// str1= 'abcadeac' , str2 = 'cafwuabdc'

let str1 = 'abcadeac' , str2 = 'cafwuabdc';

function longestCommonSubsequence(str1,str2){
    let dp = new Array(str2.length + 1).fill(0).map(() => new Array(str1.length + 1).fill(0));
    for (let i =1; i<str2.length+1;i++){
        for (let j=1;j<str1.length+1; j++){
            if(str2[i-1]===str1[j-1]){
                dp[i][j] = 1+dp[i-1][j-1]
            }
            else{
                dp[i][j] = Math.max(dp[i][j-1],dp[i-1][j])
            }
        }
    }
    return dp[str2.length][str1.length]
}

console.log(longestCommonSubsequence(str1,str2))