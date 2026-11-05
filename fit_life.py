# Проект FitLife - MVP версия 1.2
# 0. Константы
AGE_MIN = 5              # минимальная граница возраста, лет
AGE_MAX = 120            # максимальная граница возраста, лет

WEIGHT_MIN = 5.0         # минимальная граница веса, кг
WEIGHT_MAX = 250.0       # максимальная граница веса, кг

HEIGHT_MIN = 1.0         # минимальная граница роста, м
HEIGHT_MAX = 2.5         # максимальная граница роста, м

WATER_PER_KG = 30        # 30 мл.-рекомендуемая норма воды на каждый кг. веса
WATER_ML_IN_L = 1000     # Количество мл. воды в литре

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
    except ValueError:
        print("Вводи только целое число. Попробуй ещё раз.")
        continue
    if AGE_MIN <= user_age <= AGE_MAX:
        break
    else:
        print(f"""Значение должно быть от {AGE_MIN} до {AGE_MAX} лет.
              Попробуй ещё раз.""")

print("\nДля расчёта показателей необходимы сведения о весе и росте:\n")
# 1.3. ввод веса пользователя
while True:
    user_weight_str = input("Напиши вес в кг (например, 70.2): ").strip()
    if not user_weight_str:
        print("Поле не может быть пустым. Попробуй ещё раз.")
        continue
    try:
        user_weight = float(user_weight_str)
    except ValueError:
        print("Вводи только число через точку. Попробуй ещё раз.")
        continue
    if WEIGHT_MIN <= user_weight <= WEIGHT_MAX:
        break
    else:
        print(f"""Значение должно быть от {WEIGHT_MIN} до {WEIGHT_MAX} кг.
              Попробуй ещё раз.""")

# 1.4. ввод роста пользователя
while True:
    user_height_str = input("Укажи рост в метрах (например 1.75): ").strip()
    if not user_height_str:
        print("Поле не может быть пустым. Попробуй ещё раз.")
        continue
    try:
        user_height = float(user_height_str)
    except ValueError:
        print("Вводи только число через точку. Попробуй ещё раз.")
        continue
    if HEIGHT_MIN <= user_height <= HEIGHT_MAX:
        break
    else:
        print(f"""Значение должно быть от {HEIGHT_MIN} до {HEIGHT_MAX} м.
              Попробуй ещё раз.""")

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
