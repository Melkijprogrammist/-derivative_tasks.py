import random

# Словарь задач. Ключ - уровень сложности (легкий, средний, сложный), значение - список задач.
tasks = {
    "легкий": [
        {"task": "Найдите производную функции f(x) = 3x^2 + 2x - 1", "answer": "6x + 2"},
        {"task": "Найдите производную функции f(x) = 5x", "answer": "5"},
        {"task": "Найдите производную функции f(x) = 5x^3 + 5x - 5,", "answer": "15x² + 5"},
    ],
    "средний": [
        {"task": "Найдите производную функции f(x) = x^3 - 4x^2 + 7x - 2", "answer": "3x^2 - 8x + 7"},
        {"task": "Найдите производную функции f(x) = sin(x) + cos(x)", "answer": "cos(x) - sin(x)"},
       {"task": "Найдите производную функции f(x) = (2x² + 3x) * cos(x)", "answer": "(4x + 3)cos(x) - (2x² + 3x)sin(x)"},
    ],
    "сложный": [
        {"task": "Найдите производную функции f(x) = e^(2x) * sin(x)", "answer": "2e^(2x)sin(x) + e^(2x)cos(x)"}, # Используйте правило произведения
        {"task": "Найдите производную функции f(x) = ln(x^2 + 1)", "answer": "2x / (x^2 + 1)"}, # Используйте правило цепочки
        {"task": "Найдите производную функции f(x) = ln(√(x² + eˣ))", "answer": "(x + eˣ) / (2(x² + eˣ))"},
    ]
}

def get_task(difficulty):
    """Возвращает случайную задачу заданной сложности."""
    if difficulty in tasks:
        return random.choice(tasks[difficulty])
    else:
        return None

def check_answer(task, user_answer):
    """Проверяет правильность ответа пользователя."""
    return user_answer.lower() == task["answer"].lower()

def main():
    """Основная функция программы."""
    difficulty = input("Выберите уровень сложности (легкий, средний, сложный): ").lower()
    task = get_task(difficulty)

    if task:
        print(task["task"])
        user_answer = input("Ваш ответ: ")
        if check_answer(task, user_answer):
            print("Правильно!")
        else:
            print(f"Неправильно. Правильный ответ: {task['answer']}")
    else:
        print("Неверный уровень сложности.")


if __name__ == "__main__":
    main()
