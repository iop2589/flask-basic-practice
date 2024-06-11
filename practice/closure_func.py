def calc_power (n):
  def inner_calc (digit):
    return digit ** n
  
  return inner_calc


calc_funcs = list()

for num in range(1, 6):
  calc_funcs.append(calc_power(num))
  
for num in range(1, 6):
  for calc_func in calc_funcs:
    print(calc_func(num))