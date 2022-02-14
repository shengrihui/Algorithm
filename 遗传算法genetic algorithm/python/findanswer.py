#f(x1,x2) = 21.5+x1*sin(4pi*x1)+x2*sin(20pi*x2)）

from collections import defaultdict
import numpy as np
f=lambda x1,x2:21.5+x1*np.sin(4*np.pi *x1)+x2*np.sin(20*np.pi*x2)
d=defaultdict(list)
from tqdm import tqdm
s=0.0002
for x1 in tqdm(np.arange(-3.0,12.1,s)):
    for x2 in np.arange(4.1,5.8,s):
        d[f(x1,x2)].append((x1,x2))

print(max(d))
print(d[max(d)])



