function solution(N, stages) {
    let stages_cnt = new Array(N+1).fill(0);
    stages.forEach(x => stages_cnt[x-1] += 1);
    // console.log(stages_cnt);
    let remains = stages_cnt.reduce((acc, cur) => acc + cur, 0);
    // console.log(remains);
    
    let failure = [];
    for (let i = 1; i < N+1; i++) {
        let stage = {};
        stage.id = i;
        stage.failure_rate = stages_cnt[i-1]/remains;
        remains -= stages_cnt[i-1];
        failure.push(stage);
    }
    // console.log(failure);
    
    failure.sort((a, b) => b.failure_rate - a.failure_rate);
    // console.log(failure);
    
    return failure.map(a => a.id);
}