// Problem:- Given an unsorted integer array nums, return the smallest positive integer that is not present in nums.
// ex:- [3,4,-1,1] ; O/P -> 2


function missingPositive(nums){
    let i=0;
    while(i<nums.length){
        if(nums[i]===i+1 || nums[i]>nums.length || nums[i]<=0 || nums[i] === nums[nums[i]-1] ) {i++;continue}
        let temp = nums[nums[i]-1]
        nums[nums[i]-1] = nums[i]
        nums[i] = temp
    }
    for(let i=0;i<nums.length;i++){
        if(nums[i]!== i+1){return i+1}
    }
    return nums.length+1

}

console.log(missingPositive([3,4,-1,1])) // O/P ->2
console.log(missingPositive([1,1])) // O/P -> 2
console.log(missingPositive([7,8,9,11,12])) // O/P -> 1