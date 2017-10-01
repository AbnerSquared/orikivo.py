# pylint: disable=C0301
'''
.ori.
-----------
____________________________________________\n
:Ori Retrievable Interface:\n
____________________________________________\n
A basic file reader for .ori extension files.\n
Converts .ori to .txt as well.

'''

import os
import pickle
from PIL import Image

ERR_NOTE = False

def cvt():
    '''
    A call in to convert the current string list into a `.txt` file.
    '''
    if FMT == "url":
        pass
    if FMT == "txt":
        NEW_TXT.write(FILE_TO_STR)
        NEW_TXT.close()
        os.startfile(FILE_TXT)
        disp_tcp()
    if FMT == "jpg":
        NEW_IMG.save(FILE_IMG)
        NEW_IMG.show()
        disp_tcp()

def cvt_cfm():
    '''
    A call in to check the user's response to conversion.
    '''
    if FILE_INPUT == "yes":
        cvt()
    if FILE_INPUT == "no":
        disp_fcl()




def disp_spl():
    '''
    A call in to display the splash logo for :.ori.:
    '''

    #  ~CMD Ruler:
    #     0|      10|       20|       30|       40|       50|       60|       70|       80|

    print("________________________________________________________________________________")
    print("                                                                                ")
    print("                       __________      __________      ____                     ")
    print("                     /-          -   /-          -   /-    -                    ")
    print("                    | |    ||    |  | |    //    |  | |    |                    ")
    print("                    | |    ||    |  | |    | -___-  | |    |                    ")
    print("           ______   | |    ||    |  | |    |/____/  | |    |     ______         ")
    print("         /-      -  | |    ||    |  | |    |        | |    |   /-      -        ")
    print("        | |      |  | |    ||    |  | |    |        | |    |  | |      |        ")
    print("        | -______-  | -__________-  | -____-        | -____-  | -______-        ")
    print("         /_______/   /___________/   /_____/         /_____/   /_______/        ")
    print("                              [Input a file+type.]                              ")
    print("________________________________________________________________________________")

def disp_fts():
    '''
    A call in to display the retrieved `.ori` file as organized string for each entity.
    '''
    print("\n" + "________________________________________________________________________________")
    print("                                                                                ")
    print("> {} --show".format(FILE_NAME))
    print("                                                                                ")
    print("________________________________________________________________________________")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print(FILE_TO_STR + "\n\n")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("________________________________________________________________________________" + "\n")

def disp_ott():
    '''
    A call in to display to the user if he/she would like to convert
    the displayed file into a `.txt` file.
    '''
    print("\n" + "________________________________________________________________________________")
    print("\n" + "> Would you like to import this file into a text file?")
    print("\n" + "________________________________________________________________________________")

def disp_tcp():
    '''
    A call in to display to the user that the file has been converted.
    '''
    print("\n" + "________________________________________________________________________________")
    print("\n" + "> Your file has been saved." + "\n" + "> You may now close .ori.")
    print("\n" + "________________________________________________________________________________")
    os.system("pause")

def disp_fcl():
    '''
    A call in to display to the user that the file will not convert.
    '''
    if ERR_NOTE is True:
        print("\n" + "________________________________________________________________________________")
        print("\n" + "> Restart the program, and write a correct file name.")
        print("\n" + "________________________________________________________________________________")

    if ERR_NOTE is False:
        print("\n" + "________________________________________________________________________________")
        print("\n" + "> You may now close the program.")
        print("\n" + "________________________________________________________________________________")
    os.system("pause")

def disp_tfl():
    '''
    A call in to display to the user that the file has failed to convert.
    '''
    print("\n" + "________________________________________________________________________________")
    print("> An error has occured: \n> {} \n\n> In short, a file you attempted to reference doesn't exist.".format(err))
    print("________________________________________________________________________________")

def cvt_chk():
    '''
    A call in to hold a plug-in to see if it's an existing file.
    '''
    open(FILE_NAME, "rb")

#STARTS HERE

disp_spl()
FILE = input()
FILE_NAME = FILE + ".ori"

try:
    cvt_chk()
except FileNotFoundError as err:
    disp_tfl()
    ERR_NOTE = True

if ERR_NOTE is True:
    disp_fcl()
if ERR_NOTE is False:
    OPEN_FILE = open(FILE_NAME, "rb")



    FULL_FILE = pickle.load(OPEN_FILE)



    FILE_TO_STR = "\n| " + "\n| ".join(FULL_FILE)
    FILE_TO_MSG = "\n| " + FILE_NAME
    FILE_TO_IMG = "\n| " + FILE_NAME + "\n| Images cannot be shown in raw .ori files."


    disp_fts()



    FILE_INPUT = input('').lower()



    disp_ott()



    FMT = input('').lower()



    FILE_TXT = FILE + ".txt"
    FILE_IMG = FILE + ".jpg"



    NEW_TXT = open(FILE_TXT, "w")
    NEW_IMG = Image.open(FILE_IMG + "w")


    cvt_cfm()
