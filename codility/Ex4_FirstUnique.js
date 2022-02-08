// O(n^2)

function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    let n = A.length;
    let value;
    let isUnique = true;
    let repeated = [];

    if (n < 1 || n > 100000) {
        console.log("Error: size of A should be within the range [1..100,000]");
        return;
    }
    for (let i = 0; i < n; i++) {
        value = A[i];
        // console.log(value);
        if (repeated.includes(value)) {
            // console.log("repeated");
            continue;
        }
        for (let j = i + 1; j < n; j++) {
            if (value == A[j]) {
                isUnique = false;
                repeated.push(value);
                // console.log("add to repeated: ", repeated);
                break;
            }
        }
        if (isUnique == true) {
            return value;
        }
        isUnique = true;
    }
    return -1;
}

// faster version using map

function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    let mapA = new Map();
    let n = A.length;

    if (n < 1 || n > 100000) {
        console.log("Error: size of A should be within the range [1..100,000]");
        return;
    }
    for (let i = 0; i < n; i++) {
        if (mapA.has(A[i])) mapA.set(A[i], mapA.get(A[i]) + 1);
        else mapA.set(A[i], 1);
    }

    for (let i = 0; i < n; i++) {
        if (mapA.get(A[i]) == 1) {
            return A[i];
        }
    }

    return -1;

}
