function solution(K, A) {
    // write your code in JavaScript (Node.js 8.9.4)

    let n = A.length;
    let slices = 0;

    if (n < 1 || n > 100000) {
        console.log("Error: the size of A should be within the range [1..100,000");
        return;
    }

    console.log(A);
    let sortedA = A.map(function(o, i) {
                            return {idx: i, obj: o}; })
                    .sort(function(a, b) {
                    // console.log('a.idx:', a.idx, 'b.idx:', b.idx);
                    return a.obj - b.obj; });
    console.log(sortedA);
    let idxList = [];
    let objList = [];
    for (let i = 0; i < n; i++) {
        idxList.push(sortedA[i].idx);
        objList.push(sortedA[i].obj);
    }

    console.log(idxList);
    console.log(objList);

    for (let i = 0; i < n; i++) {
        for (let j = i; j < n; j++) {
            objList.slice(i, j);
            if (Math.abs(objList[i] - objList[j]) <= K) {
                console.log(idxList[i], idxList[j]);
                console.log(objList[i], objList[j]);
                console.log("----");

                slices += 1;
            }
        }

    } 

    if (slices > 1000000000) {
        return 1000000000;
    }

    return slices;
}
