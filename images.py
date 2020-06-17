from graphics import * 

def main(): 
    win = GraphWin("My Window", 800,800)
    win.setBackground(color_rgb(0,0,0))

    img = Image(Point(250,250), "apple.gif")
    img.draw(win)

    win.getMouse()
    win.close()

main()