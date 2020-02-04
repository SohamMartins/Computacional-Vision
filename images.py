import cv2

# reconhecendo a imagem
img = cv2.imread('Orange.png')

# mostrando a imagem
cv2.imshow('image', img)

# salvando essa imagem
cv2.imwrite('save.png', img)

# recortando a imagem => img[y:y+h, x:x+w]
recorte = img[75:250, 100:300]

cv2.imshow('recorte', recorte)

# aumentando ou diminuindo o tamanho
tamanho = cv2.resize(img, (600, 600)) # as informações de largura e altura em tupla!

cv2.imshow('aumentando', tamanho)

# wait key
cv2.waitKey(0)
