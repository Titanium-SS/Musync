# MUSYNC
<hr>
<div align="center">
    <img src="readme/logo.png" height=300> 
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
`Musync` is a simple Music Visualizer written in Python Programming Language made in order to enjoy some visuals along with casually played music. `Musync` is able to play any audio file if it is in a format supported by `ffmpeg`.
 
The script *musync.py* can converted to an executable using `pyinstaller` hence can be run from terminal itself.

Another file namely player.py is provided to test any code upgrades and changes before implementing it in the main file. It can be run through the `python player.py` command.

<hr>

## How to Use:
1. By script 

Run the player.py file in any **IDE** of your choice.
<br><br>

2. Through Terminal

- Convert the musync.py to exe:
```
pyinstaller --onefile musync.py
```
- Navigate to *dist* directory in the same folder, open terminal and run:
```
musync --play "path to an audio file"
```

This takes a few seconds and then a MUSYNC window will appear, simultaneously playing the music as well as visualizing it. 

You can add the path to the *musync.exe* in *dist* directory to your System Path so that the musync command is available globally. 

To reflect any changes made to *musync.py* to the `.exe`, run the following command:
```
pyinstaller --onefile musync.py
```

<hr>

## Musync in Action:
https://github.com/Titanium-SS/Musync/blob/main/readme/musync_in_action.mp4

<hr>

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

<u>Any suggestions, improvements, and feedback is welcome.</u>
