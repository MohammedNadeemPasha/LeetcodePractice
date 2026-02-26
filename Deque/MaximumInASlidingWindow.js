//Problem:- Given an array of integers nums and a sliding window of size k, return the max of the sliding windows
// ex:- nums = [1,3,-1,-3,5,3,6,7], k = 3 , O/P -> [3,3,5,5,6,7]

function maxInWindows(nums,k){
    if (nums.length === 0 || k === 0 || !nums) return []
    if (k===1) return nums.slice()
    
        let result = [];dq=[];
        for (let i=0;i<nums.length;i++){
            while(dq.length && dq[0]<=i-k){
                dq.shift();
            }
            while(dq.length && nums[dq[dq.length-1]]<=nums[i]) dq.pop()
            dq.push(i)
            if (i >=k-1)result.push(nums[dq[0]])
        }
    return result
}

console.log(maxInWindows([1,3,-1,-3,5,3,6,7],3))