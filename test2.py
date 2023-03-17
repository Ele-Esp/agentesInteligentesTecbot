#magic triangle
#sums
leftDiagonal=0
rightDiagonal=0
bottomRow=0
#nodes
top=0
leftMiddle=0
rightMiddle=0
bottomLeft=0
bottomRight=0
bottomMiddle=0

def changeTop(value):
    global leftDiagonal, rightDiagonal, bottomRow, top, leftMiddle, rightMiddle, bottomLeft, bottomRight, bottomMiddle
    leftDiagonal=leftMiddle+bottomLeft+value
    rightDiagonal=rightMiddle+bottomRight+value
    top=value

def changeLeftMiddle(value):
    global leftDiagonal, rightDiagonal, bottomRow, top, leftMiddle, rightMiddle, bottomLeft, bottomRight, bottomMiddle
    leftDiagonal=top+bottomLeft+value
    leftMiddle=value

def changeRightMiddle(value):
    global leftDiagonal, rightDiagonal, bottomRow, top, leftMiddle, rightMiddle, bottomLeft, bottomRight, bottomMiddle
    rightDiagonal=top+bottomRight+value
    rightMiddle=value

def changeBottomLeft(value):
    global leftDiagonal, rightDiagonal, bottomRow, top, leftMiddle, rightMiddle, bottomLeft, bottomRight, bottomMiddle
    leftDiagonal=top+leftMiddle+value
    bottomRow= bottomMiddle+bottomRight+value
    bottomLeft=value

def changeBottomRight(value):
    global leftDiagonal, rightDiagonal, bottomRow, top, leftMiddle, rightMiddle, bottomLeft, bottomRight, bottomMiddle
    rightDiagonal=top+rightMiddle+value
    bottomRow= bottomMiddle+bottomLeft+value
    bottomRight=value

def changeBottomMiddle(value):
    global leftDiagonal, rightDiagonal, bottomRow, top, leftMiddle, rightMiddle, bottomLeft, bottomRight, bottomMiddle
    bottomRow= bottomLeft+bottomRight+value
    bottomMiddle=value

#using only numbers from 1 to 6, fill the triangle so that the sums of the numbers in each row, column, and diagonal are all 10
def printTriangle():
    print("   ",top)
    print(" ",leftMiddle," ", rightMiddle)
    print(bottomLeft," ",bottomMiddle," ",bottomRight)
    print("--------------------")

#top
for top in range(1,7):
    #left middle
    for leftMiddle in range(1,7):
        #right middle
        for rightMiddle in range(1,7):
            #bottom left
            for bottomLeft in range(1,7):
                #bottom right
                for bottomRight in range(1,7):
                    #bottom middle
                    for bottomMiddle in range(1,7):
                        changeTop(top)
                        changeLeftMiddle(leftMiddle)
                        changeRightMiddle(rightMiddle)
                        changeBottomLeft(bottomLeft)
                        changeBottomRight(bottomRight)
                        changeBottomMiddle(bottomMiddle)
                        if leftDiagonal==10 and rightDiagonal==10 and bottomRow==10:
                            printTriangle()