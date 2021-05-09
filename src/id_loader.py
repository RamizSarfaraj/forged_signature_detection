import ProcessImage
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import cv2
import os


def find_id(path):
    """
    Traverse throught the given folder and subfolders, fine the full path of the image.
    """
    id_lst = []
    for root, dirs, filename in os.walk(path):
        for _d in dirs:
            path = os.path.join(root, _d)
            for file in os.listdir(path):
                file_id = os.path.join(path, file)
                if os.path.isdir(file_id):
                    for d_ in os.listdir(file_id):
                        new_path = os.path.join(file_id, d_)
                        id_lst.append(new_path)
                else:
                    id_lst.append(file_id)
    return id_lst


English_path = "./../Signs/Processed-Original/"

# Eng_id = find_id(path=English_path)

def interative_path(path):
    lst = []
    for new in os.listdir(path):
        file_d = os.path.join(path, new)
        if os.path.isdir(file_d):
            interative_path(file_d)
        else: 
            lst.append(file_d)
    return lst 

en_id = interative_path(English_path)

print(len(en_id))


print(en_id)

