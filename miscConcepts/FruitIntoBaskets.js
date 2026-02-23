// Problem :- Find the length of the longest contiguous subarray that contains at most 2 distinct elements
// arr = [1,2,3,2,2] -> Output = 4

// My solution
function maxconsecutive(nums) {
  let k = 0,j = 0,count = 2,map = new Set(),result=0;
  for (let i = 0; i < nums.length; i++) {
    if (!map.has(nums[i]) && count !== 0) {
      map.add(nums[i]);
      count--;
    }
    if (!map.has(nums[i]) && count === 0) {
      result = Math.max(result, i - k);
      map.clear();
      k = j;
      map.add(nums[k]);
      map.add(nums[i]);
    }
    if(count===0 && nums[i]!=nums[i-1])
    {
        j=i
    }
  }
  result = Math.max(result,nums.length - k)
  return result
}

console.log(maxconsecutive([1,2,3,2,2])) // O/P -> 4

// Simpler Solution

function LongestConsecutive(nums){
    let left = 0, map ={},result=0;

    for(let right=0;right<nums.length;right++){
        map[nums[right]] = (map[nums[right]] || 0) + 1;

        while(Object.keys(map).length >2){
            map[nums[left]]--;
            if (map[nums[left]]===0){
                delete map[nums[left]]
            }
            left++
        }
        result = Math.max(result,right-left+1)
    }
    return result
}

console.log(LongestConsecutive([1,2,3,2,2]))