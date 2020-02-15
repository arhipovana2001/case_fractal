#fractal case

#this program is designed to draw fractals.
#the program prompts the user to select the desired fractal, depth of the recursion and length of the side.

# Developers:   Arhipova A. (%),
#               Revtova L. (%),
#               Zaitseva A.   (%).

import turtle as t
import local
choose = int(input(local.CHOOSE))
if choose == 1:
    import local_english as lc
elif choose == 2:
    import local_russian as lc
elif choose == 3:
    import local_italiano as lc

def koch(order, size):
    t.color('#0000FF')
    if order == 0:
        t.forward(size)
    else:
        koch(order - 1, size / 3)
        t.left(60)
        koch(order - 1, size / 3)
        t.right(120)
        koch(order - 1, size / 3)
        t.left(60)
        koch(order - 1, size / 3)

def snow_koch(order, size):
    for i in range(3):
        koch(order, size)
        t.right(120)

def mink(order, size):
    t.color('#00FA9A')
    if order == 0:
        t.forward(size)
    else:
        mink(order - 1, size / 4)
        t.left(90)
        mink(order - 1, size / 4)
        t.right(90)
        mink(order - 1, size / 4)
        t.right(90)
        mink(order - 1, size / 4)
        mink(order - 1, size / 4)
        t.left(90)
        mink(order - 1, size / 4)
        t.left(90)
        mink(order - 1, size / 4)
        t.right(90)
        mink(order - 1, size / 4)

def levy(order, size):
    t.color('#FF1493')
    if order == 0:
        t.forward(size)
    else:
        t.pendown()
        t.left(45)
        levy(order - 1, size / 2)
        t.right(90)
        levy(order - 1, size / 2)
        t.left(45)
        t.penup()

def ice_1(order, size):
    if order == 0:
        t.forward(size)
    else:
        t.pendown()
        ice_1(order - 1, size / 2)
        t.left(120)
        ice_1(order - 1, size / 4)
        t.left(180)
        ice_1(order - 1, size / 4)
        t.left(120)
        ice_1(order - 1, size / 4)
        t.left(180)
        ice_1(order - 1, size / 4)
        t.left(120)
        ice_1(order - 1, size / 2)
        t.penup()
    
def snow_ice_1(order, size):
    t.color('#000080')
    t.left(90)
    for i in range(3):
        ice_1(order, size)
        t.left(180)
        ice_1(order, size)
        t.left(60)
    t.right(60)
    for i in range(3):
        ice_1(order, size)
        t.left(180)
        ice_1(order, size)
        t.left(60)  
        
def ice_2(order, size):
    if order == 0:
        t.forward(size)
    else:
        t.pendown()
        ice_2(order - 1, size / 2)
        t.left(90)
        ice_2(order - 1, size / 4)
        t.left(180)
        ice_2(order - 1, size / 4)
        t.left(90)
        ice_2(order - 1, size / 2)
        t.penup()    
    
 def snow_ice_2(order, size):
    t.color('#000080')
    t.left(90)
    for i in range(3):
        ice_2(order, size)
        t.left (180)
        ice_2(order, size)
        t.left(60)
    t.right(60)
    for i in range(3):
        ice_2(order, size)
        t.left(180)
        ice_2(order, size)
        t.left(60)
        
def main():
    t.speed(0)
    t.up()
    t.goto(-100, 0)
    t.down()

    choice = int(input(lc.INP_3))
    n = int(input(lc.INP_1))
    a = int(input(lc.INP_2))

    if choice == 1:
        koch(n, a)
    elif choice == 2:
        snow_koch(n, a)
    elif choice == 3:
        ice_1(n, a)
    elif choice == 4:
        ice_2(n, a)
    elif choice == 5:
        snow_ice_1(n, a)
    elif choice == 6:
        snow_ice_2(n, a)
    elif choice == 7:
        mink(n, a)
    elif choice == 8:
        levy(n, a)
    #elif choice == 9:
    #   tree(n, a)
    #elif choice == 10:
    #    dragon(n, a)
    t.done()
main()

