import cv2 as cv
import os
import sys
from fpdf import FPDF

##########################| CONFIGURATION |#############################

img_name = 'mount.jpg'
path_img = './IMGS' + '/' + img_name

img = cv.imread(path_img)

if img is None:
    sys.exit('Image could not be read')

rows = int(input('Number of rows: '))
columns = int(input('Number of columns: '))

# Regions height and width in pixels
height_region, width_region = int(img.shape[0] / rows), int(img.shape[1] / columns)

# Name of new folder with split image
path = './cropped_' + img_name.split('.')[0]

if not os.path.exists(path):
    os.mkdir(path)

# Split the image in regions and add them to a list
imgs = list()
for h in range(rows):
    for w in range(columns):
        new_region = img[h * height_region:height_region * (h + 1), w * width_region:width_region * (w + 1)]
        imgs.append(new_region)

# Save each region or block into a new folder
for i in range(len(imgs)):
    cv.imwrite(path + '/' + f'parte_{i + 1}.png', imgs[i])


# Aspect ratios of the area for the image and the image itself
area_aspect_ratio = 270 / 205
region_aspect_ratio = width_region / height_region

# Default values of area occupied by the image region
area_width = 0
area_height = 0

# Add image with maximum size to a letter size page inside a PDF
if region_aspect_ratio >= 1:
    orientation = 'L'
    if region_aspect_ratio > area_aspect_ratio:
        area_width = 270
    else:
        area_height = 205
else:
    orientation = 'P'
    if region_aspect_ratio < area_aspect_ratio:
        area_height = 270
    else:
        area_width = 205
    
# Initialize PDF document of letter size
pdf = FPDF(orientation=orientation, unit='mm', format='Letter')

# Add a page for each image
for el in os.listdir(path):
    if el.split('.')[1] != 'png':
        continue
    pdf.add_page()
    pdf.image(path + '/' + el, x = 5, y = 5, w = area_width, h = area_height)

pdf.output(path + '/' + 'cropped.pdf')
    



    













    


