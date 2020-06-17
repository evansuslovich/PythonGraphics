#program to convert Celsius to Fahrenheit using a simple graphical interface 
from graphics import * 
import random
def main(): 
    win = GraphWin("Celsius Converter", 800,600)
    win.setCoords(0.0,0.0, 3.0, 4.0) 
    colorA = random.randint(0,255)
    colorB = random.randint(0,255)
    colorC = random.randint(0,255)
    win.setBackground(color_rgb(colorA,colorB,colorC))
    

    #Draw the interface 
    celsiusTemp = Text(Point(1,3), "  Celsius temperature:")
    celsiusTemp.setSize(18)
    celsiusTemp.setStyle("bold")
    celsiusTemp.draw(win)

    fahrenTemp = Text(Point(1,1), "Fahrenheit Temperature:")
    fahrenTemp.setSize(18)
    fahrenTemp.setStyle("bold")
    fahrenTemp.draw(win)


    input = Entry(Point(2,3), 5)
    input.setText("0.0")
    input.setTextColor("purple")
    input.setStyle("bold")
    input.draw(win)
    
    output = Text(Point(2,1), "")
    output.draw(win)

   

    rect = Rectangle(Point(1,1.5), Point(2,2.5))
    rect.setFill("green")
    rect.draw(win)

    button = Text(Point(1.5,2.0), "Convert It")
    button.setSize(18)
    
    button.setTextColor("blue")
    button.setStyle("bold")
    button.draw(win)

    #wait for a mouseclick 

    win.getMouse()

    #convert input 
    celsius = eval(input.getText())
    fahrenheit = 9.0/5.0 * celsius + 32

    # display output and change button 
    output.setText(fahrenheit)
    output.setStyle("bold")
    
    rect.setFill("red")
    button.setFill("yellow")
    button.setText("Quit")

    # wait for click and then quit 
    win.getMouse()
    win.close()
main()