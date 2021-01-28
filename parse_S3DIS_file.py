import os
import numpy as np


def get_pointsXYZRGB_from_txt(file_path: str):
    pts = list()
    with open(file_path, 'r') as f:
        for line in f.readlines():
            line.strip('\n')
            value_list = line.split(' ')
            value_list = list(map(float, value_list))
            coord_list = value_list[:3]
            rgb_list = list(map(int, value_list[3:]))
            pts.append(coord_list + rgb_list)

    return pts