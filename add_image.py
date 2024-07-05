import cv2
import numpy as np

path1 = 'cat.jpg'
path2 = 'dog.jpg'

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
# print(img1.shape)
print(img2.shape)
# img1 = cv2.resize(img1, (486, 360))
img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))
print(img1.shape)
img3 = cv2.add(img1, img2)

# roi, 슬라이싱을 활용해서 이미지 자르기


mask = np.ones((img2.shape[0], img2.shape[1], 3), dtype='uint8') * 50
img1_b = cv2.add(img1, img2)
img2_d = cv2.subtract(img2, mask)
# print(mask)

roi = img1[100:300,200:500,:]
# print(roi)

# 자르고 색상바꾸기
roi[:, :, 1] = 255



cv2.imshow("Cat", img1)
cv2.imshow("Cat_b", img1_b)
cv2.imshow("Dog", img2)
cv2.imshow("Dog_d", img2_d)

cv2.imshow("ROI", roi)

# cv2.imshow("CatDog", img3)

cv2.waitKey()
cv2.destroyAllWindows()



