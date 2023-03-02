def safe_calculate(func):
    def wrapper(expression):
        if any(sym in expression for sym in ('import', 'exec', 'eval')):
            raise ValueError('Unsafe expression')
        try:
            result = func(expression)
            return result
        except Exception as e:
            print(f'Error: {e}')
    return wrapper
