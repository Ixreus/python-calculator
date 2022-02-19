from distutils import command
from tkinter import *


#        ,--.
#    ,--/  /|   ,---,                                                        ,--,
# ,---,': / ' ,--.' |                   ,-.----.                           ,--.'|
# :   : '/ /  |  |  :                   \    /  \        ,---,     ,---.   |  | :
# |   '   ,   :  :  :                   |   :    |   ,-+-. /  |   '   ,'\  :  : '      .--.--.
# '   |  /    :  |  |,--.    ,--.--.    |   | .\ :  ,--.'|'   |  /   /   | |  ' |     /  /    '
# |   ;  ;    |  :  '   |   /       \   .   : |: | |   |  ,"' | .   ; ,. : '  | |    |  :  /`./
# :   '   \   |  |   /' :  .--.  .-. |  |   |  \ : |   | /  | | '   | |: : |  | :    |  :  ;_
# |   |    '  '  :  | | |   \__\/: . .  |   : .  | |   | |  | | '   | .; : '  : |__   \  \    `.
# '   : |.  \ |  |  ' | :   ," .--.; |  :     |`-' |   | |  |/  |   :    | |  | '.'|   `----.   \
# |   | '_\.' |  :  :_:,'  /  /  ,.  |  :   : :    |   | |--'    \   \  /  ;  :    ;  /  /`--'  /
# '   : |     |  | ,'     ;  :   .'   \ |   | :    |   |/         `----'   |  ,   /  '--'.     /
# ;   |,'     `--''       |  ,     .-./ `---'.|    '---'                    ---`-'     `--'---'
# '---'                    `--`---'       `---`


print(
    """
|  _________________  |
| | KP           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
    """
)


def yaz(x):
    s = len(gir.get())
    gir.insert(s, str(x))


hesap = 5
t1 = 0


def isl(x):
    global hesap
    hesap = x
    global s1
    s1 = float(gir.get())
    print(hesap)
    print(s1)
    gir.delete(0, "end")


s2 = 0


def calculate():
    global s2
    s2 = float(gir.get())
    print(s2)

    global hesap
    sonuc = 0
    if(hesap == 0):
        sonuc = s1 + s2
    elif(hesap == 1):
        sonuc = s1 - s2
    elif(hesap == 2):
        sonuc = s1 * s2
    elif (hesap == 3):
        sonuc = s1 / s2
    gir.delete(0, "end")
    gir.insert(0, str(sonuc))


def sil():
    gir.delete(0, 'end')


sayfa = Tk()
sayfa.geometry("250x400")
gir = Entry(font="Arial 14 bold", background="#FFD9D9",
            width=16, justify="right")
gir.place(x=20, y=20)
sayfa.resizable(0, 0)
sayfa.configure(background="#BAD6FD")
sayfa.title("Hesap Makinesi")
# sayfa.iconbitmap("C:\Yeni klasör\icon.ico")

b = []

for i in range(1, 10):
    b.append(Button(text=str(i), font="Verdana 14 bold",
             background="#8D9CF4", command=lambda x=i: yaz(x)))

timer = 0

for i in range(0, 3):
    for j in range(0, 3):
        b[timer].place(x=20+j*50, y=50+i*50)
        timer += 1

islem = []

for i in range(0, 4):
    islem.append(Button(font="Arial 14 bold", background="#8D9CF4",
                 width=2, command=lambda x=i: isl(x)))

islem[0]["text"] = "+"
islem[1]["text"] = "-"
islem[2]["text"] = "*"
islem[3]["text"] = "/"


for i in range(0, 4):
    islem[i].place(x=170, y=50+50*i)

sb = Button(text=0, font="Arial 14 bold",
            background="#8D9CF4", command=lambda x=0: yaz(x))
sb.place(x=20, y=200)

nb = Button(text=".", font="Arial 14 bold", width=2,
            background="#8D9CF4", command=lambda x=".": yaz(x))
nb.place(x=70, y=200,)

eb = Button(text="=", font="Arial 14 bold",
            background="#8D9CF4", width=2, command=calculate)
eb.place(x=120, y=200)

temizle = Button(text="Clear", fg="#4D2A4F", font="Arial 14 bold",
                 background="#F67280", width=13, justify="right", command=sil)
temizle.place(x=30, y=250)


mainloop()
