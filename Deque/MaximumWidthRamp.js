// Problem:-Given an integer array nums, return the maximum width (j - i) such that i < j and nums[i] <= nums[j]. 
// If none exists, return 0.
// ex:- nums = [6,0,8,2,1,5]; O/P -> 4

function maximumRamp(nums){
    let deque=[],max_ramp=0
    deque.unshift(nums.length-1)
    for(let i =nums.length-2;i>=0;i--){
        if (nums[i]>=nums[deque[0]]){
            deque.unshift(i)           
        }
    }
    for(let i=0;i<nums.length;i++){
        while(deque.length && nums[i]<=deque[0]){
            max_ramp=Math.max(max_ramp,deque[0]-i)
            deque.shift();
        }
    }
    return max_ramp
}

console.log(maximumRamp([6,0,8,2,1,5])) // O/P -> 4
console.log(maximumRamp([1,0])) // O/P -> 0