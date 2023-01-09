# import the opencv library
import cv2
import os
import math

chars = "@#W$9876543210?!abc;:+=-,._                       "
brightnessToChar = (255 / len(chars))

# use to auto size the resolution (Scales based on terminal size)
def auto_size(frame):
    tsize = os.get_terminal_size()
    return int(tsize[0] * 100 / frame.shape[1])

#gets the charecter associated with the brightness
def get_char(brightness):
    pos = math.floor(brightness / brightnessToChar)
    return chars[(len(chars) - pos) - 1]
    
def rescale_frame_percent(frame, percent = 50):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

#loop over all pixels and do what is needed
def to_ASCII(frame):
    imageASCII = ""
    for x in range(0, frame.shape[0]):
        imageASCII += "\n"
        for y in range(0, frame.shape[1]):
            imageASCII += get_char(frame[x,y])
    print(imageASCII)
    return imageASCII

# Ask for file name
file = input("File Path for image: ")

# Image needs to be fairly low resolution for it to work in the terminal
# If needed, the rescale_frame_percent method can be used to scale an image, preserving its aspect ratio
# or use the auto_size to size it for you (according to the terminal)
try:
    # read image
    img = cv2.imread("Pictures/" + file, cv2.IMREAD_GRAYSCALE)
    # clear screen (based on different systems)
    percent = 100
    #percent = auto_size(img)
    os.system('cls' if os.name=='nt' else 'clear')
    # Manualy set image size if wanted (comment out the auto_size if desired)
    img = rescale_frame_percent(img, percent)
    imageASCII = to_ASCII(img)
    with open("ASCII/" + file.split('.')[0] + ".txt" , 'w') as f:
        f.write(imageASCII)
except AttributeError:
    print("\nNo such file is in directory. Make sure the file name is typed correctly and your file is under the \"Pictures\" directory.")
    

