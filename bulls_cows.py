import random



###Function to generate 4 digits number (0-9) to guess
def generate_num():
  cnum=[]
  for i in range(10):
    cnum.append(i)
  # to get 4 digits from cnum list 
  to_guess=random.sample(cnum,4)
  print(to_guess)
  return to_guess

#compu_num = generate_num() #var that stores number to guess

###Function to get a number from player to compare with computer's number. A number is 4 unique digits
def player_input_num():
  
  while True:
    pnum = input("Enter your number: ")
    if len(pnum) !=4 or not pnum.isdigit():
      continue
    pnum = list(map(int, pnum)) #getting list as an input 
    if len(pnum) == len(set(pnum)):
      break
  return pnum

#player_num = player_input_num() #var that stores player's number

###Function to compare two numbers to determine bulls and cows
def compare_two_num(compu_num, player_num):

  bulls = 0
  cows = 0

  for i, num in enumerate(compu_num):
    if num in player_num:
      if compu_num[i] == player_num[i]:
        bulls +=1
      else:
        cows +=1


  return bulls, cows
  


#print(compare_two_num(compu_num, player_num))


def play():
  print("Bulls and Cows")
  print("*" * 80)

  print("The number to guess is a four digits number from 0 – 9, each digit is unique. For every guess the player gets 2 values: the number of bulls and the number of cows. Bulls – show how many digits the player’s number and computer’s number have in common and they are placed in the same positions. Cows – show how many digits the player’s number have in common with computer’s number, but those digits are in different position.The game continues until the number is guessed.")
  print("*" * 80)

  compu_num=generate_num()
  while True:
    
    player_num=player_input_num()
    bulls, cows = compare_two_num(compu_num, player_num)
    print("bulls: ", bulls, "cows: ", cows)
    if bulls == 4:
      break 
  print("You won")


play()