"""
Завдання 7: Використання методу Монте-Карло

Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.

Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином (для перегляду перейди за цим шляхом assets/task_7_probability_table.jpg)

Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці.
"""
import random

def roll_dice():
    return random.randint(1, 6)

def simulate_dice_rolls(num_rolls):
    results = {}
    for _ in range(num_rolls):
        roll1 = roll_dice()
        roll2 = roll_dice()
        total = roll1 + roll2
        if total in results:
            results[total] += 1
        else:
            results[total] = 1
    return results

def calculate_probabilities(results, num_rolls):
    probabilities = {}
    for key, value in results.items():
        probabilities[key] = value / num_rolls
    return probabilities

def print_probability_table(probabilities):
    print("|  Sum  | Probability")
    print("-" * 21)
    for i in range(2, 13):
        print(f"|{i:^7}| {probabilities.get(i, 0):.2%}")

def main():
    num_rolls = 1_000_000
    results = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(results, num_rolls)
    print_probability_table(probabilities)

if __name__ == "__main__":
    main()
