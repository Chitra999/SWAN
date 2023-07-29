import pywhatkit as whatsapp
import datetime
import pandas as pd
from PIL import Image, ImageFont, ImageDraw
import os

def runBday(location) :
    print(location)
    curr = datetime.datetime.now()

    data = pd.read_excel(location, engine='openpyxl')
    Bdays = data[data["DAY"]== curr.day].head()      
    Bmon = Bdays[Bdays["MONTH"]== curr.month].head() # contains today birthdays list #
    Bph = Bmon["PHONE"].head()                       # only contains the phone numbers #
    Bname = Bmon["Student_Name"].head()              # only contains the Birthday Person Name #
    phone_num = []
    print(curr.day,"-Day, ",curr.month,"-Month")     # printing today's day and month #


    def send_Bday():
        # collecting names of bday people that is creating a list/array of the names #
        # msg = "Happy Birthday to "
        Name = []
        for Student_Name in Bname:
            Name.append(Student_Name)

        print(Name)

        # collect card # sending #
        i=0
        for PHONE in Bph:
            phone_num.append(PHONE)
            # printing names #
            print(PHONE)
            print(Name[i])
            print("--------------------")
            # editing name in bday card #
            img = Image.open('C:/Users/CHITRANSHA/Documents/Tejas/whatsapp/happybday.png')
            draw = ImageDraw.Draw(img)
            str = Name[i]
            font = ImageFont.truetype('ariali.ttf', 60)
            draw.text((img.size[0]/2, 400), str , (0,0,0), font=font, anchor="ms", stroke_width=1, stroke_fill="black")
            img.save('bb.png')
            
            # opening whatsapp #
            whatsapp.sendwhats_image(f'+91{PHONE}', 'C:/Users/CHITRANSHA/Documents/Tejas/whatsapp/bb.png', " ", tab_close = True)
            
            # removing the card #
            try:
                os.remove("bb.png")
                
            except OSError as e:                    # if failed, report it back to the user #
                print ("File is not present")
            i+=1
        print("ALL WISHES SENT SUCCESSFULLY")