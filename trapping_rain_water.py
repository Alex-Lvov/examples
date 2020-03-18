"""
https://leetcode.com/problems/trapping-rain-water/
"""

from random import randint

in_data = [0,1,0,2,1,0,1,3,2,1,2,1] # 6
in_data = [0,1,0,2,1,0,1,3,0,0,0,0] # 5
in_data = [randint(0,3) for i in range(len(in_data))]
out_data = 0

vis = []
m = max(in_data)
for line in range(m):
    for v_cell in in_data:
        print(" " if m - line > v_cell else "X", end="")
    print()

print(f"Input: {in_data}")

i = 0
while i < len(in_data):
    found_border = False
    if in_data[i]:
        cell = 0
        for j in range(i+1, len(in_data)):
            if in_data[j] < in_data[i]:
                cell += in_data[i]-in_data[j]
            else:
                found_border = True
                break
    if found_border:
        i = j
        out_data += cell
    else:
        i += 1
print(f"Output: {out_data}")
