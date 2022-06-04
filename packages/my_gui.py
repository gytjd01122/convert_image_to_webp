import tkinter as tk
from tkinter import filedialog as fd
from tkinter import simpledialog as sd

def create_simple_dialog(title, message = 1):
    return sd.askinteger(title, message, minvalue = 1, maxvalue = 10, initialvalue = 4)

def create_root_gui():
    root = tk.Tk()
    root.withdraw()
    return root

def open_directory():
    directory_name = fd.askdirectory() # 변환할 이미지 폴더 선택 다이얼로그
    return directory_name

