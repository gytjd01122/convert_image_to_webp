'''
    main.py
'''
import os
import threading
from multiprocessing import Pool
from pathlib import Path

from PIL import Image

from packages import my_gui as g


def f(args):
    with Image.open(args) as img:
        img.save(args.with_suffix('.webp'),'WEBP')
        print(os.getpid(), threading.current_thread().name, args.name)


if __name__ == '__main__':

    directory_name = g.open_directory()
    open_files = (p.resolve() for p in Path(directory_name).glob("**/*") if p.suffix in {".png",
     ".jpg", ".jpeg", ".gif", ".bmp"})
    
    pool = Pool()
    pool.map(f, open_files)

