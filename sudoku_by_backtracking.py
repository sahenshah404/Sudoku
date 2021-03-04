from random import randrange,randint,random
import numpy as np
numbers=[1,2,3,4,5,6,7,8,9]



sudoku= np.zeros((9,9))
sudoku2= np.zeros((9,9))
qsudoku= np.zeros((9,9))
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
           
    
print(" do you want to enter a sudoku puzzle and get its solution\t press 1\n")
print(" or you want to get a sudoku puzzle and solve it \t Press 2")
type=int(input())
if(type==1):
    for i in range(9):
        for j in range(9):
            sudoku[i][j]=int(input())

    newsudoku(x,y,type)
    print(sudoku2)

if(type==2):
    newsudoku(x,y,type)
    print("Do you want a easy question or hard question")
    print("Press 1 for easy question  Press 2 for hard question")
    if(input()==1):
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


    print(qsudoku)

    print()
    print("if you are unable to solve it")
    print("do you want the program itslef to solve this question  press 1")
    print("Or you want to solve it yourself and match the output then wait when completed press 2")
    input()
    for i in range(9):
            for j in range(9):
                sudoku[i][j]=qsudoku[i][j]
    newsudoku(x,y,1)
    print(sudoku)
