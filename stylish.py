import cv2
import numpy as np

img_path = 'cat.jpg'
img = cv2.imread(img_path)
img = cv2.resize(img, (400, 400))

def callBack1(value):
    pass
def callBack2(value):
    pass

cv2.namedWindow("Style", cv2.WINDOW_NORMAL)
cv2.createTrackbar("sigma_s","Style", 0, 200, callBack1)
cv2.createTrackbar("sigma_r","Style", 0, 10, callBack2)



while True:
    sigma_s = cv2.getTrackbarPos("sigma_s", "Style")
    sigma_r = cv2.getTrackbarPos("sigma_r", "Style") / 10.0
    # print(sigma_r)
    
    img_style = cv2.stylization(img, sigma_s, sigma_r)

    cv2.imshow("Image",img)
    cv2.imshow("Style", img_style)

    if cv2.waitKey(10) & 0xff == ord('q'):
        break

    # high_t = cv2.getTrackbarPos("high_t", "Slider")
    # print(high_t)
    # img_canny = cv2.Canny(img_blur, 10, high_t)
    
    # cv2.imshow("Cat", img_canny)
    # cv2.imshow("Gray", img_gray)
    # cv2.imshow("Blur", img_blur)

    # if cv2.waitKey(10) & 0xff==ord('q'):
    #     break

cv2.destroyAllwindows()