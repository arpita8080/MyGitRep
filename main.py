import tkinter as tk
from tkinter import messagebox
#import mysql.connector
#from mysql.connector import Error

#from PIL import ImageTk, Image
import os

class home:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title("Arpita's DVD Store")
        self.master.geometry("387x200")
        #self.img = ImageTk.PhotoImage(Image.open("True1.gif"))
        #self.panel = Label(self.master, image = self.img)
        #self.panel.pack(side = "bottom", fill = "both", expand = "yes")
        self.menubar = tk.Menu(self.master)
        self.menubar.add_command(label="Add a DVD", command=self.addadvd)
        self.menubar.add_command(label="Search", command=self.search)
        self.menubar.add_command(label="Modify a DVD", command=self.modify)
        self.menubar.add_command(label="Delete a DVD", command=self.delete)
        self.menubar.add_command(label="Exit", command=self.exit)
        self.master.config(menu=self.menubar)   
        self.frame.pack()
        
    def addadvd(self):
        self.newWindow = tk.Toplevel(self.master)
        AddDVD(self.newWindow)
        
    def search(self):
        self.newWindow = tk.Toplevel(self.master)
        Search(self.newWindow)
        
    def modify(self):
        self.newWindow = tk.Toplevel(self.master)
        Modify(self.newWindow)
        
    def delete(self):
        self.newWindow = tk.Toplevel(self.master)
        Delete(self.newWindow)

    def exit(self):
        self.master.destroy()

class AddDVD:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.tkvar = tk.StringVar(self.master)
        self.genrelist = {'Drama','Horror','Comedy','Romance','Action'}
        self.master.title("Add a DVD")
        self.master.geometry("400x250")
        self.titleL = tk.Label(self.master, text = "Title :").place(x = 30,y = 30)
        self.titleE = tk.Entry(self.master,width = 25).place(x = 160, y = 30)
        self.starL = tk.Label(self.master, text = "Star :").place(x = 30,y = 70)
        self.starE = tk.Entry(self.master,width = 25).place(x = 160, y = 70)
        self.yorL = tk.Label(self.master, text = "Year of Release :").place(x = 30,y = 110)
        self.yorE = tk.Entry(self.master,width = 25).place(x = 160, y = 110)
        self.genreL = tk.Label(self.master, text = "Genre :").place(x = 30,y = 150)
        self.genrePM = tk.OptionMenu(self.master, self.tkvar, *self.genrelist).place(x = 160,y = 150)
        self.quitButton = tk.Button(self.master, text = 'Add', width = 10, command = self.add_dvd).place(x = 160,y = 190)
        self.frame.pack()
    def add_dvd(self):
        mysql.connector.connect()
        connection = mysql.connector.connect(host='arpita-machine',
                                         database='DVDSTORE',
                                         user='arpita',
                                         password='Pass@1234')
        mySql_Create_Table_Query = """CREATE TABLE DVD ( 
                             Id int(11) NOT NULL,
                             Title varchar(250) NOT NULL,
                             Star varchar(250) NOT NULL,
                             YOR varchar(4) NOT NULL,
                             Genre varchar(8) NOT NULL
                             PRIMARY KEY (Id)) """

        cursor = connection.cursor()
        result = cursor.execute(mySql_Create_Table_Query)
        
        tk.messagebox.showinfo("information","DVD information Added")
        self.master.destroy()
        
class Search:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Search', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

class Modify:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Modify', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

class Delete:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Delete', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()


def main(): 
    root = tk.Tk()
    home(root)
    root.mainloop()

if __name__ == '__main__':
    main()
