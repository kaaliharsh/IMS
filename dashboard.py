from tkinter import*
from PIL import Image,ImageTk         #for image view
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System Developed by Team Null")
        
        #--------Title----------------------------------
        self.icon_title=PhotoImage(file="images/logo_ims.png")
        
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",padx=20,anchor="w").place(x=0,y=0,relwidth=1,height=70)
        
        
        #----------logout button-------------------------
        btn_logout=Button(self.root,text="Log out", font=("times new roman"))
        
        
root=Tk()
obj=IMS(root)
root.mainloop() 