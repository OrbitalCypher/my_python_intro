import random
secret_number = random.randint(1,99)
number_of_guesses = 1
while number_of_guesses <5:
    input_u = input ("Enter Your Number From 1 - 99: ")
    number_of_guesses+=1
    if input_u == secret_number:
        print "Congrats, You Win"
        break
    elif input_u > secret_number:
            print "Your Guess Was High !"
            print "You Have Used " +str(number_of_guesses)+" Guesses"
        
    elif secret_number > input_u:
            print "Your Guess Was Low!"
            print "You Have Used " +str(number_of_guesses)+ " Guesses"
        
        
