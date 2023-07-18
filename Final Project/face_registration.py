import cv2
import face_recognition
import pickle
from datetime import datetime

#Create an Instance of the VideoCapture class
cap = cv2.VideoCapture(0)

#Set the image width and height
width, height = 320, 240 

#Set the format of the captured image
cap.set(sv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(sv2.CAP_PROP_FRAME_HEIGHT, height)

#Create a face detector using the Haar cascade classifier
face_cascade = cv2.CascadeClassifier('haar_cascade_files/haarcascade_frontalface_default.xml')


#Prompt the user to enter the name for registered face
name = input("Enter your name: ")

#Prompt the user to enter the room access (comma-separated)
accsess_input = input("Enter room access (comma-separated): ")
accsess_list = access_input.split(',')

#Initilize an empty list to store the face data
face_data = []

#Counter for the number of face captures
capture_count = 0 

while True:
	#Capture frame_by_frame
	ret, frame = cap.read()

	#Convert the frame to grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	#Detect faces in the frame
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30,30))

	#Draw rectangles around the detected faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

	#Encode the face region of interest (ROI) using face _recognition
	rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	face_encodings = face_recognition.face_encodings(rgb_frame,[(y, x+w, y+h, x)])

	#Store the face region of interest (ROI), face encoding, and room access as a dictionary with the name
	face_encoding in face_encodings:
		face_data.append({"name": name, "face": frame[y:y+h, x:x+w], "face_encoding":  "access": access_list}) 

	#Display the frame
	cv2.imshow('Register Face', frame)

	if cv2.waitKey(1) & 0xFF == ord('s'):
		capture_count += 1
		print(f "Capture {capture_count} complete!")
	if capture_count >= 5:
		break

cap.release()
cv2.destroyAllWindows()

now = datetime.now()
file.name = f"faces/{now.strftime('%Y-%m-%d-%H-%M-%s')}-{name}.pickle"
with open (file_name, 'wd') as f:
	pickle.dump(face_data, f)
print(f"Face data for '{name}' saved successfully!")
