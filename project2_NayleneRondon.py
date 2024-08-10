#------------------------------------------------------------------------------------------------------------------------
# project2_NayleneRondon.py
# Written by – Naylene Rondon
# Date Began – 02/15/17
# Date Last Modified: 02/22/17
# A Dragon game where a person is rummaging around the Kingdom under the
# mountain.
# You are placed in front of multiple doors and must avoid Smaug.
# You can collect gold and other prizes at your own risk.
# It continues until 5 lives are used or when the player chooses to quit.
#--------------------------------------------------------------------------------------------------------------------------
import time
import random

#Start


#Start Function Dictionary

#Main Function
def main():
    """The main function. Calls other functions."""

    #Variables
    loop = "yes"  #Controlled
    
    lives = int(5)
    gold = int(0)
    weapons = ""
    
    intro()
    
    while (lives > 0 or loop != "no"): #Loop
        
        #Choices
        NumDoors = randomAmount()
        UserDoor = choice(NumDoors)
        results = checkDoor(NumDoors, UserDoor)

        #Output
        lives = storyResults(results, lives, weapons)

        #Stat Editor
        lives = LifeOrDeath(results, lives)
        gold = goldMath(results, gold)
        weapons = weaponMath(results, weapons)

        #Stat Output
        stats(lives, gold,weapons)
        
        if(lives != 0):
            loop = input("Do you want to continue? (yes/no) ") #Output
            if loop == "no":
                break
        
            else:
                loop = "yes"
                
        else:
            loop = input("Try again? (yes/no) ")
            if loop == "no":
                print("Thanks for playing!")
                print()
                print("References:")
                print("The Hobbit: The Desolation of Smaug. Dir. Peter Jackson. Perf. Ian McKellen, Martin" +
                      "\n     Freeman, And Richard Armitage. MGM, 2013. Film.")
                print()
                print("Tolkien, J. R. R. The Hobbit. London: HarperCollins, 2014. Print.")
                break
        
            else:

                #Reset Variables
                lives = int(5)
                gold = int(0)
                weapons = ""
    

#Introduction Function
def intro():
    """This Function gives a bit of Backstory to the game. Also, it gives credit."""
    #Part 1
    print("Welcome to Dragon's Realm, Hobbit Edition.")
    print("Many aspects and dialogue are from")
    print("\"The Hobbit: The Desolation of Smaug\" and the book: \"The Hobbit.\"")
    print("Written by: J.R.R. Tolkien.")
    print("_______________________________________________________________________________\n\n")
          
    #Part 2
    print("After almost a year of journeying. You have reached the lonely mountain.")
    time.sleep(2)
    print("This mountain is the home of the Dwarve's Old Kingdom under the Mountain. \nWithin this kindom is...")
    time.sleep(3)
    print("Smaug! The Fire Drake.")
    time.sleep(2)
    print("When you enter the kingdom, you'll be faced with multiple doors.")
    time.sleep(2)
    print("Some doors will lead to gold and prizes." +
          "\nOthers will lead you into Smaug's chambers.")
    time.sleep(2)
    print("If you enter Smaug's chambers, he will attack you.")
    time.sleep(2)
    print("Choose wisely.")

    
#Door Amount Function
def randomAmount():
    """Generate Random Number between 3 - 5."""
    doors = random.randint(3,5)  #Choice between 3 - 5 doors
    return doors

#Choosing the Door Function
def choice(num):
    """Allows input of the user choice."""
    num = int(num)
    userDoor = int(0)
    
    #print(num, userDoor)  #Tester
    while userDoor == 0 or int(userDoor) > num:
        try:
            userDoor = int(input(("\nThere are " + str(num) + " doors. Pick one: ")))
            
        except ValueError:   #Found Exceptions in page 200 - 202 in Python Crash Course Book
            continue
                
    return int(userDoor)

#Random Scene Function
def ranScene():
    """Going to generate a random, dramatic scene."""
    scene = random.randint(1,4)
    #scene = 3  #Tester
    if (scene == 1):
        print("\nYou approach a large metal door.")
        time.sleep(3)
        print("\nIt's heavy and squeals as it opens. You pray Smaug hasn't heard it.")
        time.sleep(3)
        print("\nAs you step into the room. It is dark and cold. \nYou cannot feel any walls around you.")
        time.sleep(3)

    elif(scene == 2):
        print("\nThe door is made of wood. The handle made of rope.")
        time.sleep(3)
        print("\nIt feels brittle as if it's going to break as it opens.")
        time.sleep(3)
        print("\nThe cracks in the roof and in the walls allow strips of moonlight"
              + "\nto seep in.")
        time.sleep(3)

    elif(scene == 3):
        print("\nYou approach a crumbled door.")
        time.sleep(3)
        print("\nThere's barely any of the door left, \nso you squeeze through the open space.")
        time.sleep(3)
        print("\nAs you step into the room, you discovered it is as decayed as the door.")
        time.sleep(3)
        print("You feel uneasy as you hear the wind whisper through the cracks in the walls.")
        time.sleep(3)

    else:
        print("\nThe door is small. You'll have to crouch to pass underneath it.")
        time.sleep(3)
        print("\nIt hisses as it opens. A cool sweat runs down your back.")
        time.sleep(3)
        print("\nThe room beyond is as small as the door. Your head scrapes the ceiling and"
              + "\nyou can feel both walls with your hands.")
        time.sleep(3)
        

