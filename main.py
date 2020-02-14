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
