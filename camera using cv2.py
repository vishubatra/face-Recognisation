import cv2
dataset = cv2.CascadeClassifier('hr.xml')
capture = cv2.VideoCapture(0)
while True:
    ret,img=capture.read()
    if ret:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        face=dataset.detectMultiScale(gray)

        for x,y,w,h in face: #for dimensions
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),8)
            
        cv2.imshow('result',img)
        if cv2.waitKey(1)==27:break

    else:print('camera not working')

capture.release()
cv2.destroyAllWindows()

    
