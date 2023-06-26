import os
import sys
import cv2
import time
from tqdm import tqdm
import numpy as np
from yt_dlp import YoutubeDL

def mean_squared_error(frame1, frame2):
    return np.mean(np.square(frame1 - frame2))

url = sys.argv[1]
timestamp = time.time()//1
output_dir = "output{}".format(timestamp)
movie_path = "./{}/movie{}.webm".format(output_dir, timestamp)

os.makedirs(output_dir, exist_ok=True)

option = {
	"outtmpl": movie_path,
	"format": "bestvideo"
}
ydl = YoutubeDL(option)
result = ydl.download([url])

videoCapture = cv2.VideoCapture(movie_path)

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
cv2.imwrite("./{}/img{}.png".format(output_dir, idx), frames[0])
idx += 1
for i, diff in enumerate(diffs):
    if diff < max_diff / 2:
        continue
    cv2.imwrite("./{}/img{}.png".format(output_dir, idx), frames[i+1])
    idx += 1
