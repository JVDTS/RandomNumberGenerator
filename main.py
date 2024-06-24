import random

def Gen_Euro():
 random_main = sorted(random.sample(range(1, 31), 3))
 random_main2 = sorted(random.sample(range(31, 51),2))
 random_sub = sorted(random.sample(range(1, 11), 2))
 ENumbers = random_main + random_main2 + random_sub
 print("Here are Your numbers Good luck :",  str(ENumbers))

def Gen_Mega():
 random_main = sorted(random.sample(range(1, 31), 3))
 random_main2 = sorted(random.sample(range(31, 51),2))
 random_sub = sorted(random.sample(range(1, 11), 1))
 Megnumbers = random_main + random_main2 + random_sub
 print("Here are Your numbers Good luck :" ,Megnumbers)

def LotteryGenerator():
 print("Welcome to Lottery Generator")
 print("Press 1 for Euro Lottery Number Generator")
 print("Press 2 for Mega Lottery Generator")
 print("Press 3 for Exit")
 choice = int(input("Enter your choice : "))
  
 if choice == 1:
  Gen_Euro()
  print("\n")
  LotteryGenerator()
 elif choice == 2:
  Gen_Mega()
  print("\n")
  LotteryGenerator()
 elif choice == 3:
  print("Thank You for Stopping By See you Next time")
   
 else:
  print("Invalid , Please choose option 1, 2 or 3")
  print("\n")
  LotteryGenerator()
LotteryGenerator()
  



