import cv2 
import numpy as np 
import mediapipe as mp 
from keras.models import load_model 
import tkinter as tk
import streamlit
#import time
#from atm_sim import * 
import subprocess
import os


model  = load_model("model.h5")
label = np.load("labels.npy")



holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)




lst = []

_, frm = cap.read()

frm = cv2.flip(frm, 1)

res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))


if res.face_landmarks:
	for i in res.face_landmarks.landmark:
		lst.append(i.x - res.face_landmarks.landmark[1].x)
		lst.append(i.y - res.face_landmarks.landmark[1].y)

	if res.left_hand_landmarks:
		for i in res.left_hand_landmarks.landmark:
			lst.append(i.x - res.left_hand_landmarks.landmark[8].x)
			lst.append(i.y - res.left_hand_landmarks.landmark[8].y)
	else:
		for i in range(42):
			lst.append(0.0)

	if res.right_hand_landmarks:
		for i in res.right_hand_landmarks.landmark:
			lst.append(i.x - res.right_hand_landmarks.landmark[8].x)
			lst.append(i.y - res.right_hand_landmarks.landmark[8].y)
	else:
		for i in range(42):
			lst.append(0.0)

	lst = np.array(lst).reshape(1,-1)

	pred = label[np.argmax(model.predict(lst))]
	print(model.predict(lst))
	cv2.putText(frm, pred, (50,50),cv2.FONT_ITALIC, 1, (255,0,0),2)
	if pred == "happy":
		

		process = subprocess.Popen(["streamlit", "run", os.path.join('happy_strlit.py')])

	elif pred == "sad":
		process = subprocess.Popen(["streamlit", "run", os.path.join('sad_strlit.py')])

	elif pred == "excited":
		process = subprocess.Popen(["streamlit", "run", os.path.join('excited_strlit.py')])

	elif pred == "grumpy":
		process = subprocess.Popen(["streamlit", "run", os.path.join('grumpy_strlit.py')])






	
	

	#else:
		#pred1 = label["Invalid"]


		

	

	#print(pred)
	# if pred == "srinidhi" or pred == "gagan " or pred == "hitesh":
	# 	
	# 	exec(open('atm_sim.py').read())

	# else:
	# 	temp = "unauthorised"
	# 	cv2.putText(frm, temp, (50,50),cv2.FONT_ITALIC, 1, (255,0,0),2)

	
	

	
drawing.draw_landmarks(frm, res.face_landmarks, holistic.FACEMESH_CONTOURS)
drawing.draw_landmarks(frm, res.left_hand_landmarks, hands.HAND_CONNECTIONS)
drawing.draw_landmarks(frm, res.right_hand_landmarks, hands.HAND_CONNECTIONS)

cv2.imshow("window", frm)

if cv2.waitKey(1) == 27:
	cv2.destroyAllWindows()
	cap.release()
	




