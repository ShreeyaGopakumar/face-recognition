import cv2

img = cv2.imread("family1.png")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
faces = face_classifier.detectMultiScale(
    gray_image, scaleFactor=1.1, minNeighbors=12, minSize=(40, 40)
)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 250, 0), 4)

w = int(img.shape[1] * 50 / 100)
h = int(img.shape[0] * 50 / 100)

img = cv2.resize(img, (w,h), interpolation = cv2.INTER_AREA)
 
cv2.imshow('Detected Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
