import turtle
'''
Fractal tree using recursion 
'''
def tree(length,p=90,branches=2,scale = 0.5,faction = 1.4,min_length = 10):
    step = float(p/(branches-1))
    scale /= faction
    turtle.forward(length)
    if length > min_length:
        turtle.left(p/2)
        tree(scale*length, p,branches,scale,faction,min_length)
        for c in range(branches-1):
            turtle.right(step)
            tree(scale*length, p,branches,scale,faction,min_length)
        turtle.left(p/2)
    turtle.back(length)

turtle.left(90)
tree(80,p=120,branches = 12)
turtle.exitonclick()
