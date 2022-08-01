c = 0
i = 1
import random
w = random.randint(1,100)
print ("Assalam-o-Alikum!!")
N = input ("What is your Name? ", )
print ("\nHello " + N + "! \nThis is just a simple game made by Shaheryar Ahmed Khan using basic python3 programming.\n\n In this game first of all computer will choose a number between 1 to 100 randomly & tell you to guess the number and if you guess in 5 turns than you will become a winner. Hope you like it!!")
print ("\nThe computer had chose a number between 1 and 100. Guess the number!!\n")
while ( c == 0 and i < 6 ) :
  a = input ("Enter a Number: ", )
  a = eval (a)
  if a==w :
    c = c + 1
    print ("Congratulations " + N + "!! You win...! You guessed in " , i , " turn(s).")
  if a > w :
    print ("Sorry! You guessed a high Number. Try Again.\n")
  if a < w :
    print ("Sorry! You guessed a low Number. Try Again.\n")
  i = i + 1
if (c==0):
   print ("Sorry " + N + "! You didnot guess the Number.. The Number was: ", w )