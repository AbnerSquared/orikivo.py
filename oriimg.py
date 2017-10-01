'''
test
'''
import os
import pickle
from PIL import Image

FILE = input()
FILE_N = FILE + ".ori"

OPEN_F = open(FILE_N, "rb")
FF = pickle.load(OPEN_F)
#FO = exec compile(FF)

FILE_IMG = FILE + ".jpg"

SI = (500, 500)
COLOR = 0, 0, 255
F_IMG = Image.new(mode='RGB', size=SI, color=COLOR)
F_IMG2 = Image.open(FF)
F_IMG2.show()
os.system("pause")
