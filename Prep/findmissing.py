import collections

a1 = [1,2,3,3,4,4,5,6]
a2 = [2,3,1,4,6,4]

d = collections.defaultdict(int)


for num in a2:
    d[num] = d[num] +1

for num in a1:
    if d[num]>0: d[num] = d[num]-1
    else: print(f'{num} is missing')
#we can also do this with xor