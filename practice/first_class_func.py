# def html_creator(tag):
#   def text_wrapper(msg):
#     print('<{0}><{1}</{0}>'.format(tag, msg))
    
#   return text_wrapper

# h1_html_creator = html_creator('h1')
# print(h1_html_creator)

# h1_html_creator("H1 태그는 타이틀을 표시하는 태그입니다.")

# p_html_creator = html_creator('p')
# p_html_creator("P 태그는 몰랑")


# nested func practice
def index_creator(idx):
  def list_print(list_data):
    for data in list_data:
      print('{0} {1}'.format(idx, data))
      
  return list_print


# func1 = index_creator("*")
# list_data = [1, 2, 3, 4, 5, 6, 7]

# func1(list_data)

from bs4 import BeautifulSoup
import requests


response = requests.get("https://davelee-fun.github.io/blog/crawl_html_css.html")
soup = BeautifulSoup(response.content)
courses = soup.select("ul#hobby_course_list > li")

results = list()

for data in courses:
  results.append(data.get_text())
  
data_minus_func = index_creator("-")

data_minus_func(results)