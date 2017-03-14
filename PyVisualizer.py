from PIL import Image

# Setup
width = 1920
height = 1080
counter = 0
img = Image.new('RGB', (width, height), "black") # create a new black image
pixelMap = img.load() # create the pixel map
piFile = open("pi-4Million.txt")

# color constants
# 0 = white, 1 = teal, 2 = blue,  3= pink, 4= green,
# 5= orange, 6= red,   7= yellow, 8= grey, 9= black
ZERO = (255, 255, 255)
ONE = (0, 128, 128)
TWO = (0, 0, 255)
THREE = (255, 20, 147)
FOUR = (0, 201, 87)
FIVE = (255, 128, 0)
SIX = (220, 20, 60)
SEVEN = (255, 215, 0)
EIGHT = (128, 138, 135)
NINE = (41, 36, 33)

def getColor():
    c = piFile.read(1)
    if not c:
        return None
    
    if c == '0' or c == '.':
        return ZERO
    elif c == '1':
        return ONE
    elif c == '2':
        return TWO
    elif c == '3':
        return THREE
    elif c == '4':
        return FOUR
    elif c == '5':
        return FIVE
    elif c == '6':
        return SIX
    elif c == '7':
        return SEVEN
    elif c == '8':
        return EIGHT   
    return NINE


#  For every pixel
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixelMap[i, j] = getColor()

piFile.close()
img.show()
img.save("my-image.png")
        