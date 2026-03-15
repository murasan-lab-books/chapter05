# main.py
import utilities

# 温度変換
temperature_c = 30
temperature_f = utilities.celsius_to_fahrenheit(temperature_c)
print(f"気温: {temperature_c}°C = {temperature_f}°F")

# BMI計算
weight = 65
height = 1.70
bmi = utilities.calculate_bmi(weight, height)
print(f"BMI: {bmi:.1f}")
