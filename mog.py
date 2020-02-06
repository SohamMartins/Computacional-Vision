import cv2

cap = cv2.VideoCapture('video.mp4')	

# criando o que irá subtrair
subtractor = cv2.createBackgroundSubtractorMOG2(history = 100, varThreshold = 50, detectShadows = True)

while (True):
	_, frame = cap.read()

	# criar máscara
	mask = subtractor.apply(frame)

	cv2.imshow('mask', mask)
	cv2.imshow('frame', frame)

	if cv2.waitKey(10) & 0xFF == ord('q'):
		break		

cap.release()

cv2.destroyAllWindows()
