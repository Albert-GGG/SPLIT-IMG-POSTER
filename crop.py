import cv2 as cv
import os
import sys
from fpdf import FPDF


img_name = 'lands.jpg'
path_img = './IMGS' + '/' + img_name

img = cv.imread(path_img)

if img is None:
    sys.exit('No se pudo leer la imagen')

# cv.imshow("Imagen", img)
# k = cv.waitKey(0)

div_alto = int(input('Divisiones alto: '))
div_largo = int(input('Divisiones largo: '))

height_region, width_region = int(img.shape[0] / div_alto), int(img.shape[1] / div_largo)

path = './cropped_' + img_name.split('.')[0]

if not os.path.exists(path):
    os.mkdir(path)

imgs = list()

for h in range(div_alto):
    for w in range(div_largo):
        new_region = img[h * height_region:height_region * (h + 1), w * width_region:width_region * (w + 1)]
        imgs.append(new_region)


for i in range(len(imgs)):
    cv.imwrite(path + '/' + f'parte_{i + 1}.png', imgs[i])

orientation = None
pdf_width = None
mm = 3.7795275591

if width_region / height_region > 1:
    orientation = 'L'
    pdf_width = 270
else:
    orientation = 'P'
    pdf_width = 205

pdf = FPDF(orientation=orientation, unit='mm', format='Letter')

for el in os.listdir(path):
    if el.split('.')[1] != 'png':
        continue
    pdf.add_page()
    pdf.image(path + '/' + el, x = 5, y = 5, w = pdf_width)

pdf.output(path + '/' + 'cropped.pdf')
    



    













    


