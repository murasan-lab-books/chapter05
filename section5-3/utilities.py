# utilities.py
def celsius_to_fahrenheit(celsius):
    """摂氏を華氏に変換"""
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """華氏を摂氏に変換"""
    return (fahrenheit - 32) * 5/9

def calculate_bmi(weight, height):
    """BMIを計算（体重kg、身長m）"""
    return weight / (height ** 2)
