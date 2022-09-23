# First Trial
# Test Failed

# def convertToSec(h, m, s):
#     return h*60*60 + m*60 + s

# def convertToHMS(s):
#     h = s // 3600
#     m = (s % 3600) // 60
#     s = (s % 3600) % 60
#     if h < 10: h = f'0{h}'
#     if m < 10: m = f'0{m}'
#     if s < 10: s = f'0{s}'
#     return f'{h}:{m}:{s}'

# def solution(play_time, adv_time, logs):
#     max_adv_view = 0
#     answer = []
    
#     if play_time == adv_time:
#         return "00:00:00"
    
#     h, m, s = list(map(int, play_time.split(":")))
#     time = [0] * (convertToSec(h, m, s) + 1)
    
#     for log in logs:
#         start, end = log.split("-")
#         h1, m1, s1 = list(map(int, start.split(":")))
#         h2, m2, s2 = list(map(int, end.split(":")))
#         start_sec = convertToSec(h1, m1, s1)
#         end_sec = convertToSec(h2, m2, s2)
#         print(start, end)
#         for i in range(start_sec, end_sec + 1):
#             time[i] += 1
    
#     h, m, s = list(map(int, adv_time.split(":")))
#     adv_sec = convertToSec(h, m, s)
#     for i in range(len(time) - adv_sec):
#         # print(i)
#         adv_view = 0
#         for j in range(i, i + adv_sec):
#             adv_view += time[j]
#         if adv_view >= max_adv_view:
#             if adv_view > max_adv_view:
#                 answer = []
#             max_adv_view = adv_view
#             answer.append(i-1)
        
#     # answer = ''
#     return convertToHMS(answer[0])


# ==========================================
# Other's Solution
# using dp

def str_to_sec(time):
    h, m, s = time.split(":")
    return int(h)*60*60 + int(m)*60 + int(s)

def sec_to_str(time):
    h = str(time // 3600).zfill(2)
    m = str(time % 3600 // 60).zfill(2)
    s = str(time % 3600 % 60).zfill(2)
    return f'{h}:{m}:{s}'

def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"

    play = str_to_sec(play_time)
    adv = str_to_sec(adv_time)

    time = [0] * (play + 1)
    
    for log in logs:
        start, end = log.split("-")
        start_sec = str_to_sec(start)
        end_sec = str_to_sec(end)
        time[start_sec] += 1
        time[end_sec] += -1

    for i in range(1, play):
        time[i] = time[i] + time[i-1]

    for i in range(1, play):
        time[i] = time[i] + time[i-1]

    max_val = -1
    answer = 0
    for i in range(adv - 1, play):
        temp = time[i] - time[i - adv]
        if temp > max_val:
            max_val = temp
            answer = i - adv + 1

    return sec_to_str(answer)

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
print(solution("00:00:35", "00:00:10", ["00:00:25-00:00:35", "00:00:12-00:00:15", "00:00:20-00:00:28"]))