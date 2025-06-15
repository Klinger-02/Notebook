import turtle
import random
turtle.colormode(255)

tortuga = turtle.Turtle()
tortuga.hideturtle()
tortuga.penup()
tortuga.goto(-200, 200)
tortuga.setheading(0)

colores = [(200, 100, 100), (100, 200, 100), (100, 100, 200), (200, 200, 100), (100, 200, 200), (200, 100, 200)]

distancia = 40

tamano_punto = 15

def dibujar_punto():
    color = random.choice(colores)
    tortuga.dot(tamano_punto, color)

for fila in range(10):
    for columna in range(10):
        dibujar_punto()
dibujar_punto()
tortuga.forward(distancia)
tortuga.backward(distancia * 10)
tortuga.right(90)
tortuga.forward(distancia)
tortuga.left(90)


turtle.mainloop()