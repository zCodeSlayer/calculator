def calculator(expression):
    allowed = '+-/*%'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Выражение должно содержать хотя бы один знак ({allowed})')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                return {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b,
                    '%': lambda a, b: a % b,
                }[sign](left, right)
            except(ValueError, TypeError):
                raise ValueError('Выражение должно содержать два целых числа и один знак (+-/*%)')
