function solution(s) {
    var answer = [];
    let setList = s.slice(2, s.length-2).split("},{");
    let array = [];
    for (let arr of setList) {
        array.push(arr.split(","));
    }
    array.sort((a, b) => a.length - b.length);
    for (let arr of array) {
        let elem = arr[0];
        if (arr.length !== 1) {
            for (let a of arr) {
                if (!answer.includes(Number(a))) 
                    elem = a;
            }
        }
        answer.push(Number(elem));
    }
    return answer;
}



// ======================================
// Other's solution 
// map, reduce 등 함수형 프로그래밍 사용

const tupleFrom = (str) =>
  str.slice(2, -2).split('},{')
    .map((it) => toNumbers(it))
    .sort(accendingByLength)
    .reduce((acc, cur) =>
      [...acc, ...cur.filter((it) => !acc.includes(it))], []);

const toNumbers = (str) => str.split(',').map(it => Number(it));

const accendingByLength = (arr1, arr2) => arr1.length - arr2.length;

const solution = (s) => tupleFrom(s);