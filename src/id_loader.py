import ProcessImage
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import cv2
import os


def id_loader(path):
    id_list = []
    for dirname, _, filenames in os.walk(path):
        for file in filenames:
            im = os.path.join(dirname, file)
            if im is not None:
                id_list.append(im)

    return id_list


Original = "/home/ramiz/Signature_project/Signs/Processed-Original/"

id_list = id_loader(Original)

print(len(id_list))
