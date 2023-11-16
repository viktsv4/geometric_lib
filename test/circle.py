def area(r):
    '''принимаем r-радиус окружности и возвращает ее площадь'''
    if isinstance(r, (bool, str,float)):
        return "Invalid input"
    if (r <= 0):
        return "Invalid input"
    return  3.14 * r * r

def perimeter(r):
    '''принимает r-радиус окружности и возвращает ее периметр'''
    if isinstance(r, (bool, str,float)):
        return "Invalid input"
    if (r <= 0):
        return "Invalid input"
    return 2 *3.14*r

