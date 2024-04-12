import numpy as np

leng = 50
data = np.random.randint(0, leng, 500)  # 0부터 50까지 500개
cnt = [0] * 5 #0으로 초기화


for i in data:
    cnt[i] += 1
print(cnt)

max = [[0, 0]] * 3

print(max)

for i in range(cnt):
    c = 0
