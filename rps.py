print("Winning Rules of the Rock Paper Scissor Game as follows: \n"
                                +"\tRock  vs paper   -> paper wins \n"
                                +"\tRock  vs scissor -> Rock wins \n"
                                +"\tpaper vs scissor -> scissor wins \n") 

while True:

    # Tell User to enter either Rock, Paper, Scissor    
    print("Enter choice \n 1. rock \n 2. paper \n 3. scissor \n") 
      
    # Get the response from the User 
    user_choice = input("User turn: > ") 
    user_choice = user_choice.lower()
 
    # Print the response from the User 
    print("User has choosen : " + user_choice + "\n") 
    

    
    # Computer chooses randomly between Rock, Paper and Scissor
    import random
    comp_choice = random.choice(['rock','paper','scissor']) 

    # Print computers choice
    print("Computer choice is: " + comp_choice + "\n") 
  
    # Print User Choice and Computer Choice
    print("\t" + user_choice + "\n V/s \n" + "\t"+ comp_choice) 
    

    # Decide the condition of wining according to the Game Instructions
    result = None
    
    if((user_choice == "rock" and comp_choice == "paper") or
      (user_choice == "paper" and comp_choice == "rock" )): 
        result = "paper"
    elif((user_choice == "rock" and comp_choice == "scissor") or
        (user_choice == "scissor" and comp_choice == "rock")): 
        result = "rock"
    elif(user_choice == "rock" and comp_choice == "rock"): #additonal
        result = "rock"
    elif(user_choice == "paper" and comp_choice == "paper"): #additional
        result = "paper"
    elif(user_choice == "scissor" and comp_choice == "scissor"): #additional
       result = "scissor"
    else: 
        result = "scissor"
    

    # Compare the result with user and computer 
    # Printing either user or computer wins  
    if (result == user_choice and result == comp_choice): #additional
        print("<== Draw ==>") 
    elif (result == user_choice): 
        print("<== User wins ==>") 
    else: 
        print("<== Computer wins ==>") 
    
      
    
    # Get the response from User to Play Again    
    ans = input("Do you want to play again ? (Y/N) > ") 
  
    # Check the response from User and continue the loop
    # Otherwise break the loop to close the game
    if (ans == 'n' or ans == 'N') : 
        break
    
    
# Print a Thanks Message to the user
print("\nThanks for playing Rock Paper Scissor Game \n") 
