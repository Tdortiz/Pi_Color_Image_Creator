from PIL import Image

# Setup
width = 1920
height = 1080
img = Image.new('RGB', (width, height), "black") # create a new black image
pixelMap = img.load() # create the pixel map
piFile = open("pi-4Million.txt")

# color constants
# 0 = white, 1 = teal, 2 = blue,  3= pink, 4= green,
# 5= orange, 6= red,   7= yellow, 8= grey, 9= black
COLORS = [
    (255, 255, 255),
    (0, 128, 128),
    (0, 0, 255),
    (255, 20, 147),
    (0, 201, 87),
    (255, 128, 0),
    (220, 20, 60),
    (255, 215, 0),
    (128, 138, 135),
    (41, 36, 33)
]

# Returns a color based off of the current char
def getColor():
    c = piFile.read(1)
    if not c:
        return None
    
    # Special case for the decimal
    if c == '.':
        c = '0'
    
    # Return a color based off char
    if representsInt(c):
        return COLORS[int(c)]
    else:
        return COLORS[len(COLORS)-1]

# Checks if the char represents an integer
def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


#  For every pixel
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixelMap[i, j] = getColor()

# Close the file
piFile.close()

# Show and save the image
img.show()
img.save("my-image.png")
        