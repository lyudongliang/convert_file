import os
import numpy as np


header_template = [
    'ply',
    'format ascii 1.0',
    'property float x',
    'property float y',
    'property float z',
    'property uchar red',
    'property uchar green',
    'property uchar blue',
    'end_header'
]


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

    print('len of pts', len(pts))
    return pts


def translate_pointsXYZRGB(pt_list: list):
    pt_array = np.array(pt_list)
    x_center = (np.min(pt_array, axis=0) + np.max(pt_array, axis=0)) / 2.
    y_center = (np.min(pt_array, axis=1) + np.max(pt_array, axis=1)) / 2.
    z_center = (np.min(pt_array, axis=2) + np.max(pt_array, axis=2)) / 2.
    
    new_pt_list = [[pt[0] - x_center, pt[1] - y_center, pt[2] - z_center, pt[3], pt[4], pt[5]] for pt in pt_list]
    return new_pt_list



def dump_ply_file(pt_list: list, file_path: str, translate=False):
    if translate:
        new_pt_list = translate_pointsXYZRGB(pt_list)
    else:
        new_pt_list = pt_list
    
    with open(file_path, 'w') as f:
        vertex_line = 'element vertex ' + str(len(pt_list))
        header_template.insert(2, vertex_line)
        print(header_template)
        # write header
        for line in header_template:
            f.write(line + '\n')
        
        for pt in new_pt_list:
            pt_str = list(map(str, pt))
            line = ' '.join(pt_str) + '\n'
            f.write(line)
        
        f.close()


if __name__ == '__main__':
    # txt_file = os.path.join(os.path.abspath(''), 'data/office_1.txt')
    # obj_file = os.path.join(os.path.abspath(''), 'data/office_1.ply')
    
    txt_file = os.path.join(os.path.abspath(''), 'data/conferenceRoom_1.txt')
    obj_file = os.path.join(os.path.abspath(''), 'data/conferenceRoom_1.ply')

    pts = get_pointsXYZRGB_from_txt(txt_file)
    dump_ply_file(pts, obj_file, True)

