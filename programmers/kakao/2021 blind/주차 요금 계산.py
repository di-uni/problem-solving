from collections import defaultdict
import math

def solution(fees, records):
    default_time = fees[0]
    default_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    parking = {}
    sumParking = defaultdict(int)
    carfee = {}
    
    def getFee(timeDiff):
        res = default_fee
        if timeDiff > default_time:
            res += math.ceil((timeDiff-default_time)/unit_time) * unit_fee
        return res
    
    for r in records:
        time, car, inOrOut = r.split(" ")
        h, m = time.split(":")
        time = int(h) * 60 + int(m)
        if inOrOut == "IN":
            parking[car] = time
        if inOrOut == "OUT":
            sumParking[car] += time - parking.pop(car)
    
    for car in parking.keys():
        sumParking[car] += 23*60 + 59 - parking[car]
    # print(sumParking)
    
    for car in sumParking.keys():
        carfee[car] = getFee(sumParking[car])
    # print(carfee)
    
    # print(sorted(carfee.items()))
    # return [i[1] for i in sorted(carfee.items())]
    return list(map(lambda x : x[1], sorted(carfee.items())))


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))