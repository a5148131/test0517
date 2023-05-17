import requests
from bs4 import BeautifulSoup 
import tkinter as tk
import string
from PIL import Image,ImageTk

def _clean():
    listBox.delete(0,tk.END)

def _end():
    wiN.destroy()

def _show():
    global urL
    if var.get() == "即時":
        urL = "https://udn.com/news/breaknews/1"
    elif var.get() == "運動":
        urL = "https://udn.com/news/cate/2/7227"
    elif var.get() == "生活":
        urL = "https://udn.com/news/cate/2/6649"
    elif var.get() == "數位":
        urL = "https://udn.com/news/cate/2/7226"
    elif var.get() == "兩岸":
        urL = "https://udn.com/news/cate/2/6640"

    rQ=requests.get(urL).text
    souP=BeautifulSoup(rQ,"html5lib")
    soupS=souP.find("div","context-box__content story-list__holder story-list__holder--full")

    for mySoup in soupS.find_all("div","story-list__text"):
        title = mySoup.a.text.strip()
        url = "https://udn.com" + mySoup.a["href"]
        desc = mySoup.p.text.strip()

        listBox.insert(tk.END, title)
        listBox.insert(tk.END, url)
        listBox.insert(tk.END, desc)
        listBox.insert(tk.END, "-------------------------------------------")

def _hit():
    global listBox,texT
    wiN1=tk.Toplevel(wiN)
    wiN1.title("Hello!!!")
    wiN1.geometry("800x600+200+20")
    
    s,=listBox.curselection()#獲取listbox的索引(點擊左鍵後)，加逗號是要一一對應元組中的元素，不加則直接變一個元組
    ss=listBox.get(s)
    rQ1=requests.get(ss).text
    
    souP1=BeautifulSoup(rQ1,"html5lib")
    soupS1=souP1.find("section","article-content__wrapper")
    chinese_content = ''
    KK1=soupS1.find("h1","article-content__title")
    for c in KK1:#過濾英文字
            if c not in string.ascii_letters + string.punctuation:
                chinese_content += c
    KK2=soupS1.find("div","article-content__paragraph").section.text
    for c in KK2:
            if c not in string.ascii_letters + string.punctuation:
                chinese_content += c

    
                
    btN11 = tk.Button(wiN1, text="關閉", font=("Arial", 12), width=10, height=2, command=wiN1.destroy)
    btN11.pack() 
    
    
    sBar=tk.Scrollbar(wiN1)
    sBar.pack(side=tk.RIGHT,fill=tk.Y)

    texT=tk.Text(wiN1, font=("Arial", 20),yscrollcommand=sBar.set,height=15)
    texT.pack(side=tk.BOTTOM, fill=tk.BOTH)
    sBar.config(command=texT.yview)
#    texT.insert(tk.END,KK1)
    texT.insert(tk.END,chinese_content)
    

wiN = tk.Tk()

wiN.title("Welcome!!!")
wiN.geometry("1000x800+200+20")
wiN.configure(bg='skyblue')
wiN.resizable(width=False, height=False)

img=Image.open("newspaper.jpg")
img=img.resize((1000,800))
img=ImageTk.PhotoImage(img)
imLabel=tk.Label(wiN,image=img)
imLabel.place(x=0, y=0, relwidth=1, relheight=1)

var = tk.StringVar(wiN)
box = tk.OptionMenu(wiN, var, "即時", "運動","生活","數位","兩岸")
box.config(width=10,height=2,font=("標楷體",20),fg="blue")
box.place(x=80,y=60)

btN1 = tk.Button(wiN, text="收集!!",fg="green", font=("Arial", 16), width=10, height=2, command=_show)
btN1.pack() 
btN2 = tk.Button(wiN, text="清除!!",fg="green", font=("Arial", 16), width=10, height=2, command=_clean)
btN2.pack() 
btN3 = tk.Button(wiN, text="結束!!",fg="green", font=("Arial", 16), width=10, height=2, command=_end)
btN3.pack() 
btN4 = tk.Button(wiN, text="開啟網頁!!",fg="green", font=("Arial", 16), width=10, height=2, command=_hit)
btN4.place(x=300,y=60) 


sBar=tk.Scrollbar(wiN)
sBar.pack(side=tk.RIGHT,fill=tk.Y)
listBox=tk.Listbox(wiN, font=("Arial", 20),yscrollcommand=sBar.set,bg="yellow",width=850)
listBox.pack(side=tk.RIGHT, fill=tk.BOTH)
sBar.config(command=listBox.yview)



wiN.mainloop()