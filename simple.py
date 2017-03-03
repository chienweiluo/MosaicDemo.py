#-*- coding:utf-8 -*-
#!/usr/bin/env python

from tkinter import *
import tkinter
from tkinter import filedialog
import os
from PIL import Image, ImageFilter



root = tkinter.Tk()

cv = Canvas(root, bg='white')
cv.pack()

root.title('影像處理作業')
root.geometry('100x100+0+0')
root.minsize(270, 100)

label = tkinter.Label(root, text = "檔案路徑：")
label.place(x = 5, y = 5)

entry = tkinter.Entry(root)
entry.place(x = 60, y = 5)

a= entry.get()

def Browser():
    dire = tkinter.filedialog.askopenfilename(title = '選擇', filetypes = [('image','*.jpg *.bmp *.png *.ico')])
    if dire:
        entry.delete(0, tkinter.END)
        entry.insert(tkinter.END, dire)

def conv():
    path = entry.get()
    
    im = Image.open(""+path)
    im.show()
    newim = im
    for i in range(100):
        newim = newim.filter(ImageFilter.BLUR)
    newim.save("blurout.png", quality=50) #png最後
    newim.show()
        
    if path == ' ':
        tkinter.messagebox.showerror('error', 'Input path')
        return

def mosaic():
    path = entry.get()

    im = Image.open(""+path)
    im.show()
    newim= im

    def avg_clr(p):
            c = list(p.getdata())
            b = len(c)
            k = list(map(sum,zip(*c)))
            q = (int(k[0]/b),int(k[1]/b),int(k[2]/b))
            return q

    def divide(w,h,s):
            global newim
            newim= im
            boxes = [(x,y,x+s,y+s) for x in range(0,w,s) for y in range(0,h,s)]
            for box in boxes:
                snip = newim.crop(box)
                im.paste(avg_clr(snip),box)
                
    def main():
            divide(newim.size[0],newim.size[1],20)
            newim.show()
            newim.save("mosaicout.png")

    main()

frame = tkinter.Frame(root)                                                     
frame.place(x = 100, y = 40)

buttonBrowser = tkinter.Button(root, text = 'Browser', command = Browser)
buttonBrowser.place(x = 200, y = 5)

button2 = tkinter.Button(frame, text = "模糊化", command = conv)
button2.pack(side=tkinter.BOTTOM)

button3=tkinter.Button(frame, text="馬賽克", command = mosaic)
button3.pack(side=tkinter.BOTTOM)



#--------------

menu = tkinter.Menu()
submenu = tkinter.Menu(menu, tearoff =  0)                      
submenu.add_command(label="Open")                                       
submenu.add_separator()                                                         
submenu.add_command(label="Close")
menu.add_cascade(label="File", menu = submenu)          

submenu = tkinter.Menu(menu, tearoff =  0)
submenu.add_command(label="About")
menu.add_cascade(label="Help", menu = submenu)



root.config(menu=menu)
root.mainloop()

#if __name__ == '__main__':
