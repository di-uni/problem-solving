n = int(input())
# mean_over_stud_list = []

for i in range(n):
    mean_over_stud = 0
    stud = list(map(int, input().split()))
    mean = sum(stud[1:])/stud[0]
    for score in stud[1:]:
        if score > mean:
            mean_over_stud += 1
    # mean_over_stud_list.append(mean_over_stud / stud[0] * 100)
    print("{:.3f}%".format(mean_over_stud / stud[0] * 100))

# for m in mean_over_stud_list:
#     print("{:.3f}%".format(m))