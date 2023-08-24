import cv2 as cv
import time

camera_device = 1

# -- 2. Read the video stream
cap = cv.VideoCapture(camera_device)
time.sleep(15)
if not cap.isOpened():
    print('--(!) Error opening video capture')
    exit(0)

cv.namedWindow("Video", cv.WINDOW_AUTOSIZE)

while True:
    ret, frame = cap.read()
    if not ret:  # Check if the frame was captured successfully
        print('--(!) No captured frame -- Break!')
        break

    cv.imshow("Video", frame)
    key = cv.waitKey(10)
    if key == 27:  # Press ESC to exit, 27 is the ASCII code for ESC
        break
    if key == ord("S") or key == ord("s"):
        ctime = time.localtime()
        file_name = 'image_%4d_%02d_%02d_%02d_%02d_%02d.jpg' % (
            ctime.tm_year, ctime.tm_mon, ctime.tm_mday, ctime.tm_hour, ctime.tm_min, ctime.tm_sec
        )
        cv.imwrite(file_name, frame)

cap.release()  # Release the video capture object
cv.destroyAllWindows()  # Close all OpenCV windows
