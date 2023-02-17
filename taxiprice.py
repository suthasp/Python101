from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
import tkinter as tk

GUI = Tk()#นี่คือจอหลักของโปรแกรม
GUI.title('โปรแกรมคำนวนค่า TAXI')
GUI.geometry('600x400+200+100')#'กำหนดขนาดหน้าจอ+X+Y'

label = Label(GUI,text = 'ป้อนระยะทาง(กิโลเมตร) : ',font=('Tahoma',12),fg='red')
label.place(x=150,y=50)
input1 = tk.Entry(GUI,bg='yellow',fg='black')
input1.place(x=315,y=55)

s = ttk.Style() #Font Styel
s.configure('my.TButton', font=('Tahoma', 12),foreground='blue')
FB1 = ttk.Button(GUI,text='โปรแกรมคำนวนค่า TAXI ตามระยะทาง',style='my.TButton')
FB1.pack()

#####################
def Button2(): #function Taxi price
    kilometre = int(input1.get())
    kilo = int(input1.get())
    price = int(0)
    if kilo > 80:
        x_kilo = (kilo - 80)
        price += x_kilo * 10.50
        kilo -= x_kilo
    if kilo > 60:
        x_kilo = (kilo - 60)
        price += x_kilo * 9
        kilo -= x_kilo 
    if kilo > 40:
        x_kilo = (kilo - 40)
        price += x_kilo * 8.5
        kilo -= x_kilo
    if kilo > 20:
        x_kilo = (kilo - 20)
        price += x_kilo * 8
        kilo -= x_kilo
    if kilo > 10:
        x_kilo = (kilo - 10)
        price += x_kilo * 7
        kilo -= x_kilo
    if kilo > 1:
        x_kilo = (kilo - 1)
        price += x_kilo * 6.50
        kilo -= x_kilo
    if kilo == 1:
        price += 35
    if round(price) % 2 == 0:
        price += 1
    #print('\nระยะทาง %.0f'% kilometre,'กิโลเมตร','ค่าแท็กซี่ทั้งหมด %.0f บาท'% price);
    text = 'ราคาค่าแท็กซี่ทั้งหมด %.0f บาท' % price
    messagebox.showinfo('ค่าแท็กซี่ทั้งหมดตามระยะทาง',text)

#####################
FB2 = LabelFrame(GUI) #คล้ายกระดาน
FB2.place(x=210,y=100)
B2 = ttk.Button(FB2,text='กดปุ่มเพื่อคำนวนราคา',style='my.TButton',command=Button2)#เรียกใช้ Function Button2()
B2.pack(ipadx=10,ipady=10)
##################
