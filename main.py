
__author__      = "Yigit Kader(dewlooper))"
__email__ = "ryigitkader@gmail.com"

import requests
import os
import img2pdf
from PIL import Image
from fpdf import FPDF


#Download images from url
def downloadImages(url,endOfPage):
    try:
        image_urlList = list(url)
        for i in range(1,endOfPage):
            #!! We choose -24.element because if you use dataFull link(get web page source code),  the page number is in -24.index
            image_urlList[-24] = str(i) 
            image_url = "".join(image_urlList)
            img_data = requests.get(image_url).content
            with open('downloads/'+str(i)+'.jpeg', 'wb') as handler:
                handler.write(img_data)                       
    except:
        print("Error !")



# !! Important - slideshares 'data-full' link
URL = str(input("Enter slideshare link : \n"))  
endOfPage = int(input("Total page number : \n")) 
endOfPage += 1
downloadImages(URL,endOfPage)


#Adding images from folder to List

imageList = []
sortedList = []
for i in os.listdir('downloads'):
    if "jpeg" in i:
        page = int(i[:-5])
        sortedList.append(int(page))       

sortedList.sort()

for i in sortedList:
    imagePath="downloads/"+str(i)+".jpeg"
    imageList.append(imagePath)


#Make pdf with images
with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in imageList if i.endswith(".jpeg")]))
