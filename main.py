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



# For Loop
websites = (
  "google.com",
  "airbnb.com",
  "twitter.com",
  "facebook.com",
  "tiktok.com"
)

for website in websites:
  print(website)
  