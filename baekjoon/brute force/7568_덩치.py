n = int(input())
people = []
rank = ""

for i in range(n):
    people.append(list(map(int, input().split())))

temp_rank = 1
for a in people:
    for b in people:
        if a[0] < b[0] and a[1] < b[1]:
            temp_rank += 1
    rank += str(temp_rank) + " "
    temp_rank = 1

print(rank.rstrip())

