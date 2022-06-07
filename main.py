from PIL import Image
from io import BytesIO
import os

# make output folder
newpath = r"C:\Users" #output folder path
if not os.path.exists(newpath):
    os.makedirs(newpath)
print("made folder")


# configuration
COMPRESS_QUALITY = 10 # image quality(default75, 0(min)~95(max)）

# get image in folder
path = r"C:\Users\...\testImage" #input folder path
files = os.listdir(path)
if len(files) == 1:
    flag = True:
    print(f"(compression {len(files)} Images)")
elif len(files) >=2:
    flag = True:
    print(f"(compression {len(files)} Image)")
else:
    flag = False:
    print(f"({path} is empty)")
    print("add image in testImage")

# only JPG
if flag == True:
    for i in range(len(files)):
        file_name = os.path.splitext(os.path.basename(files[i]))[0]
        with open("./imgfile/" + files[i], 'rb') as inputfile:
            # get binary mode file as PIL image
            im = Image.open(inputfile)
            # compress
            im_io = BytesIO()
            im.save(im_io, 'JPEG', quality = COMPRESS_QUALITY)
        with open("result/" + 'comp_' + file_name + str(i) + '.jpg', mode='wb') as outputfile:
            # write
            outputfile.write(im_io.getvalue())

    resultfiles = os.listdir(newpath)
    if len(files) == len(resultfiles):
        print("all collect")
    else:
        print("something failed")

    