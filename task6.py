# Дані про їжу: вартість та калорійність
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм для вибору страв з максимальним співвідношенням калорій до вартості


def greedy_algorithm(items, budget):
    """
    Реалізує жадібний підхід: вибираємо страви, які мають найбільше співвідношення калорій до вартості.
    """
    # Сортуємо страви за співвідношенням калорій до вартості
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    total_cost = 0  # Загальна вартість вибраних страв
    total_calories = 0  # Загальна калорійність вибраних страв
    chosen_items = []  # Список вибраних страв

    # Ітеруємо по відсортованих стравах
    for item, info in sorted_items:
        # Додаємо страву до вибору, якщо вона не перевищує бюджет
        if total_cost + info["cost"] <= budget:
            chosen_items.append(item)
            total_cost += info["cost"]
            total_calories += info["calories"]

    return chosen_items, total_calories

# Динамічне програмування для вибору страв, що максимізують калорійність в межах бюджету


def dynamic_programming(items, budget):
    """
    Алгоритм динамічного програмування для знаходження оптимального набору страв для максимізації калорійності при заданому бюджеті.
    """
    # Таблиця dp для збереження максимальних калорій для кожного бюджету
    dp = [0] * (budget + 1)
    # Список для запам'ятовування вибору страв для кожного бюджету
    chosen_items = [[] for _ in range(budget + 1)]

    # Ітеруємо по кожній страві
    for item, info in items.items():
        cost = info["cost"]  # Вартість страви
        calories = info["calories"]  # Калорійність страви

        # Оновлюємо таблицю dp у зворотному порядку, щоб уникнути перезапису попередніх значень
        for current_budget in range(budget, cost - 1, -1):
            # Якщо додавання страви покращує результат, оновлюємо dp і зберігаємо вибір
            if dp[current_budget - cost] + calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - cost] + calories
                chosen_items[current_budget] = chosen_items[current_budget - cost] + [item]

    return chosen_items[budget], dp[budget]


# Бюджет, в межах якого вибираємо страви
budget = 100

# Використання жадібного алгоритму
greedy_result, greedy_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_result)
print("Сумарна калорійність:", greedy_calories)

# Використання динамічного програмування
dp_result, dp_calories = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print("Вибрані страви:", dp_result)
print("Сумарна калорійність:", dp_calories)
