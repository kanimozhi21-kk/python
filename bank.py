import tkinter
from tkinter import*
from tkinter import ttk,font

def customerlog(r):
    r.destory()
    r=Tk()
    r.geometry("600x400")
    frame=frame(height=1300,width=40,bg="yellow").pack()
    label_font=font.Front(weight="bold",family="times new romas",size=30)
    label(r,text=text,font=label_font).place(relx=0.5,rely=0.45)
