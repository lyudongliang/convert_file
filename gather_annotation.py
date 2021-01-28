import os
import numpy as np
from parse_S3DIS_file import get_pointsXYZRGB_from_txt
from dump_ply import dump_ply_file


TYPE_COLOR_DICT = {'ceiling': (0, 255, 255), 'floor': (130, 130, 130), 'wall': (255, 248, 220), 'beam': (210, 180, 140), 'column': (255, 255, 0), 'window': (0, 191, 255), 'door': (0, 255,0), 
                                                'table': (255, 165, 0), 'chair': (255, 114, 86), 'sofa': (155,48,255), 'bookcase': (0, 0, 139), 'board': (255, 105, 180), 'clutter': (255, 255, 255)}


def gather_component(directory_path: str):
    print('directory_path', directory_path)

    _all_pts = list()
    
    type_list = []
    for name in os.listdir(directory_path):
        if name.endswith('.txt'):
            type_list.append(name.split('_')[0])
    type_list = list(set(type_list))
    print('type_list', type_list)

    for name in os.listdir(directory_path):
        if name.endswith('.txt'):
            type_name = name.split('_')[0]
            type_index = type_list.index(type_name)
            type_color = TYPE_COLOR_DICT[type_name]
            file_path = os.path.join(directory_path, name)
            component_pts = get_pointsXYZRGB_from_txt(file_path)
            _all_pts += [[pt[0], pt[1], pt[2], type_color[0], type_color[1], type_color[2]] for pt in component_pts]
            
    print('len of all pts', len(_all_pts))
    return _all_pts
    

if __name__ == '__main__':
    anonation_directory = os.path.join(os.path.abspath(''), 'data/area_5_conferenceRoom_2/Annotations')
    ply_file = os.path.join(os.path.abspath(''), 'data/area_5_conferenceRoom_2/annotations.ply')

    scene_pts = gather_component(anonation_directory)
    dump_ply_file(scene_pts, ply_file, False)