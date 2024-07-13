print("Welcome to the love calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

name1_lower = name1.lower()
name2_lower = name2.lower()

true_count = name1_lower.count('t') + name1_lower.count('r') + name1_lower.count('u') + name1_lower.count('e') + name2_lower.count('t') + name2_lower.count('r') + name2_lower.count('u') + name2_lower.count('e')

love_count = name1_lower.count('l') + name1_lower.count('o') + name1_lower.count('v') + name1_lower.count('e') + name2_lower.count('l') + name2_lower.count('o') + name2_lower.count('v') + name2_lower.count('e') 

total_count = int(str(true_count) + str(love_count))
if total_count < 10 or total_count > 90:
  print(f"Your Love Score is {total_count}%, you go together like coke and mentos.")
elif total_count >= 40 and total_count <= 50:
  print(f"Your Love Score is {total_count}%, you are alright together.")
else:
  print(f"Your score is {total_count}%")