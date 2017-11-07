# This is a Python program that uses two ui modules, the turtle and Tkinter modules.
# When a module is used in Python you need to import it into your program.
import turtle
import Tkinter
import csv
import math


# Dimension variables
eye_he = []
eye_ve = []

# Import csv file containing horizontal and vertical eye positions as columns
with open('eye_coords.csv') as eye_coords_file:
    reader = csv.reader(eye_coords_file, delimiter = ',')
    for row in reader:
        eye_he.append(float(row[0]))
        eye_ve.append(float(row[1]))


# Next, the main function is defined. Defining a function doesn't do anything other 
# than tell Python the name of the function. Next the program jumps all the way down 
# to the "if" statement at the bottom of the file.
def main():
   
   # Here is the first line of the main function's code. 
   root = Tkinter.Tk()
   root.title("Eye Trace Animator")
   cv = Tkinter.Canvas(root,width=1024,height=768)
   cv.pack(side = Tkinter.RIGHT)
   
   # This is how we create a turtle to draw on the canvas we created above.
   eye = turtle.RawTurtle(cv)
   screen = eye.getscreen()
   
   # With the lines below, the "turtle" will look like a pencil.
##   screen.register_shape("pencil.gif")
##   t.shape("pencil.gif")

   # This sets the lower left corner to 0,0 and the upper right corner to 600,600. 
 #  screen.setworldcoordinates(0,0,1024,768)
   global turtle_running
   turtle_running = True
   eye.speed(10)
   eye.screen.bgcolor('black')
   eye.pencolor('white')
   eye.shape('circle')
   eye.pen(fillcolor='white')
   eye.shapesize(stretch_wid = .6, stretch_len = .6, outline = 0)
   eye.pensize(5)

   # A frame is an invisible widget that holds other widgets. This frame goes 
   # on the right hand side of the window and holds the buttons and Entry widgets.
   frame = Tkinter.Frame(root)
   frame.pack(side = Tkinter.LEFT,fill=Tkinter.BOTH)

   pointLabel = Tkinter.Label(frame,text="Width")
   pointLabel.pack()
   
   # This entry widget allows the user to pick a width for their lines. 
   # With the pointSize variable below you can write pointSize.get() to to 
   # the contents of the entry widget and pointSize.set(val) to set the value
   # of the entry widget to val. Initially the pointSize is set to 1. str(1) is needed because
   # the entry widget must be given a string.
   pointSize = Tkinter.StringVar()
   pointEntry = Tkinter.Entry(frame,textvariable=pointSize)
   pointEntry.pack()
   pointSize.set(str(1))
   
   TrialLabel = Tkinter.Label(frame,text="Trial Number")
   TrialLabel.pack()
   
   TrialNumber = Tkinter.StringVar()
   TrialEntry = Tkinter.Entry(frame,textvariable=TrialNumber)
   TrialEntry.pack()
   TrialNumber.set(str(1))
   
   # This is an event handler. Handling the quit button press results in destroying the window
   # and quitting the application. 
   def quitHandler():
      root.destroy()
      root.quit()
   def paint_boxes():
        eye.penup()
        eye.setposition(-75,75)
        eye.pendown()
        for i in range(4):
            eye.forward(150)
            eye.right(90)
        eye.penup()

        eye.setposition(-275,350)
        eye.pendown()
        for i in range(4):
            eye.forward(200)
            eye.right(90)
        eye.penup()

        eye.setposition(75,350)
        eye.pendown()
        for i in range(4):
            eye.forward(200)
            eye.right(90)
        eye.penup()

        eye.setposition(-275,-150)
        eye.pendown()
        for i in range(4):
            eye.forward(200)
            eye.right(90)
        eye.penup()

        eye.setposition(75,-150)
        eye.pendown()
        for i in range(4):
            eye.forward(200)
            eye.right(90)
        eye.penup()

        eye.setposition(0,0)
        eye.pendown()
        
   def paint_eyetrace(TrialNumber):
      tn = TrialNumber.get()
      for (he,ve) in zip(eye_he,eye_ve):
         if turtle_running:
            if math.sqrt((ve*ve)+(he*he)) < 50:
               if math.sqrt((ve*ve)+(he*he)) < 9:
                  eye.pencolor('green')
               else:
                  eye.pencolor('red')
               eye.setposition(he*10,ve*10)

   def clear_turtle():
      eye.clear()
      eye.setposition(0,0)

   def reset_turtle():
      eye.reset()
      eye.speed(10)
      eye.screen.bgcolor('black')
      eye.pencolor('white')
      eye.shape('circle')
      eye.pen(fillcolor='white')
      eye.shapesize(stretch_wid = .6, stretch_len = .6, outline = 0)
      eye.pensize(5)

   def stop_turtle():
      global turtle_running
      turtle_running ^= True

      
   # This is how a button is created in the frame. The quitHandler is the event handler for button
   # presses of the "Quit" button.
   do_eyes_button = Tkinter.Button(frame, text="Commence Eye Trace", command= lambda:paint_eyetrace(TrialNumber))
   do_eyes_button.pack(fill = 'x')
   do_boxes_button = Tkinter.Button(frame, text="Paint Boxes", command=paint_boxes)
   do_boxes_button.pack(fill = 'x')
   stop_turtle_button = Tkinter.Button(frame, text = "Stop Animator", command=stop_turtle)
   stop_turtle_button.pack(fill = 'x')   
   eye_clear_button = Tkinter.Button(frame, text = "Clear Drawing", command=clear_turtle)
   eye_clear_button.pack(fill = 'x')
   eye_reset_button = Tkinter.Button(frame, text = "Reset Animator", command=reset_turtle)
   eye_reset_button.pack(fill = 'x')      
   quitButton = Tkinter.Button(frame, text = "Quit", command=quitHandler)
   quitButton.pack(fill = 'x')
   
   # Here is another event handler. This one handles mouse clicks on the screen.
   def clickHandler(x,y): 
      # When a mouse click occurs, get the pointSize entry value and set the width of the 
      # turtle called "t" to the pointSize value. The int(pointSize.get()) is needed because
      # the width is an integer, but the entry widget stores it as a string.
      eye.width(int(pointSize.get()))
      eye.goto(x,y)
      
   # Here is how we tie the clickHandler to mouse clicks.
   eye.screen.onclick(clickHandler)
   
   # Finally, this code is last. It tells the application to enter its event processing loop
   # so the application will respond to events. 
   Tkinter.mainloop()
   
# Python jumps right here after executing the def main() line. These two lines tell 
# Python to jump to the first line of the main function above. Seems a little strange,
# but there are good reasons for this which you'll learn if you take some computer 
# science.
if __name__ == "__main__":
   main()
