import tkinter as tk
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System Developed by Team Null")
        
        #--------Title----------------
        
        title=Label(self.root,text="Inventory Management System",font=("times new roman",40,"bild")).place(x=0,y=0,relwidth=1,height=70)
        root=Tk()
        obj=IMS(root)
        root.mainloop()