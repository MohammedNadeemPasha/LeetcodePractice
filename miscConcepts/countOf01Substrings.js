// Problem:- Given a binary string s (a string consisting of only 0s and 1s), count the number of substrings that have:
// (1) Equal number of 0s and 1s`, and (2) All the 0s and all the 1s are grouped consecutively. (0011)✔ ; (0101)❌ -> (01),(01)✔
// String = "00110011" 0/p -> 6 (2 pointer method)

function countOfSubstring(string){
    let curr_counter=1,prev_counter=0,count=0;

    for(let i=1;i<string.length;i++){
        if(string[i]===string[i-1]){
            curr_counter++
        }
        else{
            count +=Math.min(prev_counter,curr_counter);
            prev_counter=curr_counter;
            curr_counter=1
        }
    }
    return count+Math.min(curr_counter,prev_counter)
}

console.log(countOfSubstring("010101"))
// O/P -> 5
