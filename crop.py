import cv2 as cv
import os
import sys
from fpdf import FPDF

##########################| CONFIGURATION |#############################

img_name = 'books.png'
path_img = './IMGS' + '/' + img_name

img = cv.imread(path_img)

if img is None:
    sys.exit('Image could not be read')

rows = int(input('Number of rows: '))
columns = int(input('Number of columns: '))

height_region, width_region = int(img.shape[0] / rows), int(img.shape[1] / columns)

# Name of new folder with split image
path = './cropped_' + img_name.split('.')[0]

if not os.path.exists(path):
    os.mkdir(path)

imgs = list()

for h in range(rows):
    for w in range(columns):
        new_region = img[h * height_region:height_region * (h + 1), w * width_region:width_region * (w + 1)]
        imgs.append(new_region)

# Save each region or block into a new folder
for i in range(len(imgs)):
    cv.imwrite(path + '/' + f'parte_{i + 1}.png', imgs[i])

orientation = None
pdf_width = None
mm = 3.7795275591

# Add image with maximum size to a letter size page inside a PDF
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
    



    













    


