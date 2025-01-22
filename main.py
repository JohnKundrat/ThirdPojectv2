#Show the Fun History Quiz Game  Title
print(r"""     
 ('-. .-.           .-')    .-') _                _  .-')                          .-')                            .-') _  
( OO )  /          ( OO ). (  OO) )              ( \( -O )                       .(  OO)                          (  OO) ) 
,--. ,--.  ,-.-') (_)---\_)/     '._  .-'),-----. ,------.   ,--.   ,--.        (_)---\_)   ,--. ,--.    ,-.-') ,(_)----.  
|  | |  |  |  |OO)/    _ | |'--...__)( OO'  .-.  '|   /`. '   \  `.'  /         '  .-.  '   |  | |  |    |  |OO)|       |  
|   .|  |  |  |  \\  :` `. '--.  .--'/   |  | |  ||  /  | | .-')     /         ,|  | |  |   |  | | .-')  |  |  \'--.   /   
|       |  |  |(_/ '..`''.)   |  |   \_) |  |\|  ||  |_.' |(OO  \   /         (_|  | |  |   |  |_|( OO ) |  |(_/(_/   /    
|  .-.  | ,|  |_.'.-._)   \   |  |     \ |  | |  ||  .  '.' |   /  /\_          |  | |  |   |  | | `-' /,|  |_.' /   /___  
|  | |  |(_|  |   \       /   |  |      `'  '-'  '|  |\  \  `-./  /.__)         '  '-'  '-.('  '-'(_.-'(_|  |   |        | 
`--' `--'  `--'    `-----'    `--'        `-----' `--' '--'   `--'               `-----'--'  `-----'     `--'   `--------' 



""")

#Create list of questions that will user will be prompted with in the Quiz Game. 



questions = ("The Declaration of Independence was signed in 1776.",
             "Abraham Lincoln was the 16th President of the United States.",
            "The United States fought in World War I between 1914 and 1918.",
            "The first successful airplane flight was achieved by Thomas Edison.",
            "The U.S. Constitution was ratified in 1787.",
            "The Civil War in the United States ended in 1865.",
            "Benjamin Franklin was one of the signers of the U.S. Constitution.",
            "The first permanent English colony in America was Plymouth, founded in 1607.",
            "The Boston Tea Party occurred in 1773 as a protest against British taxation.",
            "The United States purchased the Louisiana Territory from France in 1803.",)
  

#Internal/back-end list of Answers to questions.

correctAnswer = ("T", "T", "F" , "F", "F", "T", "T", "F", "T", "T")

#set question iteration counter to 0, set user's game score to 0)
score = 0
i = 0

#Prompt user with Quiz Game.
print("Welcome to Quiz time! You will answer a few True or False Questions. Please ONLY enter the letter T or F when it's your turn to answer. Have fun!")
print("")

#Run main game loop


while i < len(questions):

    #Prompt question to user
    print(f"[{i+1}] {questions[i]}")

    #Get user Answer
    answer = input("Enter 'T' for True or 'F' for False: ")
    answer = answer.upper()
    
    #check if viable answer of 'T' or 'F' and if not, continue loop in current iteration
    if answer != "T" and answer != "F":
       print("You did not enter the letter T or F, please try again")
       continue
    
    #If viable answer in principle, check if correct Answer and if so, add 1 point to user's score, and increment to next iteration of game loop (i.e. next question)
    if answer == correctAnswer[i]:
      score += 1
      i += 1

    #if answer was not correct, move on to next question without increasing user's score.
    else:
      i += 1

#End of loop - display Answer to User. 
print("")
print(f"Quiz Complete, you answered {score} questions correctly out of {len(questions)}!") 
       
