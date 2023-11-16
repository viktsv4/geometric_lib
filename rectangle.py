def area(a,b):
    ''''Принимаем значение прямоугольника,возвращаем его  площадь '''
    if isinstance(a, (bool, str,float)) or isinstance(b, (bool, str,float)):
        return "Invalid input"
    if (a<=0 or b<=0):
        return "Invalid input"
    return a *b


def perimeter(a,b):
    '''Принимаем значение прямоугольника,возвращаем его  площадь'''
    if isinstance(a, (bool, str,float)) or isinstance(b, (bool, str,float)):
        return "Invalid input"
    if (a<=0 or b<=0):
        return "Invalid input"
    return 2*(a+b)
