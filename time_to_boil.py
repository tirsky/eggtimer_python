import math


def calc_boil_time(t_target:int=80,t_fridge:int=5,alt:int=175,weight=64)->float:
  """
  t_target: #egg temp
  t_fridge: temp in fridge
  alt: altitude above sea level
  weight: #weight of one egg
  """
  pw = math.pow(weight,2.0/3.0)
  af = (100- alt*0.003354-tFridge)
  at = (100-alt*0.003354-tTarget)
  _time = (0.451*pw*math.log(0.76*at/at)); #время варки вкрутую
  return round(_time,2) #in minutes


calc_boil_time()
