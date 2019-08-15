# -*- coding: utf-8 -*-
# @Time    : 2019-08-15 21:59
# @Author  : lixn
import cv2
from cv2.cv2 import imwrite

binary_image = cv2.imread('./mask_photo.png')

gray_image = cv2.cvtColor(binary_image, cv2.COLOR_BGR2GRAY)

diffs = []

width = len(gray_image[0])

for i in range(len(gray_image) - 1):
    total = 0
    for j in range(width):
        total += abs(int(gray_image[i][j]) - int(gray_image[i+1][j]))

    diffs.append(total/width)


tmp_a, tmp_b = 0, 0
tmp_a_index, tmp_b_index = 0, 0

imwrite("./Gray_Image.jpg", gray_image)

for index, diff in enumerate(diffs):
    if diff > tmp_a:
        tmp_a, tmp_b = diff, tmp_a
        tmp_a_index, tmp_b_index = index, tmp_a_index

    elif diff > tmp_b:
        tmp_b = diff
        tmp_b_index = index

print(tmp_a, tmp_b)
print(tmp_a_index, tmp_b_index)

# print(type(gray_image[tmp_a]))


top_line_y = min(tmp_a_index, tmp_a_index)
bottom_line_y = max(tmp_b_index, tmp_b_index) + 1

for y in [top_line_y, top_line_y - 1, top_line_y -2, bottom_line_y, bottom_line_y + 1, bottom_line_y+2]:
    for x in range(width):
        gray_image[y][x] = 0

imwrite("./Gray_Image_BlackLine.jpg", gray_image)


# 用ffmpeg crop video (top_line_y < y < bottom_line_y)
