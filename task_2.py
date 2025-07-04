# Завдання 2

# Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха» за умови, що користувач повинен мати можливість вказати рівень рекурсії.

import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("black")

    t = turtle.Turtle()
    t.color("white")
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

# Виклик функції
level = int(input("Введіть рівень рекурсії (0-6)"))
draw_koch_snowflake(level)
