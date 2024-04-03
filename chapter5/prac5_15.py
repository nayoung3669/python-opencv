import numpy as np

pts1 = np.array([(100,100), (400,100), (400,250) , (100,250)], np.float32)
theta = 30 * np.pi/180

m = np.array([[np.cos(theta), -np.sin(theta), 0],
              [np.sin(theta), np.cos(theta),0], [0,0,1],np.float32])

delta = (pts1[2] - pts1[0]) //2
center = pts1[0] + delta

t1 = np.eye(3, dtype=np.float32)
t2 = np.eye(3, dtype=np.float32)

t1[:2,2] = center[:2]


