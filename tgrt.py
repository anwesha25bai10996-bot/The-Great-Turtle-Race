import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
Screen = turtle.Screen()
Screen.setup(WIDTH, HEIGHT)
Screen.title('The Great Turtle Race')
COLORS = ['red', 'green', 'blue', 'yellow', 'purple', 'brown', 'gray', 'pink', 'olive', 'orange']

def get_the_num_of_racers():
  while True:
    racers = input("Enter the number of racers (2-10): ")
    if racers.isdigit():
      racers = int(racers)
      if 2 <= racers <= 10:
        return racers
    print("Input is not numeric or not in range 2-10. Try again!")

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.speed(2)
        racer.shape('turtle')
        racer.color(color)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        racer.left(90)
        turtles.append(racer)
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('The Great Turtle Race')

racers = get_the_num_of_racers()
random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f'The winner is the turtle with color {winner}')
Screen.mainloop()
