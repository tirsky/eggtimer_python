import math


def calc_boil_time(t_target: int = 80, t_fridge: int = 5, alt: int = 175, weight=64) -> float:
    """
    t_target: int egg temp
    t_fridge: int temp in fridge
    alt: int altitude above sea level
    weight: int weight of one egg
    """
    pw = math.pow(weight, 2.0 / 3.0)
    af = (100 - alt * 0.003354 - t_fridge)
    at = (100 - alt * 0.003354 - t_target)
    _time = (0.451 * pw * math.log(0.76 * af / at))  # boil time for core temp t_target degree
    return round(_time, 2)  # in minutes


calc_boil_time()
