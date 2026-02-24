// Problem:- Given a string find all the valid IP addresses, each integer must be between 0 and 255 
// s = "25525511135"; O/P -> ["255.255.11.135","255.255.111.35"]

function validAddresses(s) {
    let result = [];
    calculateSubstring("", 4, s, result);
    return result;
}

function calculateSubstring(current, count, remaining, result) {
    if (count === 0) {
        if (remaining === "") {
            result.push(current.slice(0, -1)); 
        }
        return;
    }

    const n = remaining.length;
    const minLen = Math.max(1, n - 3 * (count - 1));
    const maxLen = Math.min(3, n - (count - 1));
    if (minLen > maxLen) return;

    for (let i = minLen; i <= maxLen; i++) {
        const segment = remaining.slice(0, i);
        if ((segment[0] === '0' && segment.length > 1) || parseInt(segment) > 255) {
            continue;
        }
        calculateSubstring(current + segment + ".", count - 1, remaining.slice(i), result);
    }
}
let result=validAddresses('25525511135')
console.log(result)