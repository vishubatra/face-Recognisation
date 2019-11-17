import cv2
dataset = cv2.CascadeClassifier('hr.xml')
img=cv2.imread('images.jpg')
blnk=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #GRAYSCALE #ye black and white read krta hai bs
face=dataset.detectMultiScale(blnk,10.5)
for x,y,w,h in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),5)#ye rectangle box face pr laane ke liye
#print(img)
cv2.imshow('Result_Image.jpg',img) #show kregi bs photo
