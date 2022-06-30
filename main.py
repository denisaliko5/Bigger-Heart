def main():
  import turtle,math
  t = turtle.Turtle()
  t.ht()
  t.color("red")
  t.pensize(10)
  t.speed(0)
  a=90
  a1=a*2+a/2
  def draw_heart(r):
      for i in range(7):
        r+=20
        p=(0.375)*r*2*math.pi
        t.seth(a)
        t.begin_fill()
        t.circle(r,a1)
        t.fd(p)
        t.seth(-t.heading())
        t.fd(p)
        t.circle(r,a1)
        t.end_fill()
        y=t.ycor()+20
        t.clear()
        t.pu()
        t.goto(0,y)
        t.pd()
  draw_heart(10)
  reset = True
  if reset == True:
    main()
main()