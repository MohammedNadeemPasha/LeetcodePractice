//  Problem:- Given an array of positive integers nums and an integer target. Assign either a + or - sign to each element in nums 
//  and Return the number of different ways to assign the signs to reach the target sum
//  Input: nums = [1, 1, 1, 1, 1], target = 3; O/P ->5

function waysToReachTarget(nums,target){
    let queue=[0];
    for (let i of nums){
        let length = queue.length;
        for(j=0;j<length;j++){
            let num = queue.shift();
            queue.push(num+i)
            queue.push(num-i)
        }
    }
    let count=0;
    for(let k of queue){
        if(k ===target){count++}
    }
    return count
}

console.log(waysToReachTarget([1, 2, 7, 9, 981],100))
// O/P->0