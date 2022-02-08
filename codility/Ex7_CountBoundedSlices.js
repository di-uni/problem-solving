function solution(K, A) {
    let n = A.length;
    let slices = 0;

    if (n < 1 || n > 100000) {
        console.log("Error: the size of A should be within the range [1..100,000");
        return;
    }

    let temp = null;
    let max = 0;
    let min = 0;

    for (let i = 0; i < n; i++) {
        max = A[i];
        min = A[i];
        for (let j = i; j < n; j++) {
            temp = A.slice(i, j + 1);
            if (A[j] > max) max = A[j];
            if (A[j] < min) min = A[j];
            // if ((Math.max(...temp) - Math.min(...temp)) <= K) {
            if ((max - min) <= K) {
                slices += 1;
            }
            else {
                break;
            }
        }

    } 

    if (slices > 1000000000) {
        return 1000000000;
    }

    return slices;
}