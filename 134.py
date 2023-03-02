import sys

def safe_calculator(func):
    def wrapper(expression):
        try:
            return func(expression)
        except:
            print("Error: Invalid expression")
            sys.exit()
    return wrapper

@safe_calculator
def calculate(expression):
    return eval(expression)

print(calculate("2 + 2"))
print(calculate("4 / 0"))
