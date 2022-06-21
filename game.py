'''
AIM
--> generation of 4 digit random no.
--> 10 times run then show tries over
--> no match - W
--> match but misplaced  - A
--> match and correct placed - R
'''

import random as ra

def ran_list():
    ran_string = str(random_Number)
    ran_map = map(int,ran_string)                                           #function to convert the random no generated to list
    ran_list = list(ran_map)
    return ran_list
    
def inputCode():
    userInput = int(input("Enter Your Guess"))
    digi_string = str(userInput)                                               # function to convert the input code to list
    digi_map = map(int,digi_string)
    digi_list = list(digi_map)
    return digi_list
    
print('''
      Welcome to the Guessing Game 
      Instructions for the game :
      --> Enter only integer
      --> You have 10 tries to guess the 4 digit no.
      --> No digits match - "W"
      --> Digit matched but wrong placement - "A"
      --> Both digit match and correct placed - "R"
      ''')

random_Number = ra.randint(1000, 9999)                                                       # 4 digit code generated 


x = ran_list()                                                                               
i = 0
while (i<10):
    result = ""
    y = inputCode()		
    
    if len(y) != 4:
        print("Enter only 4 digit number")                                                      # exceeds 4 digits
        continue		
    if (y == x):
        print("You guessed it !", x)                                                            # Totally correct
        break
    for elements in y:
        if elements in x:
            if y.index(elements) == x.index(elements):
                result += "R  "
            else:
                result += "A  "
        else:
            result += "W  "
    print(result)
    i+=1

else: 
    print("Your 10 chances are over, The Random no. was -->",x)




   
    
    
    
    