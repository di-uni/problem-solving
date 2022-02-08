function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    let n = A.length;
    if (n < 1 || n > 200000) {
        console.log("Error: size of A should be within the range [1...200,000]");
        return;
    }
    
    let idx = 0;
    let result = 0;
    while(idx != -1) {
        idx = A[idx];
        result += 1;
    }
    return result;
}
