import time

def timing_function(function):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f"Функція {function.__name__} виконана за {end_time - start_time:.6f} секунд")
        return result
    return wrapper


def test_timing_function():
    """
    Перевіряє, чи працює функція timing_function.
    """

    @timing_function
    def test_function():
        time.sleep(1)

    start_time = time.time()
    test_function()
    end_time = time.time()
    assert (end_time - start_time) >= 1, "Час виконання недостатній"
