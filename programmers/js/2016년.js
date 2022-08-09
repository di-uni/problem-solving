// First Trial

function solution(a, b) {
    const days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    const days = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"];
    let passed_days = b;

    for (let i = 0; i < a; i++) {
        passed_days += days_in_month[i];
    }
    return days[passed_days % 7];
}


//  =============================================
//  Other's Solution
//  reduce 이용

function solution(a, b){
    var dayList = ['FRI','SAT','SUN','MON','TUE','WED','THU'];
    var monthArr = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    var daySum = b - 1;

    if (a > 1) {
        daySum += monthArr.slice(0, a - 1).reduce((a, b) => a + b);
    }
    
    return dayList[daySum % 7];
}