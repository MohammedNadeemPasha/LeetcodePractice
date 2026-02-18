// Problem - Calculate all distinct subsequences of a string
//ex - s='abca' -> 15


let s = 'abca'

const subsequencesOfString = (s) =>{
    let dp = new Array(s.length+1).fill(0);
    dp[0]=1
    let map = {}
    for(let i=1;i<s.length+1;i++){
        dp[i]=2*dp[i-1];
        if (s[i-1] in map){
            dp[i] -=dp[map[s[i-1]]-1]
        }
        map[s[i-1]]=i
    }
    return dp[s.length]
}

console.log(subsequencesOfString(s))