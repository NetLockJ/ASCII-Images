# ASCII-Images
This provides Python files for converting video and pictures to ASCII images. You will need the latest version of python as well as opencv-python for it to work.

<img src="https://www.pngitem.com/pimgs/m/159-1595932_python-logo-png-transparent-images-logo-transparent-background.png" height=200px>

Which turns into

<img src="https://github.com/NetLockJ/ASCII-Images/blob/main/ASCIIPython.png" height=400px>

(The given image is taken at 10% resolution)


`Picture.py` allows you to take any image and turn it into ASCII text. All you need to do is provide a file path upon running the program, and it will spit out your ASCII text. The default setting is to try your image at 50% resolution which you can change with the `resolution` variable in `Picture.py`.

You can un-comment the `percent = auto_size(img)` method to size it according to your current terminal. You can play around with different resolutions as you see fit. This will only work with the current terminal size, so if you want the higher resolution in the txt file, comment out this line. `python.txt` is an example done with this and my current terminal size. It will vary based on your set terminal size.

Using `Picture.py` will also provide a `.txt` file in the ASCII Folder. The best way to see the results is to open up your native text editor and decrease the font size to see the results. The picture of the Python logo was done in this way.

`Camera.py` works upon running the python file and will print out what the camera sees in ASCII to the terminal. A python window will also open displaying what the camera feed looks like.

`Video.py` works in a similar way, but prints out the provided video to the terminal. Place video files in the `Video` folder to allow the program access to them.

To install python, go to [Python's Website](https://www.python.org/downloads/) to install the latest version of python. Then install the latest version of [pip](https://pip.pypa.io/en/stable/installation/) for your platform (should be installed when python gets installed, but if it didn't). To check to ensure it is installed, you can run a `pip --version` and if you don't get an error, it is installed. Then run `pip install opencv-python` to get the latest version of opencv-python. If you have any issues, check around online as there are many guides/tutorials to get and install python tools.
