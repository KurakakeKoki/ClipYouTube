import cv2
from tqdm import tqdm
import numpy as np

def mean_squared_error(frame1, frame2):
    return np.mean(np.square(frame1 - frame2))

videoCapture = cv2.VideoCapture('movie.webm')

frames = []
while (videoCapture.isOpened()):
    success, frame = videoCapture.read()
    if not success:
        break
    frames.append(frame)

max_diff = 0
diffs = []
for i, (frame1, frame2) in enumerate(tqdm(zip(frames, frames[1:]))):
    mse = mean_squared_error(frame1, frame2)
    diffs.append(mse)
    max_diff = max(max_diff, mse)

idx = 0
cv2.imwrite("./output/img{}.png".format(idx), frames[0])
idx += 1
for i, diff in enumerate(diffs):
    if diff < max_diff / 2:
        continue
    cv2.imwrite("./output/img{}.png".format(idx), frames[i+1])
    idx += 1
