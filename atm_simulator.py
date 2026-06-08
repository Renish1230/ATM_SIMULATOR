name = input("Enter Your NAME: ")
print(f"Hello {name}")
balance = 10000
balance = int(balance)
pin = 1234
logged_in = False
for attempt in range(1, 4):
    entered_pin = int(input("Enter your pin: "))

    if entered_pin == pin:
        print("Login Successful")
        logged_in = True
        break
    else:
        print(f"Wrong Pin!Attempts Left:{3-attempt}")
if not logged_in:
           print("Too Many Wrong Attempts! Account Locked")
else:
    while True:
      print("********MENU********")
      print("1. Check Balance")
      print("2.Deposit Money")
      print("3.Withdraw Money")
      print("4.Exit")
      x = int(input("Enter your choice: "))
      if x == 1:
         print(f"your available balance is ${balance}")
      elif x == 2:
         deposit = int(input("Enter your deposit amount: "))
         if deposit <= 0:
             print(f"Deposition Failed! Enter a value greater than 0")
         else:
             print(f"Successfully Deposited ${deposit}")
             balance = balance + deposit
             print(f"Your available balance is ${balance}")
      elif x == 3:
         withdraw = int(input("Enter your withdraw amount: "))
         if withdraw > balance:
             print(f"Withdraw Failed! Your available balance is ${balance}")
         else:
             print(f"Successfully Withdrawn ${withdraw}")
             balance = balance - withdraw
             print(f"Your available balance is ${balance}")
      elif x == 4:
         print("Thank You")
         break
      else:
          print("Choose a valid input")