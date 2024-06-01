#line bettinng project
import random


bank_balance = 5000

print(bank_balance)

print("for bank balance press 4")
print("chose your gambling mode \n1 - line betting \n2 - not availble \n3- not avaaliable")

mode = input("enter the mode number: ")

if mode == "1":
    print("welcome to line betting \nline betting wkrs like if the line u bet on reach end it wins else lose all money\nline purple = 16x(chance = 5%) \nline yellow = 2x(chance = 47.5%) \n line red = 2x(chance = 47.5% )")
    moneyamountline = int(input("enter the bet money: "))
    if moneyamountline > bank_balance:
        print("you don't have enough bank balance \ntry enter a vaild amount")
        moneyamountline = input("enter the bet money: ")
    else:
        print("which line you wanna bet on \n1 - line purple \n2 - line yellow \n3 - line red")
        choseline = int(input("enter the line number: "))
        if choseline in [1,2,3]:
           linsrandom = ['purple-------------| \nyellow--------     | \nred---------    | \npurple wins','purple----------   | \nyellow-------------| \nred-----        | \nyellow wins','purple---          | \nyellow-----------  | \nred---------------| \nred wins']
           chacnes = [5, 47.5, 47.5]
           wining_line = random.choices(linsrandom, weights=chacnes, k=100)[0]
           print("winning line = \n", wining_line)

           if choseline in wining_line:
              if wining_line == 1:
                 winingamountfor1 = moneyamountline * 16
                 bank_balance += winingamountfor1
                 print("you have won \n", winingamountfor1, "\nthanks for playing")
                 print("youre bank balance =",bank_balance)
                 back = print("1 - go back to mode 2 - go back to line betting")
                 if back == "1":
                     mode = input("enter the mode number: ")
                 elif back == "2":
                     choseline = input("enter the line number: ")
                 else:
                     exit()
              else:
                  winingamountfor1 = moneyamountline * 2
                  bank_balance += winingamountfor1
                  print("you have won \n", winingamountfor1, "\nthanks for playing")
                  print("youre bank balance =",bank_balance)
                  middle = print("1 - go back to mode 2 - go back to line betting")
                  if middle == "1":
                     mode = input("enter the mode number: ")
                  elif middle == "2":
                     choseline = input("enter the line number: ")
                  else:
                     exit()
           else:
               moneyamountline -= bank_balance
               print("you have lost \n", moneyamountline, "\nthanks for playing")
               print("youre bank balance =",bank_balance)
               front = print("1 - go back to mode 2 - go back to line betting")
               if front == "1":
                     mode = input("enter the mode number: ")
               elif front == "2":
                     choseline = input("enter the line number: ")
               else:
                     exit()
        else:
            print("the line number u chosen is invalid \nplease chose another one")
            choseline = input("enter the line number: ")        
elif mode =="4":
    print("youre bank balance is", bank_balance)
    mode = input("enter the mode number: ")
elif mode in ["2", "3"]:
    print("that mode is underocnstruction  \nplease try again")
    mode = input("enter the mode number: ")
else:
    print("that mode doesn't exist \n please try again")
    mode = input("enter the mode number: ")




    
    