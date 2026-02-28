// Problem:- Given a rotated sorted array, find tge minimum value in the array
// I/P -> [4,5,6,7,0,1,2] ; O/P -> 0

function minimumRotatedArray(nums){
    let left=0;right=nums.length-1;
    while(left<right){
        mid=Math.floor((left+right)/2);
        if(nums[left]<nums[right] && nums[left]<nums[mid]){
            right=mid-1
        }
        else if(nums[right]<nums[left] && nums[right]<nums[mid]){
            left=mid+1
        }
        else {right =mid}
    }
    return nums[left]
}

console.log(minimumRotatedArray([4,5,6,7,0,1,2]))
// O/P ->0