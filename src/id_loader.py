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


English_path = "./../Signs/Processed-Original/English/"

Eng_id = find_id(path=English_path)

def labeller(id_list):
    lst, lab = [], []
    for im in id_list:
        img = im
        lb = 1
        if img is not None:
            lst.append(img)
            lab.append(lb)
    return lst, lab


id_s, lab = labeller(Eng_id)


data = {
        'ids': id_s,
        'labell': lab
        }

df = pd.DataFrame(data)

print(df.shape)

print(df.head())
