from random import randrange,randint,random
import numpy as np
numbers=[1,2,3,4,5,6,7,8,9]



sudoku= np.zeros((9,9))

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
                    print(sudoku)
                    
                else:
                    if y<8:
                        newsudoku(x,y+1,type)
                    else:
                        if y==8:
                            newsudoku(x+1,0,type)
                   
        if type:   
            if 0 in sudoku:
                sudoku[x][y]=0
        else:
            sudoku[x][y]=0


    else:
        if y==8 and x==8:
            print(sudoku)
            return
        else:
            if y<8:
                newsudoku(x,y+1,type)
            else:
                if y==8:
                    newsudoku(x+1,0,type)
           
    
print(" do you want to enter a sudoku puzzle and get its solution\t press 1\n")
print(" or you want to get a sudoku puzzle and solve it \t Press 2")
if(int(input())==1):
    type=False
else:
    type=True
if not type:
    for i in range(9):
        for j in range(9):
            sudoku[i][j]=int(input())
sudoku2=sudoku.copy()
newsudoku(x,y,type)
print(sudoku2)



