import ProcessImage
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2
import os


def Load_ID(path):
    """
    Takes in path of the parent folder and return a list of files in that directory.
    argument :
        path = path of parent directory.
    """
    id_list = []
    for dirname, _, filenames in os.walk(path):
        for file in filenames:
            im = os.path.join(dirname, file)
            if im is not None:
                id_list.append(im)
    return id_list


def Read_Image(path_list):
    """
    Takes in a list of image path(id) and loads the images in a list as grayscale image.
    argument:
        path_list = list of path(of)
    """
    list_im = []
    for i in path_list:
        im = cv2.imread(i)
        img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        if img is not None:
            list_im.append(img)
    return list_im

def Resize_Image(image, dim=(500, 90)):
    """
    Takes in single image and resize the image according to the dimension.
    And returns the resized image.

    argument:
        image = the image.
        dim = dimension, default = (500, 90).
    """
    img = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return img



def Detect_box(image, Crop = False):
    """
    This function takes a list of image and finds the outer most boundaries and crops the image along the bounding box.
    Crop by default is False. If image is to be cropped make that statement True.
    """
    img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    img_y = np.zeros(img_yuv.shape[0:2], np.uint8)
    img_y[:, :] = img_yuv[:, :, 0]

    img_blur = cv2.GaussianBlur(img_y, (5,5), 0)
    edges = cv2.Canny(img_blur, 100, 500, apertureSize=3)

    contours, hier = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    img_area = image.shape[1] * image.shape[0]

    new_contours = []
    for c in contours:
        if cv2.contourArea(c) < img_area:
            new_contours.append(c)

    best_box = [-1, -1, -1, -1]
    for c in new_contours:
        x, y, w, h = cv2.boundingRect(c)
        if best_box[0] < 0:
            best_box = [x, y, x+w, y+h]
        else:
            if x < best_box[0]:
                best_box[0] = x
            if y < best_box[1]:
                best_box[1] = y
            if x+w > best_box[2]:
                best_box[2] = x+w
            if y+h > best_box[3]:
                best_box[3] = y+h

    point_a = (best_box[0], best_box[1])
    point_b = (best_box[2], best_box[3])

    if Crop:
        im = image[best_box[1]: best_box[3], best_box[0]: best_box[2]]

    return im





