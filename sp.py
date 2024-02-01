import cv2
import numpy as np

def Split(in_image, rows, columns):

    height_region, width_region = int(in_image.shape[0] / rows), int(in_image.shape[1] / columns)
    regions = []

    for rs in range(rows):
        h_regions = list()
        for cs in range(columns):
            new_region = in_image[rs * height_region:height_region * (rs + 1), cs * width_region:width_region * (cs + 1)]
            h_regions.append(new_region)
        regions.append(h_regions)

    return regions

def mergeImg(regions):
    reg_height = regions[0][0].shape[0]
    
    hor_list = list()
    blacksH = np.zeros((reg_height, 10, 3), dtype=np.uint8)
    
    # Add black border to the right of images
    for row in range(len(regions)):
        for reg in range((len(regions[row]) - 1)):
            regions[row][reg] = np.concatenate((regions[row][reg], blacksH), axis=1)
    
    # Merge columns of each row
    for row in regions:
        hor_list.append(np.concatenate(([f for f in row]), axis=1))

    reg_width = hor_list[0].shape[1]
    blacksW = np.zeros((10, reg_width, 3), dtype=np.uint8)

    for merged_row in range(len(hor_list) - 1):
        hor_list[merged_row] = np.concatenate((hor_list[merged_row], blacksW), axis=0)

    merged_img = np.concatenate(([reg for reg in hor_list]), axis=0)

    return merged_img


readImg = cv2.imread("IMGS/forest.jpg")
regions = Split(readImg, 5, 5)

height_r, width_r = int(readImg.shape[0] / 2), int(readImg.shape[1] / 2)
blacks = np.zeros((height_r, 10, 3), dtype=np.uint8)

merged = mergeImg(regions)
cv2.imwrite('outMerged.png', merged)