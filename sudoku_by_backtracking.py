from random import randrange,randint,random
import numpy as np
from tkinter import *
numbers=[1,2,3,4,5,6,7,8,9]



sudoku= np.zeros((9,9))
sudoku2= np.zeros((9,9))
qsudoku= np.zeros((9,9))
arr=np.zeros((9,9))
count=np.zeros(1)

x=0
y=0


def startlimit(x):
    if(x>=0 and x<=2):
        return 0
    if(x>=3 and x<=5):
        return 3
    if(x>=6 and x<=8):
        return 6

def endlimit(x):
    if(x>=0 and x<=2):
        return 2
    if(x>=3 and x<=5):
        return 5
    if(x>=6 and x<=8):
        return 8

def inputgui():
    tk=Tk()
    tk.geometry("400x400")
    z=0
    a=["0"]*81
    j=0
    i=0
    def sol():
        k=0
        for i in range(9):
            for j in range(9):
                arr[i][j]=a[k].get()            
                k=k+1
        tk.destroy()


    for i in range(81):
        a[i]=IntVar()
    
    y=0
    b=IntVar()
    for i in range(9):
        for j in range(9):
            x=Entry(tk,textvariable=a[y],width=5).grid(row=i,column=j,padx=4,ipady=5)
            y=y+1
            
    Label(tk,text="Enter").grid(row=85)
    Label(tk,text="your").grid(row=86)
    Label(tk,text="sudoku").grid(row=87)
    Button(tk,text="Show Sol",command=sol,width=7).grid(row=86,column=5)

    print()
    tk.mainloop()
    for i in range(9):
        for j in range(9):
            sudoku[i][j]=arr[i][j]




def newsudoku(x,y,type):
    numbool=[True]*9

    if sudoku[x][y]==0:
    
        while True in numbool:
            num=randrange(0,9)
            if num+1 in sudoku[x]:
                numbool[num]=False
            if num+1 in sudoku.T[y]:
                numbool[num]=False
            
            xstart=startlimit(x)
            ystart=startlimit(y)

            xend=endlimit(x)
            yend=endlimit(y)

            for i in range(xstart,xend+1):
                for j in range(ystart,yend+1):
                    if num+1 == sudoku[i][j]:
                        numbool[num]=False   


            if(numbool[num]==True):
                numbool[num]=False
                sudoku[x][y]=num+1

                if y==8 and x==8:
                    if(type==1 or type==2):
                        for i in range(9):
                            for j in range(9):
                                sudoku2[i][j]=sudoku[i][j]
                    else:
                        count[0]=count[0]+1
                    
                    
                else:
                    if y<8:
                        newsudoku(x,y+1,type)
                    else:
                        if y==8:
                            newsudoku(x+1,0,type)
                   
        if type==1 or type==2:   
            if 0 in sudoku:
                sudoku[x][y]=0
                return
        else:
            sudoku[x][y]=0


    else:
        if y==8 and x==8:
            if(type==1 or type==2):
                for i in range(9):
                    for j in range(9):
                        sudoku2[i][j]=sudoku[i][j]
            else:
                count[0]=count[0]+1
            return
        else:
            if y<8:
                newsudoku(x,y+1,type)
            else:
                if y==8:
                    newsudoku(x+1,0,type)
           

def outputgui():
    tk=Tk()
    var=IntVar()
    for i in range(9):
        for j in range(9):
            x=Label(tk,text=int(sudoku2[i][j]),width=5).grid(row=i,column=j,padx=4,ipady=5)


    tk.mainloop()

def questiongui():
    tk=Tk()
    var=IntVar()
    for i in range(9):
        for j in range(9):
            x=Label(tk,text=int(qsudoku[i][j]),width=5).grid(row=i,column=j,padx=4,ipady=5)


    tk.mainloop()

def solutiongui():
    tk=Tk()
    var=IntVar()
    for i in range(9):
        for j in range(9):
            x=Label(tk,text=int(sudoku[i][j]),width=5).grid(row=i,column=j,padx=4,ipady=5)


    tk.mainloop()



print(" do you want to enter a sudoku puzzle and get its solution\t press 1\n")
print(" or you want to get a sudoku puzzle and solve it \t Press 2")
type=int(input())
if(type==1):
    print("do you wanna give input in GUI press 1")
    print("do you wanna give input in CLI press 2")
    if(input()=='2'):
        for i in range(9):
            for j in range(9):
                sudoku[i][j]=int(input())
    else:
        inputgui() 

    x,y=0,0
    newsudoku(x,y,type)
    # print(sudoku2)
    outputgui()

if(type==2):
    newsudoku(x,y,type)
    print("Do you want a easy question or hard question")
    print("Press 1 for easy question  Press 2 for hard question")
    if(input()=='1'):
        hard=False
    else:
        hard=True
    
    
    while(1):
        count[0]=0

        randposx=randrange(1,9)
        randposy=randrange(1,9)
        if hard:
            sudoku2[randposx][randposy]=0
            sudoku2[randposy][randposx]=0
        else:
            sudoku2[randposx][randposy]=0
        
        for i in range(9):
            for j in range(9):
                sudoku[i][j]=sudoku2[i][j]
        
        newsudoku(x,y,3)
        if (int(count[0])==1):
            for i in range(9):
                for j in range(9):
                    qsudoku[i][j]=sudoku2[i][j]
        else:
            break


    # print(qsudoku)
    questiongui()

    print()
    print("if you are unable to solve it")
    print("do you want the program itslef to solve this question  press 1")
    print("Or you want to solve it yourself and match the output then wait when completed press 2")
    input()
    for i in range(9):
            for j in range(9):
                sudoku[i][j]=qsudoku[i][j]
    newsudoku(x,y,1)
    # print(sudoku)
    solutiongui()