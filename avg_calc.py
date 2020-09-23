avgk1 = 0.32733
k2 = 0.28734
r1 = 0.24898
r2 = 0.32570
avg = (r1 + r2) / 2
#print(avg)

total = 5000
totalMislabeled = 2 + 9 + 2 + (70 / 2) + 121
print('totalMislabeled: ', totalMislabeled)
per = ((total - totalMislabeled) / total) * 100
print(per)
#aggr, comp, unbal, flame, moon

                          #aggr  = 169 78.553% 151 80.838% 112 85.787%   788
                          #flame =  45 81.250%  31 87.083%  64 73.333%   240
                          #unbal =   0    100%  15 99.769% 266 95.908%   6500





dhMislabeled = 898
print('dhMislabeled: ', dhMislabeled)
perDh = ((total - dhMislabeled) / total) * 100
print(perDh)

print(total - (82 * total / 100))

ari = (226 - (406 * 306) / 630) / ((712 / 2) - (406 * 306) / 630)
print('ari: ', ari)