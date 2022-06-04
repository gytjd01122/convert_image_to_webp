'''
    convert_image_to_webp.py
'''
import os
import threading
from PIL import Image


def convert_image_to_webp (start, stop, file_list):
    '''
        이미지 파일을 webp 파일로 변환하는 함수
    '''

    for i in range(start, stop):
        file = file_list[i]

        with Image.open(file) as img:
            img.save(file.with_suffix('.webp'),'WEBP')
            print(threading.current_thread().name, file.name)
        os.remove(file)
