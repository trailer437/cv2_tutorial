import cv2
import numpy as np


# print(cv2.__version__)
cap = cv2.VideoCapture(0) # 선생님과 관련된 비디오를 열어주세요.
cap.set(5, 100) # 창크기 조절
cap.set(6, 100)
low = 50
high = 150

# 스타일 callBack
def callBack1(value):
    pass
def callBack2(value):
    pass

# Canny callBack
def callBack1(value):
    pass
def callBack2(value):
    pass

cv2.namedWindow("Style", cv2.WINDOW_NORMAL)
cv2.createTrackbar("sigma_s","Style", 0, 200, callBack1)
cv2.createTrackbar("sigma_r","Style", 0, 10, callBack2)

while True:
    _, frame =cap.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #frame에 들어온 색을 그레이컬러로 바꾸기. frame = image
    canny_frame = cv2.Canny(gray_frame, low, high)
    blur_frame = cv2.GaussianBlur(frame, (11,11), 10)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    sigma_s = cv2.getTrackbarPos("sigma_s", "Style")
    sigma_r = cv2.getTrackbarPos("sigma_r", "Style") / 10.0
    # print(sigma_r)
    
    style_frame = cv2.stylization(frame, sigma_s, sigma_r)    



    cv2.imshow("Video", frame)
    cv2.imshow("Gray", gray_frame)
    # cv2.imshow("RGB", rgb_frame)
    cv2.imshow("Canny", canny_frame)
    cv2.imshow("Blur", blur_frame)

    cv2.imshow("Style", style_frame)



    if cv2.waitKey(10) & 0xff ==ord('q'):
        break

cap.release()
cv2.destroyAllwindows()




