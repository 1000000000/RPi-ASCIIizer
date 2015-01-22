#Raspberry Pi Camera ASCIIizer

---
###Description:
It is a Raspberry Pi hooked up to a camera and an LCD screen as well as.
When a button is pressed the camera will take a picture, and
the Raspberry Pi will turn it into an image that can be put
on the LCD screen (shrink it, make it two color).
Then the Raspberry Pi will display the image on the LCD screen
either in two color format or ASCII format (matches each 6x8 block of the image to the closest looking ASCII character).
ASCII format can be toggled by a button.
The program will be written in Python (it would incur significant difficulties to try and use the camera with Java since there is no library for it).

---
###Goals:
####Completed:
* Created README.md, .gitignore
* Acquired camera for Raspberry Pi
* Acquired LCD screen (Adafruit ST7565)
* Installed Raspberry Pi has operating system
* Text file containing an array of integers representing a tileset of ASCII characters
* Installed Pillow on Pi for image processing
* Image now gets scaled to fit on LCD screen before any processing
* Program converts image to black and white bitmap
* Short Term Plans:
* Write a program that reads an image from a file and makes it a two color image or “ASCIIizes” it.
    * Resources:
        * http://scipy-lectures.github.io/advanced/image_processing/
        * http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html#array-methods
        * http://docs.scipy.org/doc/numpy/reference/generated/numpy.median.html
        * http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.ndimage.imread.html
        * http://pillow.readthedocs.org/handbook/tutorial.html
        * http://stackoverflow.com/questions/384759/pil-and-numpy
        * http://docs.scipy.org/doc/numpy/reference/generated/numpy.delete.html
        * http://infohost.nmt.edu/tcc/help/pubs/pil/pil.pdf
        * http://stackoverflow.com/questions/17917749/split-a-3-dimensional-numpy-array-into-3x3-grids
        * http://effbot.org/imagingbook/image.htm#tag-Image.Image.resize
* Attach camera to Pi
* Capture when a button is pressed and process those images using the above program

####Issues:
* The process of ASCIIizing the image is slower than I would like
* The result of ASCIIizing is incorrect

####Long Term Plans:
* Write library to allow Pi to control LCD screen (ST7565) 
* Attach LCD screen to Pi


