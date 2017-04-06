import turtle
"""
Fractal snowflake
"""
def snowflake(l, d):
   if d == 0:
     turtle.forward(l)
   else:
     snowflake(l/2, d-1)
     turtle.right(80)
     snowflake(l/2, d-1)
     turtle.left(160)
     snowflake(l/2, d-1)
     turtle.right(80)
     snowflake(l/2, d-1)



snowflake(250,4)
