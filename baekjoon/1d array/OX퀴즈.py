n = int(input())

for i in range(n):
    score = 0
    temp_score = 0
    ans = input()
    for ox in ans:
        if ox == "O":
            temp_score += 1
            score += temp_score
        elif ox == "X":
            temp_score = 0
    print(score)