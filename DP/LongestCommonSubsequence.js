// Problem: Find the longest common subsequence of the given strings
// str1= 'abcadeac' , str2 = 'cafwuabdc'

let str1 = 'abcadeac' , str2 = 'cafwuabdc';

function longestCommonSubsequence(str1,str2){
    let dp = new Array(str2.length + 1).fill(0).map(() => new Array(str1.length + 1).fill(0));
    for (let i =0; i<str2.length;i++){
        for (let j=0;j<str1.length; j++){
            if(str2[i]===str1[j]){
                dp[i+1][j+1] = 1+dp[i][j]
            }
            else{
                dp[i+1][j+1] = Math.max(dp[i][j+1],dp[i+1][j])
            }
        }
    }
    return dp[str2.length][str1.length]
}

console.log(longestCommonSubsequence(str1,str2))