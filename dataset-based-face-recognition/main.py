import face_recognition
import cv2
import numpy as np
from datetime import datetime

capture = cv2.VideoCapture(0)


jobs_image = face_recognition.load_image_file("face-recognition-attendacesystem/photos/SteveJobs.jpg")
jobs_encoding = face_recognition.face_encodings(jobs_image)[0]

gates_image = face_recognition.load_image_file("face-recognition-attendacesystem/photos/BillGates.jpg")
gates_encoding = face_recognition.face_encodings(gates_image)[0]

known_encodings = [jobs_encoding, gates_encoding]
known_names = ["Steve Jobs", "Bill Gates"]

while True:
    output, frame = capture.read()
    if not output:
        break
    
    resized_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_resized_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_resized_frame)
    
    if len(face_locations) > 0:
        face_encodings = face_recognition.face_encodings (rgb_resized_frame, face_locations)
        
        
        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings,face_encoding, tolerance=0.6)
            name="Unknown"
            face_distance = face_recognition.face_distance(known_encodings,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_names[best_match_index]
            
            
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left*4, top*4), (right*4, bottom*4), (0, 0, 255), 2)
            cv2.putText(frame, name, (left*4, bottom*4 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
               
    cv2.imshow("face", frame)
    
    if (cv2.waitKey(1) & 0xFF) == 27:
        break
    if cv2.getWindowProperty("face", cv2.WND_PROP_VISIBLE) < 1:
        break

capture.release()
cv2.destroyAllWindows()
