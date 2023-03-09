def test_timing_function():

    @timing_function
    def test_function():
        time.sleep(1)

    start_time = time.time()
    test_function()
    end_time = time.time()
    assert (end_time - start_time) >= 1, "Час виконання недостатній"
