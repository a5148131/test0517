import random
import tkinter as tk
import tkinter.messagebox
from PIL import Image,ImageTk

def _hit1():
    global update_number
    btN1.config(text="停止", command=_hit11)

    # 創建一個計時器，每隔一段時間更新標籤上的數字
    def update_number():
        global DD
         # 生成一個新的隨機數字
        new_number1 = random.randint(1, 48)
        new_number2 = random.randint(1, 48)
        new_number3 = random.randint(1, 48)
        new_number4 = random.randint(1, 48)
        new_number5 = random.randint(1, 48)
        new_number6 = random.randint(1, 48)
        new_number7 = random.randint(1, 48)
        # 更新標籤上顯示的數字
        lbL1['text'] = str(new_number1)
        lbL2['text'] = str(new_number2)
        lbL3['text'] = str(new_number3)
        lbL4['text'] = str(new_number4)
        lbL5['text'] = str(new_number5)
        lbL6['text'] = str(new_number6)
        lbL7['text'] = str(new_number7)
        
        # 重複呼叫 update_number 函數，每隔一段時間更新數字
        DD=wiN.after(10, update_number)
    # 啟動計時器
    update_number() 
    
def _hit11():
    btN1.config(text="開始", command=_hit1)
    ball=[]
    
    wiN.after_cancel(DD)
    
    # 生成大樂透号码
    ball = random.sample(range(1, 49), 7)
    
    # 更新標籤上的數字
    lbL1['text'] = str(ball[0])
    lbL2['text'] = str(ball[1])
    lbL3['text'] = str(ball[2])
    lbL4['text'] = str(ball[3])
    lbL5['text'] = str(ball[4])
    lbL6['text'] = str(ball[5])
    lbL7['text'] = str(ball[6])
        
def _hit2():
        lbL1["text"]=""
        lbL2["text"]=""
        lbL3["text"]=""
        lbL4["text"]=""
        lbL5["text"]=""
        lbL6["text"]=""
        lbL7["text"]=""
        

def _hit3():
    qQ=tk.messagebox.askokcancel("提示","確定要結束程式嗎???")
    if qQ:
        wiN.destroy()
    

wiN = tk.Tk()
wiN.title("大樂透!!")
wiN.geometry("600x500")

img=Image.open("goldgod.jpg")
img=img.resize((600,400))
img=ImageTk.PhotoImage(img)
imLabel=tk.Label(wiN,image=img)
imLabel.pack()

# 建立畫布
caN = tk.Canvas(wiN, bg="yellow",width=600, height=100)
caN.pack(side="bottom")

# 繪製文字
text = caN.create_text(450,50 , text="財神祝你中大獎!    記得中了來還願~~", font=("標楷體",30), fill="red")

# 向左移動文字
def move_text():
    caN.move(text, -1, 0)
    wiN.after(10, move_text)

# 啟動流動文字
move_text()

btN1 = tk.Button(wiN, text="開始!!",fg="black",bg="gold", font=("標楷體", 16), width=10, height=2, command=_hit1 )
btN1.place(x=230,y=0) 
    
btN2 = tk.Button(wiN, text="結束!!",fg="black",bg="gold", font=("標楷體", 16), width=10, height=2, command=_hit3)
btN2.place(x=230,y=60)

btN3= tk.Button(wiN,text="清除",fg="black",bg="gold",font=("標楷體", 16), width=10, height=2, command=_hit2)
btN3.place(x=230,y=120)



lbL1 = tk.Label(wiN,text="",fg="black",bg="mediumspringgreen", font=("標楷體", 16), width=5, height=1)
lbL1.place(x=20,y=250)
lbL2 = tk.Label(wiN,text="",fg="black",bg="mediumspringgreen", font=("標楷體", 16), width=5, height=1)
lbL2.place(x=120,y=250)
lbL3 = tk.Label(wiN,text="",fg="black",bg="mediumspringgreen", font=("標楷體", 16), width=5, height=1)
lbL3.place(x=220,y=250)
lbL4 = tk.Label(wiN,text="",fg="black",bg="mediumspringgreen", font=("標楷體", 16), width=5, height=1)
lbL4.place(x=320,y=250)
lbL5 = tk.Label(wiN,text="",fg="black",bg="mediumspringgreen", font=("標楷體", 16), width=5, height=1)
lbL5.place(x=420,y=250)
lbL6 = tk.Label(wiN,text="",fg="black",bg="mediumspringgreen", font=("標楷體", 16), width=5, height=1)
lbL6.place(x=520,y=250)

lbL7 = tk.Label(wiN,text="",fg="black",bg="yellow", font=("Arial", 16), width=5, height=1)
lbL7.place(x=250,y=350)


lbL11 = tk.Label(wiN,text="第一號",fg="white",bg="seagreen", font=("標楷體", 16), width=5, height=1)
lbL11.place(x=20,y=200)
lbL21 = tk.Label(wiN,text="第二號",fg="white",bg="seagreen", font=("標楷體", 16), width=5, height=1)
lbL21.place(x=120,y=200)
lbL31 = tk.Label(wiN,text="第三號",fg="white",bg="seagreen", font=("標楷體", 16), width=5, height=1)
lbL31.place(x=220,y=200)
lbL41 = tk.Label(wiN,text="第四號",fg="white",bg="seagreen", font=("標楷體", 16), width=5, height=1)
lbL41.place(x=320,y=200)
lbL51 = tk.Label(wiN,text="第五號",fg="white",bg="seagreen", font=("標楷體", 16), width=5, height=1)
lbL51.place(x=420,y=200)
lbL61 = tk.Label(wiN,text="第六號",fg="white",bg="seagreen", font=("標楷體", 16), width=5, height=1)
lbL61.place(x=520,y=200)

lbL71 = tk.Label(wiN,text="特別號",fg="white",bg="seagreen", font=("標楷體", 16), width=5, height=1)
lbL71.place(x=250,y=300)

      
    


wiN.resizable(width=False, height=False)
wiN.mainloop()