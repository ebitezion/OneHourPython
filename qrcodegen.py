import qrcode
import os
#qrcode generator 
img=qrcode.make('https://google.com/')

img.save("googleqr.png","PNG")

os.system("open googleqr.png")
