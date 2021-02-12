from PIL import Image
from os import listdir

path = input("What is the path of the files that need to be resized?\n")
print(path)
files = listdir(path)

for f in files:
    resized = Image.open(path+f).resize((240,320))
    resized.save(path+f)
