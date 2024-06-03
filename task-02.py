"""
Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. 
Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.
"""

import turtle

def draw_pifagor_tree(branch_len, level):
    if level == 0:
        return
    turtle.forward(branch_len)
    turtle.right(45)
    draw_pifagor_tree(0.7 * branch_len, level - 1)
    turtle.left(90)
    draw_pifagor_tree(0.7 * branch_len, level - 1)
    turtle.right(45)
    turtle.backward(branch_len)


def main(user_input):
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("blue")
    turtle.left(90)
    draw_pifagor_tree(
        branch_len=80, level=user_input
    )  # set branch length and recursion level
    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    while True:
        try:
            user_input = int(input("Enter an integer from 1 to 7: "))
            if 0 < user_input < 8:
                main(user_input)
                break
            else:
                print("Input is out of range")
        except ValueError:
            print("Input is not integer")
