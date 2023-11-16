def area(a, h):
    '''принимаем значения a,h-основания и высоты треугольника и возвращаем площадь треугольника'''
    if isinstance(a, (bool, str, float)) or isinstance(h, (bool, str, float)):
        return "Invalid input"
    if a <= 0 or h <= 0:
        return "Invalid input"
    return (a * h )/ 2 
def perimeter(a, b, c): 
    '''принимаем значения a,b,c-сторон треугольника и возвращаем периметр треугольника'''
    if isinstance(a, (bool, str,float)) or isinstance(b, (bool, str,float)) or isinstance(c, (bool, str,float)):
        return "Invalid input"
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid input"
    if a + b <= c or b + c <= a or a + c <= b:
        return "Invalid input"
    return a + b + c
