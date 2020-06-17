from graphics import * 

def main():
    #introduction 
    print("This program plots the growth of a 10-year investment.")

    #Get prinicipal and interest rate 
    principal = input("Enter the intiial principal: ")
    apr = input("Enter the annualied interest rate")
   
    #Create  a graphics window with labels on left edge 
    win = GraphWin("Investment Growth Chart", 750, 600)
    win.setBackground("white")
    win.setCoords(-1.75,-200,11.5,10400)
    Text(Point(-1,0), "0.0k").draw(win)
    Text(Point(-1,2500), "2.5k").draw(win)
    Text(Point(-1,5000), "5.0k").draw(win)
    Text(Point(-1,7500), "7.5k").draw(win)
    Text(Point(-1,10000), "10.0k").draw(win)

    #Draw bar for initial principal 
    bar = Rectangle(Point(0,0), Point(1,principal))
    bar.setFill("blue")
    bar.setWidth(2)
    bar.draw(win)

    #Draw bars for succesive years
    for year in range(1,11):
        principal = principal*(1+apr)
        bar = Rectangle(Point(year,0), Point(year+1,principal))
        bar.setFill("blue")
        bar.setWidth(2)
        bar.draw(win)
    
    input("PRESS <ENTER> TO QUIT")
    win.close()

main()

