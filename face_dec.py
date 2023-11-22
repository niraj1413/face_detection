#pip install opencv-python

import cv2   #camera enable krega 


face_cap =cv2.CascadeClassifier("C:/Users/user/Desktop/python/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml")





video_cap = cv2.VideoCapture(0)   # access the computer camera and 0 for prime camera use 1 for exteranal camera 

while True: 
    ret, video_data = video_cap.read()    # video enavble hone ke baad read krega 
    col =cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY) #caputed video color changing 
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags= cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,h,w) in faces:
        cv2.rectangle(video_data,(x,y) , (x+w,y+h),(0,255,0),2)
    cv2.imshow("video_live",video_data)  # display krega vide live naam se 
    if cv2.waitKey(10) == ord("a"):      # to stop video press a or any keyword u fixed 
        break

video_cap.release()




