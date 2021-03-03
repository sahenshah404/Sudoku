from random import randrange,randint,random
import numpy as np
numbers=[1,2,3,4,5,6,7,8,9]


# sudoku=[[0]*9]*9
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




def newsudoku(x,y):
    numbool=[True]*9
    # print(numbool)
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
                return
            else:
                if y<8:
                    y=y+1
                else:
                    if y==8:
                        x=x+1
                        y=0
                
                newsudoku(x,y)
    if 0 in sudoku:
        sudoku[x][y]=0
   
        
newsudoku(x,y)

print(sudoku)

