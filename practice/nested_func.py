
def outer_func():
  print("call outer_func")
  
  def inner_func():
    print("call inner_func")
    
  print(inner_func())
  
outer_func()

# 호출 불가, 함수 내에서 선언되어 있으므로, 함수 내에서만 Call 가능
# inner_func()