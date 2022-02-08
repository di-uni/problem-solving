// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');
function merge(arr, l, m, r){
    let left = [];
    let right = [];
    let i = 0, j = 0, k = l, swaps = 0;

    for(let i = l; i < m + 1; i++) {
        left.push(arr[i]);
    }
    
    for(let i = m + 1; i < r + 1; i++) {
        right.push(arr[i]);
    }

    while (i < left.length && j < right.length){
        // console.log("-------");
        // console.log(left[i], right[j]);
        if (left[i] <= right[j]) {
            arr[k++] = left[i++];
        }
        else {
            arr[k++] = right[j++];
            swaps += (m + 1) - (l + i);
            // console.log(m, l, i);
            // console.log((m + 1) - (l + i));
        }
    }
    while (i < left.length) {
        arr[k++] = left[i++];
    }
    while (j < right.length) {
        arr[k++] = right[j++];
    }
    return swaps;
}

// 합병 정렬
function merge_sort(mlist, left, right){
  let mid;
  let result = 0;

  if(left < right){
    mid = Math.floor((left+right)/2); // 중간 위치를 계산하여 리스트를 균등 분할 -분할(Divide)
    result += merge_sort(mlist, left, mid); // 앞쪽 부분 리스트 정렬 -정복(Conquer)
    result += merge_sort(mlist, mid+1, right); // 뒤쪽 부분 리스트 정렬 -정복(Conquer)
    result += merge(mlist, left, mid, right); // 정렬된 2개의 부분 배열을 합병하는 과정 -결합(Combine)
  }
  return result;
}

function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    // console.log(A);
    let n = A.length;

    let inversion =  merge_sort(A, 0, n-1);
    if (inversion > 1000000000) {
        return -1;
    }
    return inversion;

}
