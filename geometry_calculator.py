import math

def area_circle(radius: float) -> float:
    """Площа кола"""
    if radius < 0:
        raise ValueError("Радіус не може бути від'ємним")
    return math.pi * radius ** 2

def area_rectangle(width: float, height: float) -> float:
    """Площа прямокутника"""
    if width < 0 or height < 0:
        raise ValueError("Сторони не можуть бути від'ємними")
    return width * height

def area_triangle(base: float, height: float) -> float:
    """Площа трикутника"""
    if base < 0 or height < 0:
        raise ValueError("Основа і висота не можуть бути від'ємними")
    return 0.5 * base * height

def area_trapezoid(a: float, b: float, height: float) -> float:
    """Площа трапеції"""
    return 0.5 * (a + b) * height

if __name__ == "__main__":
    print(f"Коло r=5:          {area_circle(5):.2f} кв.од")
    print(f"Прямокутник 4x6:   {area_rectangle(4, 6):.2f} кв.од")
    print(f"Трикутник 3x8:     {area_triangle(3, 8):.2f} кв.од")
    print(f"Трапеція 3,7 h=4:  {area_trapezoid(3, 7, 4):.2f} кв.од")
