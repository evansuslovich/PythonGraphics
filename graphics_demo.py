from graphics import *

def main(): 
    win = GraphWin("f*CK yU0", 1000,1000)
    win.setBackground(color_rgb(242,242,242))
   
    pt1 = Point(100,100)
    cir = Circle(pt1,75)
    cir.setFill(color_rgb(100,255,50))
    cir.draw(win)

    pt2 = Point(250,250)
    circ2 = Circle(pt2, 75)
    circ2.setFill(color_rgb(227,171,255))
    circ2.draw(win)

    pt3 = Point(450,200)
    circ3 = Circle(pt3,75)
    circ3.setFill(color_rgb(199,255,171))
    circ3.draw(win)

    pt4 = Point(900,300)
    circ4 = Circle(pt4, 75)
    circ4.setFill(color_rgb(148,169,255))
    circ4.draw(win)

    pt5 = Point(500,500)
    label1 = Text(pt5,"f*CK yU0")    
    label1.draw(win)
    
    pt6 = Point(500,490)
    label2 = Text(pt6,"f*CK yU0")    
    label2.draw(win)
    
    pt7 = Point(500,510)
    label3 = Text(pt7,"f*CK yU0")    
    label3.draw(win)
    

    pt8 = Point(250,400)
    label1 = Text(pt8,"f*CK yU0")    
    label1.draw(win)
    
    pt9 = Point(300,350)
    label2 = Text(pt9,"f*CK yU0")    
    label2.draw(win)
    
    pt10 = Point(350,300)
    label3 = Text(pt10,"f*CK yU0")  
    label3.draw(win)

    line = Line(Point(0,0),Point(800,800))
    line.draw(win)

    oval = Oval(Point(900,900),Point(950,950))
    oval.setFill(color_rgb(92,92,214))
    oval.draw(win)


    win.getMouse()
    win.close()

main()