#Check Door
def checkDoor(num_Doors,user_Door):
    """Going to see if safe door is equal to death door."""
    ranScene() #Call Random Scene before checking door
    
    if(num_Doors == 3):    #If 3 doors, only two safe door
        safedoor1 = random.randint(1,num_Doors)
        safedoor2 = random.randint(1,num_Doors)
        #print(user_Door, safedoor1, safedoor2) #Tester 
        
        if user_Door == safedoor1:
            return "yes"
        elif user_Door  == safedoor2:
            return "yes"
        else:
            return "no"
        
    else: #If greater than 3 doors, will have three safe doors
        safedoor1 = random.randint(1,num_Doors)
        safedoor2 = random.randint(1,num_Doors)
        safedoor3 = random.randint(1,num_Doors)
        
        #print(user_Door, safedoor1, safedoor2, safedoor3) #Tester

        if user_Door == safedoor1:
            return "yes"
        elif user_Door  == safedoor2:
            return "yes"
        elif user_Door  == safedoor3:
            return "yes"
        else:
            return "no"

#Results Function
def storyResults(Succ_Fail, lifeNum, Weapon):
    """Will give special output based off whether you failed and still have lives, no lives, or is you succeed."""
    
    if Succ_Fail == "no":
        if lifeNum > 1:
            print("\nYou hear Smaug's voice echo throughout the kingdom.")
            time.sleep(2)
            print("\"Well, thief! I smell you, I hear your breath, I feel your air. Where are you?\" He says.")
            time.sleep(2)
            print("\"Where are you? Come now, don't be shy... step into the light.\"")
            time.sleep(2)

            Life = FightBack(lifeNum, Weapon)

            if (Life != lifeNum):
                print()
                
                return Life

            else:
                print("As he finished speaking, bright burning light, illuminated the room. \nYou run for cover and get a bit scorched.")

                return lifeNum
        else:
            print("Smaug's voice ripped through the air,")
            print("\"There you are, Thief in the Shadows!\"")
            time.sleep(2)
            print("Before you stood a massive red dragon. Wrapped around it's chest was like an \narmor of diamonds."
                  +"\nHe was an incredible beast.")
            time.sleep(2)

            Life = FightBack(lifeNum, Weapon)

            if (Life != lifeNum):
                print()

                return Life

            else:
        
                print("...")
                time.sleep(2)
                print("You cower into a corner and realize there is no escape.")
                time.sleep(2)
                print("You close your eyes and accept your fate.")
                time.sleep(2)
                print("Soon a piercing light envelops you.")
                time.sleep(2)
                print("Extreme heat burns away your flesh.")
                time.sleep(2)
                print("Smaug burns you to your death.")

                return lifeNum
                
    else:
        print("The room turns out to be safe. You discover prizes as you continue to wander.")
        time.sleep(2)
        print("However, it's not long until you make your way to another set of doors.")

        return lifeNum
    
    

#Lives Function
def LifeOrDeath(Succ_Fail, lifeNum):
    """Removes a life if you fail."""
    if Succ_Fail == "no":  #Removes a life
        lifeNum = lifeNum - 1 
        return lifeNum
    else:                #Does Nothing
        return lifeNum

#Gold Function
def goldMath(Succ_Fail, goldNum):
    """Gives or remove gold based on how you did."""
    gold = random.randint(50,200)
    
    if Succ_Fail == "no":
        if(goldNum == 0 or gold > goldNum):
            goldNum = goldNum
            
        else:
            goldNum = goldNum - gold
            print("\nYou dropped some gold.")
        
    else:
        goldNum = goldNum + gold
        print("\nYou have found gold!")

    return goldNum

#Weapons Function
def weaponMath(Succ_Fail, weapNum):
    """Will give weapons if you succeed."""
    new = random.randint(1,5)
    weapNew = ""
    
    if Succ_Fail == "no":
        return weapNum
        
    else:
        if (new == 1):
            weapNew = "Sword,"
            print("\nYou have found a Sword!")
        elif (new == 2):
            weapNew = "Dagger,"
            print("\nYou have found a Dagger!")
        elif (new == 3):
            weapNew = "Bow & Arrows,"
            print("\nYou have found a Bow & Arrows!")
        elif (new == 4):
            weapNew = "Axe,"
            print("\nYou have found an Axe!")
        else:
            weapNew = "Hammer,"
            print("\nYou have found a Hammer!")
        
        weapNew = weapNum + " " + weapNew

    return weapNew

#Stat Function
def stats(lifeNum, goldNum, WeapNum):
    """Output of the players current stats."""
    print()
    print("------------------------STATS------------------------")
    print("Lives: " + str(lifeNum))
    print("Gold: " + str(goldNum))
    print("Weapons: " + str(WeapNum))
    print("-----------------------------------------------------")
    
#Fight Back Function
def FightBack(Life, Weapon):
    """This will determine if you have a chance to fight back"""
    if (Weapon != ""):  #Will only play if they have weapon
        chance = random.randint(1,6)
        #chance = int(3)  #Tester

        if (chance == 3):  #Minimize chances
            print("You hold tightly to your weapons.")
            time.sleep(2)
            print("You hit Smaug and he laughs in your face.")
            time.sleep(2)
            print("\"Those do not hurt me!\" He says.")
            time.sleep(2)
            print("It didn't matter though because it distracted him.")
            time.sleep(2)
            print("You manage to evade Smaug.")
            time.sleep(2)
            print("You escape unharmed to the next series of doors.")
            Life = Life + 1

            return Life
        
        else:
            print("Your weapons couldn't save you from Smaug's flames.")
            return Life
    else:
        return Life
            

#End Function Dictionary



###Actual Program


#Program Start

main()


#Program End



#End
