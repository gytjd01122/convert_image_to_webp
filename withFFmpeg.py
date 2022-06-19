'''
    main.py
'''
from ast import arg
import os
import threading
from multiprocessing import Pool
from pathlib import Path

from PIL import Image
import os
from packages import my_gui as g
import ffmpeg

def f(args):
    args = list(args)
    for file in args :
        print(file)
        
        stream = ffmpeg.input(file)
        stream = ffmpeg.output(stream, 'dd.webp')
        ffmpeg.run(stream)

        #진행중 파일명, 현재 /전체, 백분율 출력
        print(file.name)
#    os.remove(args)


if __name__ == '__main__':

    directory_name = g.open_directory()
    open_files = (p.resolve() for p in Path(directory_name).glob("**/*") if p.suffix in {".png",
     ".jpg", ".jpeg", ".gif", ".bmp"})

    f(open_files)
