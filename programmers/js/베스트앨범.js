function solution(genres, plays) {
    let answer = [];
    
    let genres_total_plays = {};
    // {
    //     "classic": {
    //         "total_plays": 1450,
    //         "song": [[3, 800], [0, 500], [2, 150]]
    //     }
    // }
    for (let i = 0; i < genres.length; i++) {
        if (!(genres[i] in genres_total_plays)) {
            genres_total_plays[genres[i]] = {};
            genres_total_plays[genres[i]]["total_plays"] = 0;
            genres_total_plays[genres[i]]["song"] = [];
        }
        genres_total_plays[genres[i]]["total_plays"] += plays[i];
        genres_total_plays[genres[i]]["song"].push([i, plays[i]]);
    }
    // console.log(genres_total_plays);
    
    // [
    //     {
    //         "genre": "classic",
    //         "total_plays": 1450,
    //         "song": [[3, 800], [0, 500], [2, 150]]
    //     }
    // ]
    
    let sortable = [];
    for (let genre in genres_total_plays) {
        genres_total_plays[genre]["genre"] = genre;
        sortable.push(genres_total_plays[genre]);
    }
    sortable.sort((a, b) => b.total_plays - a.total_plays);
    // console.log(sortable);
    
    for (let genre of sortable) {
        genre.song.sort((a, b) => b[1] - a[1]);
        let n = Math.min(genre.song.length, 2);
        for (let i = 0; i < n; i++) {
            answer.push(genre.song[i][0]);
        }
    }
    
    return answer;
}