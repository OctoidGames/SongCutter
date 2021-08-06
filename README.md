# SongCutter
cuts the begining and end off a song (mp3)

Dependencies:
 - Python3
 - ffmpeg
 - pyDub

I use media human's youtube to mp3 converter for my offline music playlist. However, some channels like to put silence in the begining and end of a song for title screens and whatnot so I made a script to cut those off. 

# using:
run the bash script to install dependencies then put the pythion script in the same folder as your playlist and run it from a terminal. 

## step by step:
#### getting the code
download code then extract the zip folder and open it in terminal
#### installing dependencies
next use `chmod +x dep.sh` to make `dep.sh` executable
next run the dependencies script with `./dep.sh`
this will install all the dependencies on your machine.
#### running the script
now take main.py and drop it into whatever folder your mp3s are in
next open a terminal in this folder
now run `python3 main.py` in your terminal.

## only for use on linux systems
 - tested on Ubuntu 20.04
