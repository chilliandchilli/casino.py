 #-*- coding: UTF-8 -*-

Secret = 333

guess = int( raw_input ( "Ugani skrito številko (med 1 - 333):"))

if guess == Secret:
  print "Congratulations! You won! Number is 333!"

if guess > Secret:
    print "Wow, there are a lot of numbers, but limit your knowledge under 400!"

else:
  print "Sorry.. More luck next time! Secret number is not " + str(guess)