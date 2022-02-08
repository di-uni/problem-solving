function solution(S) {
    // write your code in JavaScript (Node.js 8.9.4)
    let n = S.length;
    let stack = [];
    if (n < 0 || n > 1000000) {
        console.log("Error: size of A should be within the range [0..1,000,000]");
        return;
    }

    for (let i = 0; i < n; i++) {
        if (S[i] == "(") {
            stack.push(")");
        }
        if (S[i] == ")") {
            if (stack.pop() != ")") {
                return 0;
            }
        }
    }

    if (stack.length == 0) {
        return 1;
    }
    return 0;
}