import random

def multiplication_quiz():
    correct_answers = 0
    consecutive_incorrect = 0

    while correct_answers < 5:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        product = num1 * num2

        user_answer = int(input(f"Результат умножения {num1} на {num2}: "))

        if user_answer == product:
            correct_answers += 1
            consecutive_incorrect = 0
            if correct_answers == 3:
                print("Отличная работа! Продолжай в том же духе!")
            if correct_answers == 5:
                print("Поздравляем! Вы успешно прошли тест по таблице умножения!")
        else:
            print(f"Неправильно. Правильный ответ: {product}")
            consecutive_incorrect += 1
            if consecutive_incorrect == 3:
                print("Ты что, серьезно? Это же таблица умножения! Попробуй лучше следующий раз.")

multiplication_quiz()