import turtle
import csv
import math
from Tkinter import *



eye_he = []
eye_ve = []



with open('eye_coords.csv') as eye_coords_file:
    reader = csv.reader(eye_coords_file, delimiter = ',')
    for row in reader:
        eye_he.append(float(row[0]))
        #print(float(row[0]))
        eye_ve.append(float(row[1]))


#np.asarray(eye_he)
#np.asarray(eye_ve)
#eye_coords = dict(zip(eye_he,eye_ve))
#eye_coords = np.matrix(np.asarray(eye_he),np.asarray(eye_ve))
#print(eye_coords)

eye = turtle.Turtle()
eye.speed(10)
eye.screen.bgcolor('black')
eye.pencolor('white')
eye.shape('circle')
eye.pen(fillcolor='white')
eye.shapesize(stretch_wid = .6, stretch_len = .6, outline = 0)
eye.pensize(5)

class Input_Frame(Frame):
    def __init__(self, parent, frame):
        self.frame = frame
        self.do_boxes = Button(self.frame,
                                          text="remove",
                                          width=10,
                                          command=Turtles.paint_boxes)
        self.do_boxes.pack()
        
class Turtles:
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
        
    def paint_eyetrace():
        for (he,ve) in zip(eye_he,eye_ve):
        ##    eye.penup()
        ##    eye.setposition(-500,-500)
        ##    eye.pendown()
        ##    eye.write('((%s),(%s))' %(he, ve), font=("Arial", 16, "normal"))
        ##    eye.penup()
            if math.sqrt((ve*ve)+(he*he)) < 50:
                if math.sqrt((ve*ve)+(he*he)) < 9:
                    eye.pencolor('green')
                else:
                    eye.pencolor('red')

                eye.setposition(he*10,ve*10)
            
        turtle.done()

def main():

    root = Tk()

    root.title('EyeTrace Console')
    root.resizable(True, True)
    root.configure(background = 'grey')
    sizex = 700
    sizey = 600
    posx  = 0
    posy  = 0
    root.geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
    main_frame = Frame(root).pack()
    input_panel = Input_Frame(root, main_frame)
##    style_main = Style()
##    style_main.theme_use("default")
##    style_main.configure("main.TButton",
##                         foreground="black",)
##
##    s = ttk.Style()
##    s.theme_use("default")


    root.mainloop()

if __name__ == "__main__": main()
