'''
    UI 생성 모듈
'''
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import simpledialog as sd

def create_simple_dialog(title, message = 1):
    '''
            간단한 다이얼로그 생성 함수

            Parameters:

            Returns:
                (int) : 사용자가 선택한 값
    '''
    return sd.askinteger(title, message, minvalue = 1, maxvalue = 10, initialvalue = 4)

def create_root_gui():
    '''
        최상위 프레임 생성
    '''
    root = tk.Tk()
    root.withdraw()
    return root

def open_directory():
    '''
            간단한 다이얼로그 생성 함수

            Parameters:

            Returns:
                directory (str) : 사용자가 선택한 폴더 경로
    '''
    directory_name = fd.askdirectory() # 변환할 이미지 폴더 선택 다이얼로그
    return directory_name