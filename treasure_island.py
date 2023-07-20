#!/bin/python3
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

f_inp = input("You have reached at a crossroad. Where do you want to go ? Please enter 'left' or 'right'! :  ").lower()


if f_inp == "left":
  s_input = input("Please enter if you have to 'Swim' or 'Wait' : ").lower()
  if s_input != "wait":
    print("Attacked by Trout ..! \nGame Over")
  else:
    t_input = input("Please enter the door which you have to enter ! 'Red' or 'Blue' or 'Yellow' : ").lower()
    if t_input == "red":
      print("Burned by Fire !! \nGame Over")
    elif t_input == "blue":
      print("Eaten by beasts.! \nGame Over")
    elif t_input == "yellow":
      print("You Win !!!!")
    else:
      print("Game Over!!")
elif f_inp == "right":
  print("Fall into a Hole !!\nGame Over")
else:
  print("Please enter correct choices ! 'Left' or 'Right'")

