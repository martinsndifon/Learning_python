from turtle import*
import colorsys
tracer (50)
bgcolor ('black')
pensize (4)
h = 0.4

for i in range (1000):
	c = colorsys.hsv_to_rgb(h, 1, 1)
	color (c)
	h += 1/37
	up()
	forward(i)
	goto(0,0)
	down()
	left(288)
	circle(i, -180)
done()
