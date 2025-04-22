from deepface import DeepFace

import cv2
import os

import random 


hash = random.getrandbits(128)


cap = cv2.VideoCapture(0)

save_folder = "captured_pics"
faces_directory="attendance_library"
os.makedirs(save_folder, exist_ok=True)




filepath=""
while True:
    ret, frame = cap.read()
    if not ret:
        print("couldn't get frame")
        break
    cv2.putText(frame,"This is an attendance app. Press space to take pic, esc to exit",(50,200),cv2.FONT_HERSHEY_PLAIN,1, (0,0,0),2,cv2.LINE_AA)

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)

    if key % 256 == 27: 
        break
    elif key % 256 == 32: 
        filename = str(hash) + ".png"
        filepath = os.path.join(save_folder, filename)
        cv2.imwrite(filepath, frame)
        print(f"Saved image to {filepath}")
        cap.release()
        cv2.destroyAllWindows()
        break


print(os.path.exists(filepath),'filepath check')
results = DeepFace.find(img_path=f'{filepath}',db_path=faces_directory,enforce_detection=False, model_name="Facenet",detector_backend="retinaface")
print('results',results)
if len(results[0]) > 0:
    face_img = cv2.imread(filepath)
    print("Attendance marked.")
    cv2.putText(face_img,"Attendance marked for you",(100,100),cv2.FONT_HERSHEY_PLAIN,1, (0,0,0),2,cv2.LINE_AA)
    cv2.imshow('face',face_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("You are not in the class.")
    face_img = cv2.imread(filepath)
    cv2.putText(face_img,"Attendance not marked, you are not in this class",(100,100),cv2.FONT_HERSHEY_PLAIN,1, (0,255,0),2,cv2.LINE_AA)
    cv2.imshow('face',face_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

