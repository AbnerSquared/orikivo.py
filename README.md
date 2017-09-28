# Orikivo
A Discord.py bot that will include many methods, such as mathematics, image editing, saving, and the functionalities of multiple API, including Steam and Overwatch at one point.

## Commands:
The command extension's default is : `~`
1. img : A command used to reference saved images.
   a. edit : The sub-command that references the types of edits possible for an image.
   b. rot :
   c. flip :
   d. add : The sub-command of edit that allows you to add several methods for an image.
      - txt : The sub-command of add that allows you to add text to an image.
      - msg : The message the text will say.
      - fnt : The font name you use for the text.
        i. fns : The size of the letters for the text.
        ii. clmethod : The method used to color your text. [RGB, HEX, HSL, HTML]
        iii. clp : The primary reference used for the color. If HEX or HTML, put the full name/code here.
        iv. cls : The secondary reference used for the color, mainly towards RGB and HSL.
        v. clt : The tertiary reference used for the color, mainly towards RGB and HSL.
        vi. plmethod : The method used to place the text in the image. [POSNAME, XY]
        vii. plx : The primary reference used for the placement. If POSNAME, put the the positioning name here.
        viii. ply : The secondary reference used for the placement, mainly towards y on XY.
      - cir : The sub-command of `add` that adds a circle to an image.
      - rct : The sub-command of `add` that adds a rectangle to an image.
 sub-command that sends the image name referenced.

## Required:
- `discord.py` : library
- `PIL` : library
- `pyping` : library
- `python-valve` : library
- `BeautifulSoup 4` : library
