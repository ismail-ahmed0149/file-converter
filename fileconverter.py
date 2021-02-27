# The purpose of this file is to just test conversion
# between a .png file to a .pdf file

from PIL import Image

if __name__ == '__main__':
    image1 = Image.open(r"C:\Users\Ismail Ahmed\Pictures\samplepng.png")
    im1 = image1.convert('RGB')
    im1.save(r"C:\Users\Ismail Ahmed\Downloads\samplepdf.pdf")