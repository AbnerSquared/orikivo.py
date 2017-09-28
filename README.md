# Orikivo
A Discord.py bot that will include many methods, such as mathematics, image editing, saving, and the functionalities of multiple API, including Steam and Overwatch at one point.

## Commands:
The command extension's default is : `~`

<ol type="a">
   <li>img : A command used to reference saved images.
   <ul>
      <li>edit : The sub-command that references the types of edits possible for an image.
      <ul>
         <li>rot :</li>
         <li>flip :</li>
         <li>add : The sub-command of edit that allows you to add several methods for an image.
         <ul>
            <li>txt : The sub-command of add that allows you to add text to an image.
            <ul>
               <li>msg : The message the text will say.</li>
               <li>fnt : The font name you use for the text.</li>
               <li>fns : The size of the letters for the text.</li>
               <li>clmethod : The method used to color your text. [RGB, HEX, HSL, HTML]</li>
               <li>clp : The primary reference used for the color. If HEX or HTML, put the full name or code here.</li>
               <li>cls : The secondary reference used for the color, mainly towards RGB and HSL.</li>
               <li>clt : The tertiary reference used for the color, mainly towards RGB and HSL.</li>
               <li>plmethod : The method used to place the text in the image. [POSNAME, XY]</li>
               <li>plx : The primary reference used for the placement. If POSNAME, put the the positioning name here.</li>
               <li>ply : The secondary reference used for the placement, mainly towards y on XY.</li>
            </ul>
            </li>
            <li>cir : The sub-command of add that adds a circle to an image.</li>
            <li>rct : The sub-command of add that adds a rectangle to an image.</li>
         </ul>
         </li>
      </ul>
      </li>
      <li>view : The sub-command that sends the image name referenced.</li>
</ol>

## Required:
- `discord.py` : library
- `PIL` : library
- `pyping` : library
- `python-valve` : library
- `BeautifulSoup 4` : library
