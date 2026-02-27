// Problem:-integer array nums, find a peak element, and return its index. If the array contains multiple peaks, 
// return the index to any of the peaks.
// ex:- [1,2,1,3,5,6,4], O/P-> 1 or 5

var findPeakElement = function(nums) {
    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        let mid = Math.floor((left + right) / 2);

        if (nums[mid] < nums[mid + 1]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
};