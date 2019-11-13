import cv2
import numpy as np

class HaarFaceDetector:
    __image = None
    __grayimg = None
    face_cascade =  cv2.CascadeClassifier('HaarCascades/haarcascade_frontalface_default.xml')
    
    def detect(self,image):
        self.__image = image
        self.__grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(self.__grayimage, 4, 6)
        print ('We found ' + str(len(faces)) + ' faces in this image')
        img_with_detections = np.copy(self.__image)
        for (x,y,w,h) in faces:
            cv2.rectangle(img_with_detections,(x,y),(x+w,y+h),(255,0,0),5)
            img = img_with_detections[y:y+h, x:x+w]

        cv2.imshow('faces',img_with_detections)

if __name__ == '__main__':
    x = HaarFaceDetector()
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        x.detect(frame)
        if cv2.waitKey(1) == 13: break
    
    cap.release()
    cv2.destroyAllWindows()