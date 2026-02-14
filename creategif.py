import imageio.v3 as iio
import os
print("working directory: ", os.getcwd())
filenames = ['chicklet1.png','chicklet2.png','chicklet3.png','chicklet4.png']
images = []
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('team.gif', images, duration = 500, loop = 0)    