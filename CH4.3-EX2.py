import turtle
bob = turtle.Turtle()
#print(bob)
#for i in range(4):
     #bob.fd(100)
     #bob.lt(90)
#turtle.mainloop()
th=100

def square(t,length):
    #t=turtle.Turtle()
    print(t)
    for i in range(4):
        t.fd(100+length)
        t.lt(90)

def sud(bob,th):
    square(bob,th)
#square(bob)
sud(bob,th)
turtle.mainloop()
