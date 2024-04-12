import numpy as np

m = np.array([11, 22, 30, 40, 50, 7, 9, 72, 34, 26], np.float32)

s = sum(m)
a = s / len(m)

print('합 = {:.2f}'.format(s))
print('평균 = {:.2f}'.format(a))
