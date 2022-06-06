'''
    main.py
'''
from pathlib import Path

from packages import convert_img_to_webp as convert_img
from packages import manage_thread as th
from packages import my_gui as g

def main():
    '''
        main 함수
    '''

    # thread 관련 변수
    threads_list = []

    # GUI 관련
    directory_name = g.open_directory()
    max_thread = g.create_simple_dialog('최대 스레드 개수','최대 스레드 개수를 입력하세요')
    open_files = (p.resolve() for p in Path(directory_name).glob("**/*") if p.suffix in {".png",
     ".jpg", ".jpeg", ".gif", ".bmp"})
    th.create_thread(threads_list, max_thread, convert_img.convert_image_to_webp, open_files)

    th.run(threads_list)
    th.end(threads_list, '모든 스레드가 종료되었습니다.')

if __name__ == '__main__':
    main()
    