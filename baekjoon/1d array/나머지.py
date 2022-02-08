res = set([])

for i in range(10):
    res.add(int(input()) % 42)
    
print(len(res))