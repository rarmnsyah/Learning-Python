import cv2

# read images with opencv
# img = cv2.imread("C:/Users/LENOVO/Template Program/Python/Project/OpenCV/Resources/saya.jpg")
# cv2.imshow('Saya',img)
# cv2.waitKey(0)

# read videos with opencv
frameWidth = 640
frameHeighth = 480  

# an information, 
# videos1 we use to capture a video in local
# videos2 we use to capture a webcam video
# videos(1) = cv2.VideoCapture("C:/Users/LENOVO/Template Program/Python/Project/OpenCV/Resources/Tugas Hafalan Risky Armansyah - 09021282126055 (1).mp4")
# videos(2) = cv2.VideoCapture(0)
# videos = cv2.VideoCapture("C:/Users/LENOVO/Template Program/Python/Project/OpenCV/Resources/Tugas Hafalan Risky Armansyah - 09021282126055 (1).mp4")
videos = cv2.VideoCapture(0)
videos.set(3,frameWidth)
videos.set(4,frameHeighth)

while True:
    success, img = videos.read()
    # img = cv2.resize(img, (frameWidth, frameHeighth))
    cv2.imshow("My Videos", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
