# def check_func(param_func):
#   def inner_check_func(digit1, digit2):
#     if digit1 == 0 or digit2 == 0:
#       print("0으로 나눌 수 없습니다.")
#     else:
#       param_func(digit1, digit2)
  
#   return inner_check_func


# @check_func
# def divide_digit(digit1, digit2):
#   print(digit1 / digit2)
  
  
# divide_digit(1, 2)
# divide_digit(0, 2)
# divide_digit(2, 0)

# 연습문제
# def type_checker(param_func):
#   def inner_type_check(digit1, digit2):
#     if (type(digit1) != int) or (type(digit2) != int):
#       print("정수만 곱셈이 가능합니다.")
#       return 
    
#     param_func(digit1, digit2)
#   return inner_type_check
    
# @type_checker
# def mutiple_num (digit1, digit2):
#   print(digit1, digit2)
  
# mutiple_num(1, 2)
# mutiple_num(34, 2)
# mutiple_num(0.5, 0.2)

# 도전과제
# def mark_bold(param_func):
#   def inner_mark_bold(*args, **kwargs):
#     return "<b>" + param_func(*args, **kwargs) + "</b>"
  
#   return inner_mark_bold

# def mark_italic(param_func):
#   def inner_mark_italic(*args, **kwargs):
#     return "<i>" + param_func(*args, **kwargs) + "</i>"
  
#   return inner_mark_italic

# @mark_bold
# @mark_italic
# def print_content(content):
#   return content
  
  
# print(print_content("안녕하세요"))

# 도전과제 2

def make_html(tag):
  def outer_make_html(param_func):
    def inner_make_html(*args, **kwargs):
      return f"<{tag}>" + param_func(*args, **kwargs) + f"<{tag}>"
    return inner_make_html
  return outer_make_html


@make_html("h4")
def say_content(content):
  return content

print(say_content("안녕하세요?"))

print(say_content("누구세요?"))