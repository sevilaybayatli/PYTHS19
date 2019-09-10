import turtle
bob = turtle.Turtle()

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


    


    
    

