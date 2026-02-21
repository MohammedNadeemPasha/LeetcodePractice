// Problem :- Find elements that are maximum from their index to the right end
//  arr = [16,17,4,5,3,2] 
//Intuition - Moving left to right we'd ahave to calculate max per each element, since question's asking about calculating from 
//            index to right end, reverse the direction of traversal -> [1,2,3,5] -> [5,3,2,1]

function maximum(arr){
    let res = [], max =0;
    for(let i=arr.length-1;i>=0;i--){
        if(arr[i]>max){
            res.push(arr[i])
            max = arr[i]
        }
    }
    return res
}

console.log(maximum([16,17,4,5,3,2]))
// o/p -> [ 2, 3, 5, 17 ]