// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    let n = A.length;
    let inversion = 0;

    if (n < 0 || n > 100000) {
        console.log("Error: the size of A should be within the range [0..100,000");
        return;
    }

    // console.log(A);
    let sortedA = A.map(function(o, i) {
                            return {idx: i, obj: o}; })
                    .sort(function(a, b) {
                    // console.log('a.idx:', a.idx, 'b.idx:', b.idx);
                    return b.obj - a.obj; });
    // console.log(sortedA);
    let idxList = [];
    let objList = [];
    for (let i = 0; i < n; i++) {
        idxList.push(sortedA[i].idx);
        objList.push(sortedA[i].obj);
    }

    // console.log(idxList);
    // console.log(objList);

    for (let i = 0; i < n - 1; i++) {
        for (let j = i + 1; j < n; j++) {
            if (objList[i] == objList[j]) {
                continue;
            }
            if (idxList[i] < idxList[j]) {
                // console.log(idxList[i], idxList[j]);
                inversion += 1;
            }
        }
    }
    return inversion;
}
