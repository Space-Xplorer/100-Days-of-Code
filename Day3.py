print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************'
''')
#The three single quotes help write codes in multiple lines.

print("Welcome to the world of Jumanji")
print("Do you accept the risks of Jumaji? \nFailing to comply will land you in trouble")
a = input("Type \"Yes\" or \"No\"\n").lower()

if a == 'no':
    print()
    print("!!!!!!You've encountered the wrath of Van pelt!!!!!!!")
    print("Van: \"You mortal beings are not worth it, I shall curse you to be eternally banished from the world of Jumanji\"")
    print()
elif a == 'yes':
    print()
    print("Van: \"You are brave young person, come on I shall guide you through the game\"")
    print("Van: \"I am Van Pelt, cursed to guide all souls who arive here, by choice or by chance\"")
    print()
    print("Van: \"Welcome to Jumanji, a cursed world struck for a millenia.\nYour job is to find the jewel of the panther and thou shall be freed\"")
    print("With me, the world rewinds or freezes still. To beat me, you need courage and will. What am I?")
    b = input("Type the answer:\n").lower()
    if b == 'dice':
        print()
        print("Van: \"Alrighty, you seem intelligent, let's go for the next one\"")
        print("Van: \"You've reached an end, there is a river here, and an island in the middle of it.\nWhat's your next move")
        print("Would you wait for a boat or swim across the river?")
        c = input("Type \"Swim\" or \"Wait\"\n").lower()
        if c == 'swim':
            print()
            print("Attacked by crocodiles\n  GAME OVER\n")
        elif c == 'wait':
            print()
            print("Van: \"Look there's a ship coming for us\"")
            print("Van: \"Actually there are three... which one do you choose\"")
            print("There's a red, white and a blue boat waiting for you choose one to continue your journey")
            d = input("Type \"Red\" or \"Blue\" or \"White\"\n").lower()
            if d == 'red':
                print()
                print("You were attacked by the blood hungry demons.\n GAME OVER")
            elif d == 'white':
                print()
                print("It was a mirage projected by deadly water beings, you were killed as a sport by their queen\n GAME OVER")
            elif d == 'blue':
                print()
                print("You have choosen the right one!")
                print("Van: \"Now on the journey is yours to cross, find the jewel and you'd be freed from the game")
                print("CHAPTER 1 ENDS HERE")
    else:
        print()
        print(" GAME OVER\n")