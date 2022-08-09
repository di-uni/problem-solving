// First Trial

function solution(numbers) {
    let answer = 0;
    let exists = new Array(10).fill(false);
    
    for (let num of numbers) {
        exists[num] = true;
    }
    for (let i = 0; i < 10; i++) {
        if (!exists[i]) {
            answer += i;
        }
    }
    return answer;
}


//  =============================================
//  Other's Solution
//  총합을 이용

function solution(numbers) {
    return 45 - numbers.reduce((acc, cur) => acc + cur, 0);
}


// includes 이용

function solution(numbers) {
    let answer = 0;
    for(let i = 0; i < 10; i++) {
        if(!numbers.includes(i)) answer += i;
    }

    return answer;
}