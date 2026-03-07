// Problem: Teemo attacks Ashe at times given in a non-decreasing array `timeSeries`. Each attack poisons Ashe for 
// `duration` seconds (interval [t, t + duration - 1]). If another attack happens before the poison ends, the poison 
// timer resets.Return the total number of seconds Ashe remains poisoned.
//  ex1: timeSeries = [1,4], duration = 2  -> O/P: 4


function diff(nums,duration){
    let result=0;
    for (let i=0;i<nums.length-1;i++){
        result+=Math.min(nums[i+1]-nums[i],duration)
    }
    return result+duration
}

console.log(diff([1,4],2)) // O/P -> 4
console.log(diff([1,2],2)) //O/P -> 3
