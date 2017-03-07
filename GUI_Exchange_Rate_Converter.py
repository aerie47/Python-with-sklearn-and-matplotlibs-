
print"\nSTSCI 4060 HW4 Name: Hongxiang Zhao\n"
print"\n*****Question1*****\n"

from graphics import *

def main():
    # define the coordinate of window
    win = GraphWin('Currency Converter',300,500)
    # set the coordinates
    win.setCoords( 0.0, 0.0, 400.0, 600.0)
    
    # draw the interface 
    Text(Point(150,500),'Exchange rate:').draw(win)
    Text(Point(150,480),'(USD to RMB)').draw(win)
    Text(Point(150,430),'US Dollar:').draw(win)
    Text(Point(150,380),'RMB:').draw(win)
    
    
    # set the entry object
    # set the default of rate as 6.5
    input_rate = Entry(Point(280,500),9)
    input_rate.setText('6.5')
    input_rate.draw(win)
    
    input_dollar = Entry(Point(280,430),9)
    input_dollar.setText('0.0')
    input_dollar.draw(win)
    
    input_rmb = Entry(Point(280,380),9)
    input_rmb.setText('0.0')
    input_rmb.draw(win)
    
    # draw the button rectangle 
    button1 = Text(Point(200,300), 'Convert\n(Clear First)')
    button1.draw(win)
    
    b_rec1=Rectangle(Point(130,330), Point(270,270))
    b_rec1.draw(win)
    
    button2 = Text(Point(200,210), 'Clear')
    button2.draw(win)
    b_rec2=Rectangle(Point(130,240), Point(270,180))
    b_rec2.draw(win)
    
    button3 = Text(Point(200,120), 'Quit')
    button3.draw(win)
    b_rec3=Rectangle(Point(130,150), Point(270,90))
    b_rec3.draw(win)

   

# define a function that can help me check if the mouse is clicked within the button 
    def button(point, button):
        x = point.getX()
        y = point.getY()
        p1 = button.getP1()
        p2 = button.getP2()
        x_range = [p1.getX(),p2.getX()]
        y_range = [p1.getY(), p2.getY()]
        return ((x >= x_range[0] and x <= x_range[1]) and (y >= y_range[1] and y <= y_range[0]))
    
    
    

# wait for a mouse click 
    point = win.getMouse()

    
# loop through the statements until the 'quit' button is clicked    
    
    while button(point, b_rec3) != True:
# situation that the "convert" button is clicked        
        if button(point, b_rec1) == True:
            rate = eval(input_rate.getText())
            dollar = eval(input_dollar.getText())
            rmb = eval(input_rmb.getText())
# if RMB is not typed
            if rmb ==0.0:#input_rmb.getText() == '0.0' :
                #rate = eval(input_rate.getText())
                #dollar = eval(input_dollar.getText())
    
                
                currency2 = float(rate) * dollar
                input_rmb.setText('%0.1f' %currency2)
            
    
 # if Dollar is not typed      
            elif dollar == 0.0:#input_dollar.getText() == '0.0':
                #rate = eval(input_rate.getText())
                #rmb = eval(input_rmb.getText())
        
                
                currency2 = float(1/rate) * rmb
                input_dollar.setText('%0.1f' %currency2)
         
# if both and dollar are typed, do nothing             
            else :
               pass
# situation that 'clear' button is clicked            
        elif button(point, b_rec2) == True:
            input_rate.setText('6.5')
            input_dollar.setText('0.0')
            input_rmb.setText('0.0')
            
        else:
            pass
# store the new mouse click action        
        point = win.getMouse()
    
    # quit when 'quit' is clicked    
    win.close()
# call the GUI function        
main()



