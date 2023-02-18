# Overview

I wanted to learn how to communicate with other computers using python. I also wanted to learn how to make other computers do work for other computers. With this software, in order to run it properly, you just need to run the server.py on the computer that you want to do the processing. With the client computers, you will need to grab the IP address (either private or public) and alter such accordingly within the client.py file.

This program only executes python files, so no other programming languages. You also are going to need to place the file you wanted executed in the same directory as the client.py file. Typically if you have errors loading the file in the client.py, it either has to do with you not putting the full file extension or it cannot find the file.

I wanted to write this piece of software as I was studying recursion, I noticed that my laptop could not do inefficent recursion very well. My PC on the off hand, could do it a lot faster. And so I started to think about how I would solve this problem if I had to run slow Python Programs while I was on my laptop and this was the solution to my problem. (In case you are wondering I came across tail-recursion and have done more efficient programming in terms of O efficiency) 


[Software Demo Video](https://youtu.be/7yfQNL8UOEk)

# Network Communication

I used a server-to-peer architecture, though I only used peer-to-peer sockets.

I am using TCP and the sole port being used is 9091.

The format of the messages being sent are strings that are converted into byte datatypes.

# Development Environment

VScode
Python 3.11.1

Libraries:
-socket
-time
-multiprocessing
-os
-subprocess
-sys

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Python (multiprocessing)](https://docs.python.org/3/library/multiprocessing.html)
* [Python (socket)](https://docs.python.org/3/library/socket.html?highlight=socket#module-socket)
* [Python (subprocess)](https://docs.python.org/3/library/subprocess.html?highlight=subprocess#module-subprocess)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* I need to adjust server.py to allow files be completed in a multiprocess fashion.
* I want to make client.py more memory efficient when listening for messages from the server
* I want to make it so that client.py can recieve multiple outputs (for a python file that does multiple print statements)