import turtle
import math

# Налаштування екрану
window = turtle.Screen()
window.bgcolor("white")

# Створюємо об'єкт "черепашка"
pen = turtle.Turtle()
pen.color("red")
pen.speed(0)

# Функція для малювання дерева Піфагора


def draw_pythagoras_tree(branch_len, depth, angle):
    if depth > 0:
        # Малюємо основну гілку
        pen.forward(branch_len)

        # Ліва гілка
        pen.left(angle)
        draw_pythagoras_tree(branch_len * math.sqrt(2) / 2, depth - 1, angle)

        # Повертаємося до початкової точки
        pen.right(2 * angle)
        draw_pythagoras_tree(branch_len * math.sqrt(2) / 2, depth - 1, angle)

        # Повертаємо початкове положення черепашки
        pen.left(angle)
        pen.backward(branch_len)

# Функція для початкового виклику рекурсії


def draw_tree(branch_len, depth):
    pen.left(90)  # Орієнтуємо "дерево" вертикально
    draw_pythagoras_tree(branch_len, depth, 45)


# Введення рівня рекурсії від користувача
depth = int(input("Введіть рівень рекурсії: "))
branch_len = 100  # Довжина початкової гілки

# Виклик функції для малювання
draw_tree(branch_len, depth)

# Залишаємо вікно відкритим після малювання
window.mainloop()
