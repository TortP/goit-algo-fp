import random
import matplotlib.pyplot as plt


def monte_carlo_simulation(num_simulations):
    # Можливі суми від кидка двох кубиків (від 2 до 12)
    sum_counts = {i: 0 for i in range(2, 13)}

    # Симуляція кидка двох кубиків
    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)  # Перший кубик
        dice2 = random.randint(1, 6)  # Другий кубик
        dice_sum = dice1 + dice2
        sum_counts[dice_sum] += 1  # Підраховуємо частоту суми

    # Обчислюємо ймовірність для кожної суми
    probabilities = {key: (value / num_simulations) *
                     100 for key, value in sum_counts.items()}
    return probabilities


def display_results(probabilities):
    # Створення списків для побудови графіку
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    # Побудова стовпчикового графіку
    plt.bar(sums, probs, color='skyblue')
    plt.xlabel('Сума двох кубиків')
    plt.ylabel('Ймовірність (%)')
    plt.title('Ймовірність суми двох кубиків (метод Монте-Карло)')
    plt.show()


# Кількість симуляцій
num_simulations = 1000000

# Запускаємо симуляцію Монте-Карло
probabilities = monte_carlo_simulation(num_simulations)

# Відображаємо результати
display_results(probabilities)

# Виведення ймовірностей у табличній формі
print("Ймовірності для кожної суми:")
for sum_value, probability in probabilities.items():
    print(f"Сума {sum_value}: {probability:.2f}%")
