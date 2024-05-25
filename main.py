import cv2
from mtcnn import MTCNN
detector = MTCNN()
def mtcnn_face_detect(frame):
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    faces = detector.detect_faces(frame)

    face = []
    if faces:
        confidence_scores = [face['confidence'] for face in faces]
        max_confidence_index = confidence_scores.index(max(confidence_scores))
        #x,y,w,h
        face = faces[max_confidence_index]['box']
    return face


    
image = cv2.imread(r"D:/ytb/WIN_20240404_07_18_34_Pro.jpg")
face = mtcnn_face_detect(image)
if face:
    
    x,y,w,h = face
    cv2.rectangle(image,(x,y),(x+w,y+h),color = (0,0,255))
    

cv2.imshow("image",image)
cv2.waitKey(0)