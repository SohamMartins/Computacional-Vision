import cv2

# capturando um vídeo
cap = cv2.VideoCapture(0)

# criando loop infinito para percorrer todos os frames
while(True):
	# recuperar frame
	ret, frame = cap.read()

	# se tem retorno de frame
	if ret:
		cv2.imshow('frame', frame)

	# recupera o botão apertado	
	key = cv2.waitKey(1)	
	
	if key == ord('q'):
		break		

# libera o cachê de cap
cap.release()

# destrói todas as janelas abertas
cv2.destroyAllWindows()		
