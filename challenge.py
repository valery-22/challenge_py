import os,time,random

def add():
  os.system("clear")
  idea = input("Idea > ")
  with open("my.ideas","a+") as f:
    f.write(f"{idea}")
  print("Idea added")
  time.sleep(1)
  os.system("clear")

def show():
  os.system("clear")
  with open("my.ideas","r") as f:
    ideas = f.readlines()
    if ideas:
      print(f"Random idea: {random.choice(ideas).strip()}")
    else:
      print("No ideas found. Add some ideas first.")
  time.sleep(1)
  os.system("clear")

while True:
  print("Idea storage")
  print()
  menu = input("a:Add an idea r: Show a random idea > ")
  if menu == "a":
    add()
  elif menu == "r":
    show()
  else:
    print("Invalid option.")