// Problem:- Given an integer array nums and an integer k, return the number of non-empty subarrays whose sum is divisible by k.
// (Intuition):- If the prefix sum divided by k appears as the prefix_sum again, then there must be a subarray that's divisible by k
// ex:- [1,5],k=5 - prefix_sums-[1,6], [1,1] since the sum divisble by 5 is 1 again then there must be a subarray whose sum be 5 
// for the sum to get to 1 again.
// ex:- nums = [4,5,0,-2,-3,1], k = 5 ; O/P -> 7


function divisible(nums,k){
    let result=0,prefix=0,dict={0:1};

    for(let i=0;i<nums.length;i++){
        prefix=(prefix+nums[i])%k
        if (prefix<0){prefix+=k}
        if (dict[prefix]){
            result+=dict[prefix]
            dict[prefix]+=1
        }
        else{
            dict[prefix]=1
        }
    }
    console.log(dict)
    return result
}

console.log(divisible([4,5,0,-2,-3,1],5)) // O/P -> 7