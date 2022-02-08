# Time Limit Exceeded

n = input()
temp = n
count = 0

while True:
    if int(temp) < 10:
        temp = "0" + temp
    new_temp = str(int(temp[0]) + int(temp[1]))
    temp = temp[-1] + new_temp[-1]
    count += 1
    if n == temp:
        break
        
print(count)