from turtle import *
import turtle as tur

turt = tur.Turtle()
tur.title("Proposal")

def curve():
    for i in range(200):
        turt.right(1)
        turt.forward(1)

def heart():
    turt.fillcolor('red')
    turt.begin_fill()
    turt.left(140)
    turt.forward(113)
    curve()
    turt.left(120)
    curve()
    turt.forward(112)
    turt.end_fill()
  
def txt():
    turt.up()
    turt.setpos(-68, 95)
    turt.down()
    turt.color('cyan')
    turt.write(" I Love You ", font=("Times New Roman", 16, "bold")) #HERE, YOU CAN ADD SOMEONE'S NAME ALSO
heart()
txt()
tur.ht()
tur.done()
