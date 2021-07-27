#importing the necessary packages
import xlrd
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

#opening the excel sheet that contains information
loc = ("FINAL_PROJECT_EXCEL.xlsx")
wb = xlrd.open_workbook(loc)


#initializing the excel pointer to (0,0)
sheet = wb.sheet_by_index(0)

#adding the each entry from the excel sheet to the list 

details=[]


for i in range(sheet.nrows):
    temp=[]
    temp.append(sheet.row_values(i)[0])
    temp.append(sheet.row_values(i)[1])
    temp.append(sheet.row_values(i)[2])
    details.append(temp)


j=1

for i in details:

    #opening the image using the image module
    im = Image.open(r'D:\python programs\template.jpg')

    #passing the image object to the draw to draw the 2D images
    d = ImageDraw.Draw(im)

    #specifying the location in which the text image needs to be drawn
    location = (50, 230)

    #specifying the color code in RGB
    text_color = (0, 137, 209)

    #setting the text image font and the font size
    font = ImageFont.truetype("arial.ttf", 60)

    #drawing the image using all the details such as
    #location text color font details
    d.text(location, i[0], fill = text_color, font = font)

    #doing the same for the other details 

    location = (50, 310)
    font = ImageFont.truetype("arial.ttf", 30)
    text_color = (0, 137, 209)
    d.text(location, i[1], fill = text_color, font = font)

    location = (680,30)
    font = ImageFont.truetype("arial.ttf", 30)
    text_color = (0, 137, 209)
    d.text(location, i[2], fill = text_color, font = font)
    #saving the certificate in the same folder along with the name in excel

    im.save("certificate_" + str(j) + ".jpg")
    j+=1
print("Program Completed Successfully!")
