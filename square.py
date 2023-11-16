def area(a):
    ''''Принимаем значение а-сторона квадрата,возвращаем площадь квадрата'''
    if isinstance(a, (bool, str, float)):
        return "Invalid input"
    if (a <= 0):
        return "Invalid input"
    return a * a


def perimeter(a):
    '''Принимаем значение а-сторона квадрата,возвращаем периметр квадрата'''
    if isinstance(a, (bool, str, float)):
        return "Invalid input"
    if (a <= 0):
        return "Invalid input"
    return 4 * a
