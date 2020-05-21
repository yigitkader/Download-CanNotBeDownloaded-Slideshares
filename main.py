#@author = dewlooper(Yigitkader)
import requests
import os
import img2pdf
from PIL import Image
from fpdf import FPDF


###Download Images From Url
endOfPage = 389 # total page number = end of page number
for i in range(1,endOfPage):
    # in addition 'i' is going to be our page number
    image_url = "linkOfSlideSharePic"+str(i)+"restOfLink"
    img_data = requests.get(image_url).content
    with open('your-path/image_name'+str(i)+'.jpeg', 'wb') as handler:
        handler.write(img_data)


###Adding Images From Folder To List
imageList = []
for i in os.listdir('your-path'):
    if "jpeg" in i: 
        imagePath = "your-path/"+str(i)
        imageList.append(imagePath)
imageList.sort()


###Make Pdf With Images
with open("pdffilename.pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in imageList if i.endswith(".jpeg")]))
