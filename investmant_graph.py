from graphics import * 

def main():
    #introduction 
    print("This program plots the growth of a 10-year investment.")

    #Get prinicipal and interest rate 

    principal = input("Enter the intiial principal: ")
    apr = input("Enter the annualied interest rate")

    #Crete a graphics window with labels on left edge 

    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")

    Text(Point(20,230), "0.0k").draw(win)
    Text(Point(20,180), "2.5k").draw(win)
    Text(Point(20,130), "5.0k").draw(win)
    Text(Point(20,80), "7.5k").draw(win)
    Text(Point(20,30), "10.0k").draw(win)
    


    
    

    #Draw bar for initial principal 

    height = principal*0.02
    bar = Rectangle(Point(40,230), Point(65,230-height))
    bar.setFill("Green")
    bar.setWidth(1)
    bar.draw(win)

    #Draw bars for succesive years
    for year in range(1,11):
        # calculate value for the next year 
        principal = principal*(1+apr)
        #draw bar for this value 
        x11 = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(x11,230), Point(x11 + 25, 230 - height))
        bar.setFill("green")
        bar.setWidth(1)
        bar.draw(win)
    
    input("PRESS <ENTER> TO QUIT")
    win.close()

main()

   