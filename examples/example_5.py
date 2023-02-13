from time import sleep


def slow_add(a: int, b: int) -> int:
    # sleep(10)
    return a + b


def slow_multiply(a: int, b: int) -> int:
    # sleep(10)
    return a * b


def complex_calculation(a: int, b: int) -> int:
    
    intermediate_step_1 = a + 1

    intermediate_step_2 = slow_add(intermediate_step_1, b)

    intermediate_step_3 = slow_multiply(intermediate_step_2, a)

    intermediate_step_4 = slow_add(intermediate_step_3, a)

    return intermediate_step_4 - 1
