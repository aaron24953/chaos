import cv2
from time import sleep
import pytesseract
from PIL import ImageGrab
from numpy import asarray

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
)
# img=cv2.imread("textReadTest.png")
sleep(0.3)
img = ImageGrab.grab(
    bbox=(90, 330, 1300, 470)
)  # bbox=(470,210,920,230)#bbox=(145,370,1250,425)#bbox=(90,330,1300,470)
img.save("test.png")
img = cv2.imread("test.png")
gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, gimg = cv2.threshold(gimg, 200, 255, cv2.THRESH_BINARY)
cv2.imwrite("gimg.png", gimg)
# img=ImageOps.grayscale(img)
# img.save("graytest.png")
text = pytesseract.image_to_string(gimg, config="--psm 7")
print(text)
