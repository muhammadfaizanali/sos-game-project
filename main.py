from tkinter import Tk,Button
class Main(Tk):
    def __init__(self,title,geometry,bg) -> None:
        super().__init__()
        self.title(title)
        self.geometry(f"{geometry[0]}x{geometry[1]}")
        self.configure(background=bg)
        self.resizable(False,False)
        self.l=2
        self.btnlist=''
        # self.btn=[]
        self.drawbtn()
        self.mainloop()
    def event(self,btns):
        if(btns['text']==''):
            if(self.l%2==0):
                btns['text']='S'
                self.l+=1    
            else:
                btns['text']='O'
                self.l+=1
        # Logic class call
        objlogic=Logic(self.btnlist)
    def drawbtn(self):
        # btm row no 1
        btn1=Button(text='',bg='white',fg='black',font=('Arial',15),width='10',height='5')
        btn1.place(x=140*0,y=135*0)
        btn1.configure(command=lambda:self.event(btn1))
        btn2=Button(text='',bg='white',fg='black',font=('Arial',15),width='10',height='5')
        btn2.place(x=140*1,y=135*0)
        btn2.configure(command=lambda:self.event(btn2))
        btn3=Button(text='',bg='white',fg='black',font=('Arial',15),width='10',height='5')
        btn3.place(x=140*2,y=135*0)
        btn3.configure(command=lambda:self.event(btn3))
        # btm row no 2
        btn4=Button(text='',bg='white',fg='black',font=('Arial',15),width='10',height='5')
        btn4.place(x=140*0,y=135*1)
        btn4.configure(command=lambda:self.event(btn4))
        btn5=Button(text='',bg='white',fg='black',font=('Arial',15),width='10',height='5')
        btn5.place(x=140*1,y=135*1)
        btn5.configure(command=lambda:self.event(btn5))
        btn6=Button(text='',bg='white',fg='black',font=('Arial',15),width='10',height='5')
        btn6.place(x=140*2,y=135*1)
        btn6.configure(command=lambda:self.event(btn6))
        # btm row no 3
        btn7=Button(text='',bg='white',fg='black',font=('Arial',15),width='10',height='5')
        btn7.place(x=140*0,y=135*2)
        btn7.configure(command=lambda:self.event(btn7))
        btn8=Button(text='',bg='white',fg='black',font=('Arial',15),width='10',height='5')
        btn8.place(x=140*1,y=135*2)
        btn8.configure(command=lambda:self.event(btn8))
        btn9=Button(text='',bg='white',fg='black',font=('Arial',15),width='10',height='5')
        btn9.place(x=140*2,y=135*2)
        btn9.configure(command=lambda:self.event(btn9))
        # create list of btns objts
        self.btnlist=[btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9]
class Logic:
    def __init__(self,btns) -> None:
        self.btnlist=btns
        self.winone=''
        self.wintwo=''
        self.gamelogic()
    def gamelogic(self):
        # rows conditions
        if(self.btnlist[0]['text']=='S' and self.btnlist[1]['text']=='O' and self.btnlist[2]['text']=='S'):
            if(self.winone==''):
                self.winone='Player One Winer'
                print(self.winone)
        elif(self.btnlist[3]['text']=='S' and self.btnlist[4]['text']=='O' and self.btnlist[5]['text']=='S'):
            if(self.winone==''):
                self.winone='Player One Winer'
                print(self.winone)
        elif(self.btnlist[6]['text']=='S' and self.btnlist[7]['text']=='O' and self.btnlist[8]['text']=='S'):
            if(self.winone==''):
                self.winone='Player One Winer'
                print(self.winone)
        # columns conoditions    
        elif(self.btnlist[0]['text']=='S' and self.btnlist[3]['text']=='O' and self.btnlist[6]['text']=='S'):
            if(self.winone==''):
                self.winone='Player One Winer'
                print(self.winone)
        elif(self.btnlist[1]['text']=='S' and self.btnlist[4]['text']=='O' and self.btnlist[7]['text']=='S'):
            if(self.winone==''):
                self.winone='Player One Winer'
                print(self.winone)
        elif(self.btnlist[2]['text']=='S' and self.btnlist[5]['text']=='O' and self.btnlist[8]['text']=='S'):
            if(self.winone==''):
                self.winone='Player One Winer'
                print(self.winone)
        # Daignal conoditions    
        elif(self.btnlist[0]['text']=='S' and self.btnlist[4]['text']=='O' and self.btnlist[8]['text']=='S'):
            if(self.winone==''):
                self.winone='Player One Winer'
                print(self.winone)
        elif(self.btnlist[2]['text']=='S' and self.btnlist[4]['text']=='O' and self.btnlist[6]['text']=='S'):
            if(self.winone==''):
                self.winone='Player One Winer'
                print(self.winone)
        else:
            if(self.btnlist[0]['text']!='' and self.btnlist[1]['text']!='' and self.btnlist[2]['text']!='' and self.btnlist[3]['text']!='' and self.btnlist[4]['text']!='' and self.btnlist[5]['text']!='' and self.btnlist[6]['text']!='' and self.btnlist[7]['text']!='' and self.btnlist[8]['text']!=''):
                self.wintwo='Player Two Winer'
                print(self.wintwo)
if __name__=="__main__":
    objmain=Main(title='SOS Game',geometry=(420,405),bg='grey')    