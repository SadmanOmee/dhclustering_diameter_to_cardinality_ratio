import numpy as np
from sklearn.metrics.cluster import adjusted_rand_score

u = []
v = []
for i in range(0, 70):
    u.append(0)
for i in range(0, 30):
    u.append(1)
for i in range(0, 10):
    u.append(2)
for i in range(0, 67):
    v.append(0)
for i in range(0, 3):
    v.append(2)
for i in range(0, 30):
    v.append(1)
for i in range(0, 10):
    v.append(2)
    
    
    
    
    
    

#ari = adjusted_rand_score([0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1, 1, 1, 1, 0])
ari = adjusted_rand_score(u, v)  
print(ari)

ri = (2694 + 3070) / 5995
print(ri)


#sum of ratio
pmethod = (20 / 5) * 2
kmethod = (15.62 / 6) + (13 / 4)
print(pmethod)
print(kmethod)




















