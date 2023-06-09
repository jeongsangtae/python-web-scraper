# function + parameter
"""
def tax_calc(money):
  return money * 0.35

def pay_tax(tax):
  print("thank you for paying", tax)

pay_tax(tax_calc(150000000))
"""



# f()
"""
my_name = '상태'
my_age = 31
my_color = 'black'

print(f"안녕 나는 {my_name} {my_age}살이야 좋아하는 색은 {my_color}")
"""



# return
"""
def make_juice(fruit):
  return f"{fruit}+🥤"

def add_ice(juice):
  return f"{juice}+🧊"

def add_sugar(iced_juice):
  return f"{iced_juice}+🍾"

juice = make_juice("🥝")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)
print(perfect_juice)
"""



# if-else-elif
"""
winner = 5

if winner > 10:
  print("winner is greater than 10")
elif winner < 10:
  print("winner is less than 10")
else:
  print("winner is 10")

age = int(input("몇살이니?"))
"""



# And & Or
"""
if age < 18:
  print("You cant drink")
elif age > 18 and age < 35:
  print('you drink beer!')
elif age == 60 or age == 70:
  print("birthday party")
else:
  print("go ahead")
"""



# while + Python Standard Library
"""
from random import randint

print("파이썬 카지노 어서오세요")
pc_choice = randint(1, 100)


playing = True

while playing:
  user_choice = int(input("번호 선택 (1~100)"))

  if user_choice == pc_choice:
    print("이김")
    playing = False
  elif user_choice > pc_choice:
    print("그것보단 낮아")
  elif user_choice < pc_choice:
    print('그것보단 높아')
"""



# method
"""
name = "jeong"

print(name.upper())
print(name.capitalize())
print(name.endswith("o"))
print(name.replace("j", "y"))
"""



# List
"""
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", [1, 2, 3]]
print(days_of_week)

days_of_week.append("Sat")
print(days_of_week) 

days_of_week.append("Sun")
print(days_of_week) 
print(days_of_week[5][1])
print(days_of_week[6][1])

days_of_week.remove("Mon")
print(days_of_week)
"""




# Tuple
"""
days = ("Mon", "Tue", "Wed")

print(days[-3])
"""



# Dict
"""
player = {
  "name": "jeong",
  "age": 31,
  "alive": True,
  "fav_food": ["🍕", "🍔"]
}

print(player)
print(player['age'])
print(player["fav_food"])
print(player.get("fav_food"))
print(player.pop("age"))
player['xp'] = 999
player["fav_food"].append("🌭")
print(player)
"""



# For Loop + URL Formatting + Status Code
"""
from requests import get

websites = (
  "google.com",
  "airbnb.com",
  "https://twitter.com",
  "facebook.com",
  "https://tiktok.com",
  "https://httpstat.us/502",
  "https://httpstat.us/404",
  "https://httpstat.us/300",
  "https://httpstat.us/200",
  "https://httpstat.us/101"
)

results = {}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  if response.status_code >= 100 and response.status_code < 200:
    results[website] = "Information responses"
  elif response.status_code >= 200 and response.status_code < 300:
    results[website] = "OK"
  elif response.status_code >= 300 and response.status_code < 400:
    results[website] = "Redirect"
  elif response.status_code >= 400 and response.status_code < 500:
    results[website] = "Client Error"
  else:
    results[website] = "Server Error"

print(results)
"""



# JOB SCRAPPER
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?&term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text, 'html.parser')
  jobs = soup.find_all('section', class_="jobs")
  for job_section in jobs:
    job_posts = job_section.find_all("li")
    job_posts.pop(-1)
    for post in job_posts:
      print(post)
      print("/////////////")