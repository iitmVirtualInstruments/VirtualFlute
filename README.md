# VirtualFlute
A repository containing the arduino code and the python code used to make a virtual flute. 
FL Studio was the music software used to play the sounds.

# Mechanical and Electronic Part
The Virtual Flute was made with a combination of flex sensors and a pressure sensor. While the flex sensors on the fingers helped to detect the finger's position, the pressure sensor placed on the left-hand thumb changed the scale when the lip was pressed against it. 
Almost all notes in a flute can be played using flex sensors on left hand – index, ring and middle fingers and right hand – index,middle and ring fingers. 
The Arduino code interprets the position of the fingers based on the resistance values obtained from the flex sensors attached to the fingers and also detects the scale in which to play depending on the input from the pressure sensor.The Python Code on the laptop generates a keyboard event to play keys on FL Studio.
 
# Source Programs
* flute.ino : Arduino code to receive data from the flex sensors and the pressure sensor.
* flute.py : Python code which acts as interface between the arduino and FL Studio.

# Dependencies
* Arduino IDE 1.6
* Python (version 3)
* FL Studio 12


