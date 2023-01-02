# import the opencv library
import cv2
import os
import math

chars = "@#W$9876543210?!abc;:+=-,._                       "
brightnessToChar = (255 / len(chars))

# clear screen (based on different systems)
os.system('cls' if os.name=='nt' else 'clear')

# rescale the frame based on percent
def rescale_frame_percent(frame, percent = 50):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

#gets the charecter associated with the brightness
def getChar(brightness):
    pos = math.floor(brightness / brightnessToChar)
    return chars[(len(chars) - pos) - 1]
    

#loop over all pixels and do what is needed
def to_ASCII(frame):
    imageASCII = ""
    for x in range(0, frame.shape[0]):
        imageASCII += "\n"
        for y in range(0, frame.shape[1]):
            imageASCII += getChar(frame[x,y])
    print(imageASCII)
            

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    realFrame = frame
    frame = rescale_frame_percent(frame, percent = 8)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    to_ASCII(frame)
    #time.sleep(1)

    # Display frame
    cv2.imshow('frame', realFrame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()