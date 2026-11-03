# Проект FitLife - MVP версия 1.1
# 0. Константы
WATER_PER_KG = 30  # 30 мл.-рекомендуемая норма воды на каждый кг. веса
WATER_ML_IN_L = 1000  # Количество мл. воды в литре

# 1. Знакомство
# 1.1. ввод имени пользователя
print("\nДобро пожаловать в FitLife!\n")
while True:
    user_name = input("Как тебя зовут? ").strip()
    if user_name:
        user_name = user_name.title()
        break
    print("Имя не может быть пустым. Попробуй ещё раз.")

# 1.2. ввод возраста пользователя
while True:
    user_age_str = input("Сколько тебе лет? ").strip()
    if not user_age_str:
        print("Поле не может быть пустым. Попробуй ещё раз.")
        continue
    try:
        user_age = int(user_age_str)
        if 5 <= user_age <= 120:  # границы возраста: 5 - 120 лет
            break
        else:
            print("Значение должно быть от 5 до 120 лет. Попробуй ещё раз.")
    except ValueError:
        print("Вводи только число. Попробуй ещё раз.")

print("\nДля расчёта показателей необходимы сведения о весе и росте:\n")
# 1.3. ввод веса пользователя
while True:
    user_weight_str = input("Напиши вес в кг (например, 70.2): ").strip()
    if not user_weight_str:
        print("Поле не может быть пустым. Попробуй ещё раз.")
        continue
    try:
        user_weight = float(user_weight_str)
        if 5 <= user_weight <= 250:  # границы веса: 5 - 250 кг
            break
        else:
            print("Значение должно быть от 5 до 250 кг. Попробуй ещё раз.")
    except ValueError:
        print("Вводи только число. Попробуй ещё раз.")

# 1.4. ввод роста пользователя
while True:
    user_height_str = input("Укажи рост в метрах (например 1.75): ").strip()
    if not user_height_str:
        print("Поле не может быть пустым. Попробуй ещё раз.")
        continue
    try:
        user_height = float(user_height_str)
        if 1.0 <= user_height <= 2.5:  # границы роста: 1.0 - 2.5 метров
            break
        else:
            print("Значение должно быть от 1.0 до 2.5 м. Попробуй ещё раз.")
    except ValueError:
        print("Вводи только число. Попробуй ещё раз.")

# 2. Логика расчетов
# 2.1. расчёт индекса массы тела (ИМТ)
bmi = round((user_weight / (user_height ** 2)), 1)

# 2.2. расчёт рекомендуемой нормы воды
water_ml = user_weight * WATER_PER_KG  # норма воды, выраженная в мл.
water_l = water_ml / WATER_ML_IN_L  # норма воды, выраженная в литрах

# 3. Вывод результата расчетов
print()
print("ОТЧЁТ ДЛЯ ПОЛЬЗОВАТЕЛЯ:")
print("-" * 50)
print(f"Привет, {user_name}!\n")
print(f"Твой возраст: {user_age} лет")
print(f"Твой индекс массы тела (ИМТ): {bmi}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. в день\n")
print("Расчет окончен. Будьте здоровы!")
print("-" * 50)
