import random
#print multiline instruction performstring concatentation of string
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
       "Paper vs Scissors -> Scissors wins \n")

while True:
    print("Enter your choice \n 1. Rock \n 2. Paper \n 3. Scissors \n")

    #take input from user
    choice= int(input("Enter your choice : "))
    #or is the short- circuit operator if any of the condition is true then it return True or False
    #looping until user enter invalid input
    while choice > 3 or choice < 1:
        choice=int(input('Enter a valid choice please'))
        #initialize the value of choice_name variable corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    #print user choice
    print("User choice is\n", choice_name)
    print("Now its Computer Turn.....")
    
    #computer chooses randomly any number among 1,2,3. Using randint method of random module
    comp_choice = random.randint(1,3)
    #looping until the comp_choice value is equal to the choice value
    while comp_choice == choice:
        comp_choice= random.randint(1,3)
    
    #initialize the comp_choice_name variable corresponding to the choice value
    if comp_choice ==1:
        comp_choice_name = 'rocK'
    elif comp_choice == 2:
        comp_choice_name = 'papeR'
    else:
        comp_choice_name = 'scissoR'
    #print computer choice
    print("Comnputer choice is \n", comp_choice_name)
    print(choice_name, 'VS', comp_choice_name)
    #check for a draw
    if choice == comp_choice:
        print("Its a Draw", end="")
        result = "DRAW"
    #condition for winning
    if (choice==1 and comp_choice == 2):
        print("Paper wins =>\n", end="")
        result = "papeR"
    elif(choice == 2 and comp_choice == 1):
        print("paper wins =>\n", end="")
        result = 'Paper'

    
    if (choice==1 and comp_choice == 3):
        print("rock wins =>\n", end="")
        result='Rock'
    elif(choice==3 and comp_choice==1):
        print("Rock wins =>\n", end="")
        result = 'rocK'


    if (choice == 2 and comp_choice == 3):
        print("Scissor wins =>\n", end="")
        result = 'scissoR'
    elif(choice == 3 and comp_choice == 2):
        print("Scissor wins =>\n", end="")
        result = 'Scissor'

    #printing either user or computer wins or its a draw
    if result == "DRAW":
        print("<===Its a tie===>")
    if result == choice_name:
        print("<===User wins===>")
    else:
        print("<===Computer wins===>")
    print("Do you want to play again? (Y/N)")
    #if user input in n or N then condition is True
    ans=input().lower()
    if ans=='n':
        break
#come out of the while loop, print thanks for playing
print("Thanks for playing")
