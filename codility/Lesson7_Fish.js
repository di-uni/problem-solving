function solution(A, B) {
    // write your code in JavaScript (Node.js 8.9.4)
    let downstream_fish = [];
    let upstream_fish = 0;
    let n = A.length;

    for (let i = 0; i < n; i++) {
        let fishSize = A[i];
        if (B[i] == 1) {
            downstream_fish.push(fishSize);
        }
        else {
            if (downstream_fish.length == 0) {
                upstream_fish += 1;
            } 
            else {
                for (let j = 0; j < downstream_fish.length; j++) {
                    let pop = downstream_fish.pop();
                    if (fishSize < pop) {
                        downstream_fish.push(pop);
                        break;
                    }
                }
                if (downstream_fish.length == 0) {
                    upstream_fish += 1;
                } 
            }
        }
    }
    // console.log(upstream_fish);
    // console.log(downstream_fish.length);
    return upstream_fish + downstream_fish.length;
}