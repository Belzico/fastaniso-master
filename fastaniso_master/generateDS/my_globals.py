#single img
from threading import current_thread
import threading

rute_download=""
rute_img=""

#multiple images
rute_download_multiple=""
rute_img_multiple=""

my_parameters=None

current_threads=0
max_threads=3

ani_second=None

#c:\Users\Bell\Documents\GitHub\Perona-Malik (Dark)\Perona-Malik (Dark)\ds_ini
root_dir = 'c:\Users\Bell\Documents\GitHub\Perona-Malik (Dark)\Perona-Malik (Dark)\ds_ini'

#c:\Users\Bell\Documents\GitHub\Perona-Malik (Dark)\Perona-Malik (Dark)\ds_final
final_root_dir='c:\Users\Bell\Documents\GitHub\Perona-Malik (Dark)\Perona-Malik (Dark)\ds_final'


my_lock=threading.Lock()