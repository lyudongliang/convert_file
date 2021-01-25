import os
import sys
import json


def get_points_from_txt(file_path: str):
    pts = list()
    with open(file_path, 'r') as f:
        for line in f.readlines():
            line.strip('\n')
            value_list = line.split(' ')
            value_list = [float(s) for s in value_list]
            pts.append(value_list[:3])

    print('len of pts', len(pts))
    return pts


def dump_obj_file(pt_list: list, file_path: str):
    with open(file_path, 'w') as f:
        # print(pt_list)
        for pt in pt_list:
            pt_str = map(str, pt)
            line = 'v' + ' ' + ' '.join(pt_str) + '\n'
            f.write(line)
        
        f.close()


if __name__ == '__main__':
    txt_file = os.path.join(os.path.abspath(''), 'data/office_1.txt')
    obj_file = os.path.join(os.path.abspath(''), 'data/office_1.obj')
    
    pts = get_points_from_txt(txt_file)
    dump_obj_file(pts, obj_file)