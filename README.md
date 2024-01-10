# MUSYNC
<hr>
<div align="center">
<<<<<<< HEAD
    <img src="icon.ico" height=300> 
=======
    <img src="readme/logo.png" height=300> 
>>>>>>> 158f52ec6ff2b5bc30be2bda1dee027a6ddb77ad
    <p>Music Visualizer in Python</p>
</div>

<hr>

## Language Used: 
<div align="center">
<img src="readme/python.png" height=70>
</div>

<hr>

## Libraries Used:
<div align="center">
    <img src="readme/Numpy.png" height=70> 
    <img src="readme/pygame.webp" height=70>
    <img src="readme/scipy.png" height=70>
    <img src="readme/ffmpeg-python.png" height=70>
</div>

<hr>

## About:
<<<<<<< HEAD
`Musync` is a simple Music Visualizer written in Python Programming Language made in order to enjoy some visuals along with casually played music. It supparts the feature of Drag-&-Drop audio file to play it. `Musync` is able to play an audio file if it is in any one of the following formats: (.wav, .mp3, .ogg, .flac, .opus, .m4a, .raw).
 
The script *musync.py* can be converted to an application using `auto-py-to-exe`.
=======
`Musync` is a simple Music Visualizer written in Python Programming Language made in order to enjoy some visuals along with casually played music. `Musync` is able to play any audio file if it is in a format supported by `ffmpeg`.
 
The script *musync.py* can converted to an executable using `pyinstaller` hence can be run from terminal itself.

Another file namely player.py is provided to test any code upgrades and changes before implementing it in the main file. It can be run through the `python player.py` command.
>>>>>>> 158f52ec6ff2b5bc30be2bda1dee027a6ddb77ad

<hr>

## Build Application:

make sure you have <a herf="https://ffmpeg.org/download.html">ffmpeg</a> installed in your system. 

<<<<<<< HEAD
and for necessary Python Libraries, simply run:
```
pip install -r requirements.txt
=======
2. Through Terminal

- Convert the musync.py to exe:
```
pyinstaller --onefile musync.py
```
- Navigate to *dist* directory in the same folder, open terminal and run:
```
musync --play "path to an audio file"
>>>>>>> 158f52ec6ff2b5bc30be2bda1dee027a6ddb77ad
```

Now open terminal and run:

```
auto-py-to-exe
```

<<<<<<< HEAD
triggering a `Auto Py To Exe window`. To know more about the process visit <a href="https://pypi.org/project/auto-py-to-exe/">here</a>.

> in option Script Location : add path to `musync.py`
> in option Onefile : select One File
> in option Console Window: select Window Based (hide the console)
> in option Icon : add path to `icon.ico`
> in option Additional Files : add path to logo.png
> Click CONVERT .PY TO .EXE

after finishing an `output` folder will appear containing the  `musync.exe` application. Copy and add logo.png to this folder(`output`) also.
=======
To reflect any changes made to *musync.py* to the `.exe`, run the following command:
```
pyinstaller --onefile musync.py
```
>>>>>>> 158f52ec6ff2b5bc30be2bda1dee027a6ddb77ad

<hr>

## Musync in Action:
<div align="center">
    <img src="readme/waiting.png"> 
    <img src="readme/playing.png">
</div>

<hr>

<<<<<<< HEAD
=======
## To install requirements:

for Windows:
```
winget install ffmpeg
```

for Ubuntu:
```
apt install ffmpeg
```

and for necessary Python Libraries, simply run:
```
pip install requirements.txt
```

<hr>

>>>>>>> 158f52ec6ff2b5bc30be2bda1dee027a6ddb77ad
<u>Any suggestions, improvements, and feedback is welcome.</u>
