from PIL import Image, ImageTk, ImageOps
import customtkinter as ctk
from customtkinter import filedialog
import bday 

class App(ctk.CTk) :
    def __init__ (self) :
        super().__init__()
        self.title("SWAN")
        self.iconbitmap("ww1.ico")
        self.geometry("1000x500")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        # self.config(bg = "blue")
        # self.home_page_instance = HomePage(self)
        # self.birthday_page_instance = BirthdayPage(self)
        # self.festival_page_instance = FestivalPage(self)

    def home_page(self) :
        # self.home_page_instance.create_home_page()
        HomePage(self).create_home_page()

    def birthday_page(self) :
        # self.birthday_page_instance.create_birthday_page()
        BirthdayPage(self).create_birthday_page()

    def festival_page(self) :
        # self.festival_page_instance.create_festival_page() 
        FestivalPage(self).create_festival_page()

class HomePage(ctk.CTk) :
    def __init__(self, root) :
        self.root = root

        self.swan_logo = ctk.CTkImage(Image.open("logo.png"), size=(250,325))
        # self.swan_label = ctk.CTkLabel(root , text="SWAN", font=("Cambria", 80), text_color="#04A777")
        self.swan_label = ctk.CTkLabel(root , text="", image = self.swan_logo)
        self.text1 = ctk.CTkLabel(root, text="Whatsapp Wisher is a communication tool which is capable of automating the whatsapp messages and is pretty simple and clean to use.", font=("Ariel", 14))
        self.text2 = ctk.CTkLabel(root , text="Click on the choices given below", font=("Calibri", 14))

        #self.button_frame = ctk.CTkFrame(root)
        self.birthday_button = ctk.CTkButton(root, text="Birthday", command=lambda : self.button_actions("birthday"))
        self.festival_button = ctk.CTkButton(root, text="Festivals/Holidays", command=lambda : self.button_actions("festival")) 
        self.close_button = ctk.CTkButton(root, text="Exit", command=lambda : self.root.quit())

    def create_home_page(self) :
        self.swan_label.pack()
        self.text1.pack()
        self.text2.pack()

        #self.button_frame.pack()
        self.birthday_button.pack(pady = 20)
        #self.festival_button.pack(pady = 0)
        self.close_button.pack(pady=0)

    def button_actions(self, id) :
        if id == "birthday" :
            self.destroy_home_page()
            self.root.birthday_page()
        if id == "festival" :
            self.destroy_home_page()
            self.root.festival_page()

    def destroy_home_page(self) :
        self.swan_label.destroy()
        self.text1.destroy()
        self.text2.destroy()

        self.birthday_button.destroy()
        self.festival_button.destroy()
        #self.button_frame.destroy()
        self.close_button.destroy()


class BirthdayPage()  :
    def __init__(self, root) :
        self.root = root 
        self.text1 = ctk.CTkLabel(root, text="Send Birthday Wishes :)", font=ctk.CTkFont("Calibri", 30, "bold"))
        self.text2 = ctk.CTkLabel(root, text="Select the image and contacts list", font=("Calibri", 20))
     
        self.button1 = ctk.CTkButton(root, text='Press to select an image', command=lambda : self.button_actions("image input"))   
        self.button2 = ctk.CTkButton(root, text='Press to select excel file', command=lambda : self.button_actions("file input"))

        self.label1 = ctk.CTkLabel(root, text='')
        self.label2 = ctk.CTkLabel(root, text='')

        self.label3= ctk.CTkLabel(root, text="ALL WISHES ARE SENT", font=("Calibri",20), bg_color="#2F4F4F")
        self.send_wishes_button =  ctk.CTkButton(root, text="Send the wishes", command=lambda: self.button_actions("send wishes"))
        self.go_back_button = ctk.CTkButton(root, text="Go to Home Page", command=lambda : self.button_actions("home page"))

    def create_birthday_page(self) :
        self.text1.place(x = 350, y = 20) 
        self.text2.place(x = 360, y = 65)
        self.button1.place(x = 200, y = 150)
        self.button2.place(x = 650, y = 150)
        self.label1.place(x = 195, y = 200)
        self.label2.place(x = 650, y = 250)
        self.send_wishes_button.place(x = 430, y = 400)
        self.go_back_button.place(x = 430, y = 450)
    
    def button_actions(self, id) : 
        if id == "file input" :
            self.fileInput()
        if id == "image input" :
            self.imageInput()
        if id == "home page" :
            self.destroy_birthday_page()
            self.root.home_page()
        if id == "send wishes" :
            self.import_pack()
        
    def fileInput(self):
        self.file_= filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if self.file_:
            self.label2.configure(text=self.file_)
            self.label2._text=self.file_   
        else:
            print("No file selected")

    def imageInput(self):
        file_path = filedialog.askopenfilename(
            title="Select image file",
            filetypes=(("Image files", "*.jpg;*.jpeg;*.png;*.bmp"), ("All files", "*.*"))
        )
        if file_path:
            image = Image.open(file_path)
            img = ImageOps.contain(image, (250, 200))
            img = ctk.CTkImage(img, size=(175, 175))
            self.label1.configure(image=img)
            self.label1.image = img
            image.save('happybdayF.png')
            #image.show() # display image in the default image viewer
    
    def import_pack(self) :
        bday.runBday(self.file_)
        self.label3.pack(padx=10, pady=100)

    def destroy_birthday_page(self) :
        self.text1.destroy()
        self.text2.destroy()
        self.button1.destroy()
        self.button2.destroy()
        self.label3.destroy()
        self.label1.destroy()
        self.label2.destroy()
        self.send_wishes_button.destroy()
        self.go_back_button.destroy()

class FestivalPage() :
    def __init__(self, root) :
        self.root = root 

    def create_festival_page(self) :
        None 

    def destroy_festival_page(self) :
        None

if __name__ == "__main__" :
    app_instance = App()
    app_instance.home_page()
    app_instance.mainloop()
