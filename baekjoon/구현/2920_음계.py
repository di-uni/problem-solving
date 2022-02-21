# First Trial
# Test Passed

# scale = list(map(int, input().split()))
# ans = "mixed"

# # ascending
# if scale[0] == 1:
#     i = 1
#     ans = "ascending"
#     for s in scale:
#         if s != i:
#             ans = "mixed"
#             break
#         i += 1
# # descending
# elif scale[0] == 8:
#     i = 8
#     ans = "descending"
#     for s in scale:
#         if s != i:
#             ans = "mixed"
#             break
#         i -= 1
# 
# print(ans)

# ======================================================
# Second Trial according to other's solution

scale = list(map(int, input().split()))
if scale == sorted(scale):
    print("ascending")
    exit(0)
elif scale == sorted(scale, reverse=True):
    print("descending")
    exit(0)
else:
    print("mixed")

