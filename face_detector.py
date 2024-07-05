import cv2

# print(cv2.__version__)
cap = cv2.VideoCapture(0) # 선생님과 관련된 비디오를 열어주세요.
# cap.set(5, 100) # 창크기 조절
# cap.set(6, 100)
# low = 50
# high = 150

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")




while True:
    _, frame =cap.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #frame에 들어온 색을 그레이컬러로 바꾸기. frame = image
    # canny_frame = cv2.Canny(gray_frame, low, high)
    # blur_frame = cv2.GaussianBlur(frame, (11,11), 10)
    # rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 얼굴 찾기
    # faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    print(faces)

    if faces:
        print("Found")


    cv2.imshow("Video", frame)
    cv2.imshow("Gray", gray_frame)
    # cv2.imshow("RGB", rgb_frame)
    # cv2.imshow("Canny", canny_frame)
    # cv2.imshow("Blur", blur_frame)

    if cv2.waitKey(10) & 0xff ==ord('q'):
        break

cap.release()
cv2.destroyAllwindows()



