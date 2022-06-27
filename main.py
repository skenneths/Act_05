import cv2 as cv
import numpy as np
import os
filepath = "os.jpg"
img = cv.imread(filepath)
windowTitle = "Operating System"

if (len(img.shape)<3):  
    pic = cv.imread('117013.jpg')
    print("Error.. The image is Grayscale!")
    print("Press Enter")
    cv.waitKey(0)
    cv.destroyAllWindows()

shapes = img.shape
print("Input Pixel:")
x = int(input("Enter 'x' coordinate value (max value "+str(shapes[0])+" ) : "))
y = int(input("Enter 'y' coordinate value (max value "+str(shapes[1])+" ) : "))
ch = int(input("""Select channel:
0 - blue
1 - green
2 - red
>> """))

angle = img.item(x,y,ch)
shapes = img.shape
print("Modify a Pixel")
x = int(input("Enter 'x' coordinate value (max value "+str(shapes[0])+" ) : "))
y = int(input("Enter 'y' coordinate value (max value "+str(shapes[1])+" ) : "))
blue = int(input("Enter blue channel value: "))
green = int(input("Enter green channel value: "))
red = int(input("Enter red channel value: "))


print("Output: ")

print("\nAccessed Pixel Value:", angle)

print("Pixel value before modify:", img[x, y])

img.itemset((x, y, 0), blue)
img.itemset((x, y, 1), green)
img.itemset((x, y, 2), red)

print("Pixel value after modified:", img[x, y])

lapad = 300
taas = 300

if lapad > shapes[1] or taas > shapes[0]:
    print("Set Image Dimension: Out of bounderies")
else:
    print("Set Image Dimension: Within the bounderies")

pixel = 1683001

if pixel > img.size: print("Set pixel: Higher than the pixel count")

elif pixel < img.size: print("Set pixel: Lower than the pixel count")

else: print("Set pixel: Equal to the pixel count")

print("Image Data Type:", img.dtype)