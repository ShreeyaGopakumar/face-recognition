import cv2

capture = cv2.VideoCapture(0)

while True:
    output, frame = capture.read() 
    if not output:
        break  
    cv2.imshow("Capture Window", frame)  

    if (cv2.waitKey(1) == ord('s')):
        cv2.imwrite(filename='capture.jpg',img=frame)
        capture.release()
        new_image = cv2.imread('capture.jpg', cv2.IMREAD_GRAYSCALE)
        break
    elif (cv2.waitKey(1) & 0xFF) == 27:
        capture.release()
        break
    elif cv2.getWindowProperty("Capture Window", cv2.WND_PROP_VISIBLE) < 1:
        capture.release()
        break
cv2.destroyAllWindows()