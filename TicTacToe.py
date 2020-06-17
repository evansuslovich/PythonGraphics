from graphics import *  
# create a default 200x200 window 
def main():
    win = GraphWin("Tic-Tac-Toe",400,400)
    win.setBackground("white")

    #set coordinates to go from (0,0) in the lower left 
    # to (3,3) in the upper right 
    win.setCoords(0.0,0.0,3.0,3.0)

    #DRAW vertical lines 
    Line(Point(1,0),Point(1,3)).draw(win)
    Line(Point(2,0),Point(2,3)).draw(win)

    #DRAW horizontal lines 
    Line(Point(0,1),Point(3,1)).draw(win)
    Line(Point(0,2),Point(3,2)).draw(win)

    #input numbers into each grid 
    Text(Point(0.5,2.5), "Position 1").draw(win)
    Text(Point(1.5,2.5), "Position 2").draw(win)
    Text(Point(2.5,2.5), "Position 3").draw(win)
    Text(Point(0.5,1.5), "Position 4").draw(win)
    Text(Point(1.5,1.5), "Position 5").draw(win)
    Text(Point(2.5,1.5), "Position 6").draw(win)
    Text(Point(0.5,0.5), "Position 7").draw(win)
    Text(Point(1.5,0.5), "Position 8").draw(win)
    Text(Point(2.5,0.5), "Position 9").draw(win)
    
    position = input("Input a Position integer")

    if(position == 1):
        Line(Point(0.25,2.25),Point(0.75,2.75)).draw(win)
        Line(Point(0.25,2.75),Point(0.75,2.25)).draw(win)

    if(position == 2):
        Line(Point(1.25,2.25),Point(1.75,2.75)).draw(win)
        Line(Point(1.25,2.75),Point(1.75,2.25)).draw(win)


    if(position == 3):
        Line(Point(2.25,2.25),Point(2.75,2.75)).draw(win)
        Line(Point(2.75,2.25),Point(2.25,2.75)).draw(win)

    if(position == 4):
        Line(Point(0.25,1.25),Point(0.75,1.75)).draw(win)
        Line(Point(0.75,1.25),Point(0.25,1.75)).draw(win)

    if(position == 5):
        Line(Point(1.25,1.25),Point(1.75,1.75)).draw(win)
        Line(Point(1.75,1.25),Point(1.25,1.75)).draw(win)

    if(position == 6):
        Line(Point(2.25,1.25),Point(2.75,1.75)).draw(win)
        Line(Point(2.75,1.25),Point(2.25,1.75)).draw(win)

    if(position == 7):
        Line(Point(0.25,0.25),Point(0.75,0.75)).draw(win)
        Line(Point(0.75,0.25),Point(0.25,0.75)).draw(win)

    if(position == 8):
        Line(Point(1.25,0.25),Point(1.75,0.75)).draw(win)
        Line(Point(1.75,0.25),Point(1.25,0.75)).draw(win)

    if(position == 9):
        Line(Point(2.25,0.25),Point(2.75,0.75)).draw(win)
        Line(Point(2.75,0.25),Point(2.25,0.75)).draw(win)



    input("Press <Enter> to Quit")
    win.close()


    
    

main()

