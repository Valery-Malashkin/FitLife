# Проект FitLife - MVP версия 1.0
# 0. Константы
WATER_PER_KG = 30  # 30 мл.-рекомендуемая норма воды на каждый кг. веса
WATER_ML_IN_L = 1000  # Сколько мл. воды в литре

# 1. Знакомство
print("\nДобро пожаловать в FitLife.\n")
user_name = input("А как тебя зовут? ").title()
user_name = user_name.strip() or "друг"
try:
    user_age_str = input("Сколько тебе лет? ")
    user_age = int(user_age_str)
except ValueError:
    user_age_str = input("Напиши цифрами свой возраст: ")
    user_age = int(user_age_str)

# 2. Сбор данных
print("\nДля расчёта показателей необходимы сведения о весе и росте:\n")
try:
    user_weight_str = input("Напиши вес в килограммах (например, 70.2): ")
    user_weight = float(user_weight_str)
except ValueError:
    user_weight_str = input("Нужно указать вес в кг., используя точку: ")
    user_weight = float(user_weight_str)
try:
    user_height_str = input("Укажи рост в метрах (например 1.75): ")
    user_height = float(user_height_str)
except ValueError:
    user_height_str = input("Нужно указать рост в метрах, используя точку: ")
    user_height = float(user_height_str)

# 3. Логика расчетов
# Расчёт индекса массы тела (ИМТ)
bmi = round((user_weight / (user_height ** 2)), 1)
# Расчёт рекомендуемой нормы воды
water_ml = user_weight * WATER_PER_KG  # норма воды, выраженная в мл.
water_l = water_ml / WATER_ML_IN_L  # норма воды, выраженная в литрах

# 4. Вывод красивого результата
print()
print("ОТЧЁТ ДЛЯ ПОЛЬЗОВАТЕЛЯ:")
print("-" * 50)
print(f"Привет, {user_name}!\n")
print(f"Твой возраст: {user_age} лет")
print(f"Твой индекс массы тела (ИМТ): {bmi}")
print(f"Рекомендуемая норма: {water_l:.1f} л. воды в день\n")
print("Расчет окончен. Будьте здоровы!")
print("-" * 50)
