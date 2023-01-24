import cv2 as cv

capture = cv.VideoCapture(1)

pretrained_model = cv.CascadeClassifier("face_detector.xml")

while 1:
    ret, img = capture.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = pretrained_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

    if len(faces) == 0:
        print("CANNOT SEE FACE")

    for (x,y,w,h) in faces:
        re = cv.rectangle(img,(x,y),(x+w,y+h),(200,200,0),2)

        if 're' in locals():
            print('SEE FACE')

        else:
            print('CANNOT SEE FACE')
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv.imshow('image', img)

    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()