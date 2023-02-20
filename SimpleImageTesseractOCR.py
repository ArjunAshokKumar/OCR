#import the necessary packages
from PIL import Image
import pytesseract
import numpy as np

def main():
    print("Enter the filename of the image to be OCR'd")
    filename = input()
    image = Image.open(filename)
    image = np.array(image)
    text = pytesseract.image_to_string(image)
    print(text)

if __name__ == '__main__':
    main()