# importing modules
import itertools, random

option = "Y"
wallet = 100

def start():
   keepgoing = 1
   global wallet
   option1 = ""

   # make a deck of cards
   deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
   
   # shuffle the cards
   random.shuffle(deck)

   #function to print the log
   def printlog():
      print('Log: ')
      print(f"First card was {first_card[0]} of {first_card[1]} \nNext card was {next_card[0]} of {next_card[1]}\n")
      print(f"BONUS ${bet}")

   #printing header
   print(f"\n-----------------------------------------")
   print(f"|    Welcome to BIG or SMALL game!!!    |")
   print(f"-----------------------------------------\n")

   print(f"Your balance is ${wallet}")
   bet_ = input('How much do you want to bet: ? ')
   while bet_.strip().isdigit() == False:
      print('Invalid input')
      bet_ = input('How much do you want to bet: ? ')
   bet = int(bet_)
   wallet = wallet - bet

   #print the first card and remove it from the deck
   first_card = deck[0]
   print(f"\nYour first card is {first_card[0]} of {first_card[1]}\n")
   deck.pop(0)

   counter = 0

   while keepgoing == 1:
      
      print(f"\nDo you think the next card is Bigger or Smaller than {first_card} ?")
      userInput = input('Write B for Bigger, S for Smaller and X for Cashout: ').upper()

      while userInput != 'B' and userInput != 'S' and userInput != 'X':
        print('Invalid input')
        userInput = input('Write B for Bigger, S for Smaller and X for Cashout: ').upper()
      
      next_card = deck[0]
      deck.pop(0)

      if(userInput == 'X'):
         wallet = wallet + bet
         print(f"Your new balance is ${wallet}")
         keepgoing = 0
      if(userInput == 'B' and next_card[0] > first_card[0]) or (userInput == 'S' and next_card[0] < first_card[0]) and (keepgoing == 1):
         print(f"\n------------------------------")
         print(f"|         Users wins         |")
         print("------------------------------")
         bet = bet * 2
         counter = counter + 1
         printlog()
         print(f"Winning {counter} times in a row!!!!")
         first_card = next_card
      elif (next_card[0] == first_card[0]) and (keepgoing == 1):
         print(f"\n------------------------------")
         print(f"|            Draw            |")
         print("------------------------------")
         printlog()
         first_card = next_card
      elif (keepgoing == 1):
         print(f"\n-------------------------------")
         print(f"|         Users loses         |")
         print("-------------------------------")
         bet = 0
         keepgoing = 0
         printlog()
         option1 = input(f"Do you want to check the sequence of the deck? Type Y and Enter : ").upper()
         if (option1 == 'Y'):
            print(f"\n-------------------------------")
            cont = 1 
            for i in deck:
               print(cont,"-",i)
               cont = cont + 1
            print(f"-------------------------------\n")

   option = input(f"Do you want to keep playing? type y and press enter to continue : ").upper()
   if (option == 'Y'):
      start()
   else:
      print(f"\nThank you for playing")
      print(f"You have ${wallet} in your wallet!")

      
start()
