from graphics import * 
def main(color): 
    win = GraphWin("Draw a Polygon",800,800)
    win.setCoords(0.0,0.0,10.0,10.0)
    message = Text(Point(5,0.5), "Click on Five points")
    message.draw(win)
    
    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    
    p2 = win.getMouse()
    p2.draw(win)

    p3 = win.getMouse()
    p3.draw(win)

    p4 = win.getMouse()
    p4.draw(win)

    p5 = win.getMouse()
    p5.draw(win)

    
    # Use Polygon object to draw the triangle 
    triangle = Polygon(p1,p2,p3,p4,p5)
    triangle.setFill(color)
    triangle.setOutline(color)
    triangle.draw(win)

    # Wait for another click to exit 
    message.setText("Click anywhere to quit.")
    win.getMouse()

main("green")
main("blue")
main(color_rgb(0,123,32))