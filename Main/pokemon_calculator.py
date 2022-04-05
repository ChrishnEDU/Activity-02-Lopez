#Libraries
import random


#Default Damage Multipliers
badgedmg = 1
typeadvdmg = 1
weatherdmg = 1

#Attacker Pokemon Level
print('Pokemon Damage Calculator')
atkname = input("Enter the name of attacker Pokemon: ")
level = float(input("Pokemon Level: "))

defname = input("Enter the name of target Pokemon: ")
deflvl = float(input("Pokemon Level: "))

#Attacker Pokemon Type
q1 = input('Is your Pokemon a dual type or not?: ')
if q1 == "Yes" or q1 == "yes":
    type1 = input("Enter the primary type of your Pokemon: ")
    type2 = input("Enter the secondary type of your Pokemon: ")
elif q1 == "No" or q1 == "no":
    type1 = input("Enter the type of your Pokemon: ")
    type2 = ""

#Target Pokemon Type
q2 = input('Is your Enemy Pokemon a dual type or not?: ')
if q2 == "Yes" or q2 == "yes":
    etype1 = input("Enter the primary type of enemy Pokemon: ")
    etype2 = input("Enter the secondary type of enemy Pokemon: ")
elif q2 == "No" or q2 == "no":
    etype1 = input("Enter the type of enemy Pokemon: ")
    etype2 = ""

#Single or Multiple Targets
targets = input('Are you attacking at two or more targets?: ')
if targets == "Yes" or targets == "yes":
    targetdmg = 0.5
elif targets == "No" or targets == "no":
    targetdmg = 1

#Power, Special / Attack Damage & Special / Defense Damage
pwr = float(input('Enter Move base power here: ')) #Determine the Effectiveness of Move used
patk = float(input('Enter your Pokemon Attack / Sp. Attack: '))
movetype = input('Move Type: ') #Determine Effectiveness of Attack

#Target Normal/Special Defense
pdef = float(input('Enter enemy Defense / Sp. Defense: '))


#Weather Advatage Check
weather = input('Input weather effect: ')

#Critical Damage
crithit = random.randint(1,2)
if crithit == 1:
    critdmg = 2
elif crithit == 2:
    critdmg = 1

#STAB Multiplier
if (type1 or type2) != movetype:
    stabdmg = 1
else:
    stabdmg = 1.5

#Burn RNG
if (etype1 or etype2) == "Fire" or (etype1 or etype2) == "Dragon":
    burnrng = random.randint(1,2)
    if burnrng == 1: 
        burneddmg = 0.5
    elif burnrng == 2: 
        burneddmg = 1.0  
else:
    burneddmg = 1 #Default Value

#Damage RNG
x = random.randint(1,2)
if x == 1:
    randomdmg = 0.85
elif x == 2:
    randomdmg = 1.0


#Pokemon Types Atk Advantages
#Normal
if (type1 == "Normal" and etype1 == "Ghost" or type1 == "Normal" and etype2 == "Ghost") or (type2 == "Normal" and etype1 == "Ghost" or type2 == "Normal" and etype2 == "Ghost"):
    typeadvdmg = 0

elif (type1 == "Normal" and etype1 == "Rock" or type1 == "Normal" and etype2 == "Rock") or (type2 == "Normal" and etype1 == "Rock" or type2 == "Normal" and etype2 == "Rock"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Normal" and etype1 == "Steel" or type1 == "Normal" and etype2 == "Steel") or (type2 == "Normal" and etype1 == "Steel" or type2 == "Normal" and etype2 == "Steel"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

#Fight
elif (type1 == "Fight" and etype1 == "Ghost" or type1 == "Fight" and etype2 == "Ghost") or (type2 == "Fight" and etype1 == "Ghost" or type2 == "Fight" and etype2 == "Ghost"):
    typeadvdmg = 0

elif (type1 == "Fight" and etype1 == "Flying" or type1 == "Fight" and etype2 == "Flying") or (type2 == "Fight" and etype1 == "Flying" or type2 == "Fight" and etype2 == "Flying"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Fight" and etype1 == "Poison" or type1 == "Fight" and etype2 == "Poison") or (type2 == "Fight" and etype1 == "Poison" or type2 == "Fight" and etype2 == "Poison"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Fight" and etype1 == "Bug" or type1 == "Fight" and etype2 == "Bug") or (type2 == "Fight" and etype1 == "Bug" or type2 == "Fight" and etype2 == "Bug"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Fight" and etype1 == "Psychic" or type1 == "Fight" and etype2 == "Psychic") or (type2 == "Fight" and etype1 == "Psychic" or type2 == "Fight" and etype2 == "Psychic"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Fight" and etype1 == "Fairy" or type1 == "Fight" and etype2 == "Fairy") or (type2 == "Fight" and etype1 == "Fairy" or type2 == "Fight" and etype2 == "Fairy"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Fight" and etype1 == "Normal" or type1 == "Fight" and etype2 == "Normal") or (type2 == "Fight" and etype1 == "Normal" or type2 == "Fight" and etype2 == "Normal"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Fight" and etype1 == "Rock" or type1 == "Fight" and etype2 == "Rock") or (type2 == "Fight" and etype1 == "Rock" or type2 == "Fight" and etype2 == "Rock"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Fight" and etype1 == "Steel" or type1 == "Fight" and etype2 == "Steel") or (type2 == "Fight" and etype1 == "Steel" or type2 == "Fight" and etype2 == "Steel"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

#Flying
elif (type1 == "Flying" and etype1 == "Rock" or type1 == "Flying" and etype2 == "Rock") or (type2 == "Flying" and etype1 == "Rock" or type2 == "Flying" and etype2 == "Rock"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Flying" and etype1 == "Steel" or type1 == "Flying" and etype2 == "Steel") or (type2 == "Flying" and etype1 == "Steel" or type2 == "Flying" and etype2 == "Steel"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Flying" and etype1 == "Electric" or type1 == "Flying" and etype2 == "Electric") or (type2 == "Flying" and etype1 == "Electric" or type2 == "Flying" and etype2 == "Electric"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Flying" and etype1 == "Fight" or type1 == "Flying" and etype2 == "Fight") or (type2 == "Flying" and etype1 == "Fight" or type2 == "Flying" and etype2 == "Fight"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Flying" and etype1 == "Bug" or type1 == "Flying" and etype2 == "Bug") or (type2 == "Flying" and etype1 == "Bug" or type2 == "Flying" and etype2 == "Bug"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Flying" and etype1 == "Grass" or type1 == "Flying" and etype2 == "Grass") or (type2 == "Flying" and etype1 == "Grass" or type2 == "Flying" and etype2 == "Grass"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

#Poison
elif (type1 == "Posion" and etype1 == "Steel" or type1 == "Posion" and etype2 == "Steel") or (type2 == "Posion" and etype1 == "Steel" or type2 == "Posion" and etype2 == "Steel"):
    typeadvdmg = 0

elif (type1 == "Posion" and etype1 == "Posion" or type1 == "Posion" and etype2 == "Posion") or (type2 == "Posion" and etype1 == "Posion" or type2 == "Posion" and etype2 == "Posion"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Posion" and etype1 == "Ground" or type1 == "Posion" and etype2 == "Ground") or (type2 == "Posion" and etype1 == "Ground" or type2 == "Posion" and etype2 == "Ground"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Posion" and etype1 == "Rock" or type1 == "Posion" and etype2 == "Rock") or (type2 == "Posion" and etype1 == "Rock" or type2 == "Posion" and etype2 == "Rock"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Posion" and etype1 == "Ghost" or type1 == "Posion" and etype2 == "Ghost") or (type2 == "Posion" and etype1 == "Ghost" or type2 == "Posion" and etype2 == "Ghost"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Posion" and etype1 == "Grass" or type1 == "Posion" and etype2 == "Grass") or (type2 == "Posion" and etype1 == "Grass" or type2 == "Posion" and etype2 == "Grass"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Posion" and etype1 == "Fairy" or type1 == "Posion" and etype2 == "Fairy") or (type2 == "Posion" and etype1 == "Fairy" or type2 == "Posion" and etype2 == "Fairy"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

#Ground
elif (type1 == "Ground" and etype1 == "Flying" or type1 == "Ground" and etype2 == "Flying") or (type2 == "Ground" and etype1 == "Flying" or type2 == "Ground" and etype2 == "Flying"):
    typeadvdmg = 0

elif (type1 == "Ground" and etype1 == "Bug" or type1 == "Ground" and etype2 == "Bug") or (type2 == "Ground" and etype1 == "Bug" or type2 == "Ground" and etype2 == "Bug"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Ground" and etype1 == "Grass" or type1 == "Ground" and etype2 == "Grass") or (type2 == "Ground" and etype1 == "Grass" or type2 == "Ground" and etype2 == "Grass"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Ground" and etype1 == "Posion" or type1 == "Ground" and etype2 == "Posion") or (type2 == "Ground" and etype1 == "Posion" or type2 == "Ground" and etype2 == "Posion"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Ground" and etype1 == "Rock" or type1 == "Ground" and etype2 == "Rock") or (type2 == "Ground" and etype1 == "Rock" or type2 == "Ground" and etype2 == "Rock"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Ground" and etype1 == "Steel" or type1 == "Ground" and etype2 == "Steel") or (type2 == "Ground" and etype1 == "Steel" or type2 == "Ground" and etype2 == "Steel"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Ground" and etype1 == "Fire" or type1 == "Ground" and etype2 == "Fire") or (type2 == "Ground" and etype1 == "Fire" or type2 == "Ground" and etype2 == "Fire"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Ground" and etype1 == "Electric" or type1 == "Ground" and etype2 == "Electric") or (type2 == "Ground" and etype1 == "Electric" or type2 == "Ground" and etype2 == "Electric"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

#Rock
elif (type1 == "Rock" and etype1 == "Fight" or type1 == "Rock" and etype2 == "Fight") or (type2 == "Rock" and etype1 == "Fight" or type2 == "Rock" and etype2 == "Fight"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Rock" and etype1 == "Ground" or type1 == "Rock" and etype2 == "Ground") or (type2 == "Rock" and etype1 == "Ground" or type2 == "Rock" and etype2 == "Ground"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Rock" and etype1 == "Steel" or type1 == "Rock" and etype2 == "Steel") or (type2 == "Rock" and etype1 == "Steel" or type2 == "Rock" and etype2 == "Steel"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Rock" and etype1 == "Flying" or type1 == "Rock" and etype2 == "Flying") or (type2 == "Rock" and etype1 == "Flying" or type2 == "Rock" and etype2 == "Flying"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Rock" and etype1 == "Bug" or type1 == "Rock" and etype2 == "Bug") or (type2 == "Rock" and etype1 == "Bug" or type2 == "Rock" and etype2 == "Bug"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Rock" and etype1 == "Fire" or type1 == "Rock" and etype2 == "Fire") or (type2 == "Rock" and etype1 == "Fire" or type2 == "Rock" and etype2 == "Fire"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Rock" and etype1 == "Ice" or type1 == "Rock" and etype2 == "Ice") or (type2 == "Rock" and etype1 == "Ice" or type2 == "Rock" and etype2 == "Ice"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Rock" and etype1 == "Electric" or type1 == "Rock" and etype2 == "Electric") or (type2 == "Rock" and etype1 == "Electric" or type2 == "Rock" and etype2 == "Electric"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

#Bug
elif (type1 == "Bug" and etype1 == "Fight" or type1 == "Bug" and etype2 == "Fight") or (type2 == "Bug" and etype1 == "Fight" or type2 == "Bug" and etype2 == "Fight"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Bug" and etype1 == "Flying" or type1 == "Bug" and etype2 == "Flying") or (type2 == "Bug" and etype1 == "Flying" or type2 == "Bug" and etype2 == "Flying"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Bug" and etype1 == "Posion" or type1 == "Bug" and etype2 == "Posion") or (type2 == "Bug" and etype1 == "Posion" or type2 == "Bug" and etype2 == "Posion"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Bug" and etype1 == "Ghost" or type1 == "Bug" and etype2 == "Ghost") or (type2 == "Bug" and etype1 == "Ghost" or type2 == "Bug" and etype2 == "Ghost"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Bug" and etype1 == "Steel" or type1 == "Bug" and etype2 == "Steel") or (type2 == "Bug" and etype1 == "Steel" or type2 == "Bug" and etype2 == "Steel"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Bug" and etype1 == "Fire" or type1 == "Bug" and etype2 == "Fire") or (type2 == "Bug" and etype1 == "Fire" or type2 == "Bug" and etype2 == "Fire"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Bug" and etype1 == "Fairy" or type1 == "Bug" and etype2 == "Fairy") or (type2 == "Bug" and etype1 == "Fairy" or type2 == "Bug" and etype2 == "Fairy"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Bug" and etype1 == "Grass" or type1 == "Bug" and etype2 == "Grass") or (type2 == "Bug" and etype1 == "Grass" or type2 == "Bug" and etype2 == "Grass"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Bug" and etype1 == "Psychic" or type1 == "Bug" and etype2 == "Psychic") or (type2 == "Bug" and etype1 == "Psychic" or type2 == "Bug" and etype2 == "Psychic"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Bug" and etype1 == "Dark" or type1 == "Bug" and etype2 == "Dark") or (type2 == "Bug" and etype1 == "Dark" or type2 == "Bug" and etype2 == "Dark"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

#Ghost
elif (type1 == "Ghost" and etype1 == "Normal" or type1 == "Ghost" and etype2 == "Normal") or (type2 == "Ghost" and etype1 == "Normal" or type2 == "Ghost" and etype2 == "Normal"):
    typeadvdmg = 0

elif (type1 == "Ghost" and etype1 == "Dark" or type1 == "Ghost" and etype2 == "Dark") or (type2 == "Ghost" and etype1 == "Dark" or type2 == "Ghost" and etype2 == "Dark"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Ghost" and etype1 == "Ghost" or type1 == "Ghost" and etype2 == "Ghost") or (type2 == "Ghost" and etype1 == "Ghost" or type2 == "Ghost" and etype2 == "Ghost"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Ghost" and etype1 == "Psychic" or type1 == "Ghost" and etype2 == "Psychic") or (type2 == "Ghost" and etype1 == "Psychic" or type2 == "Ghost" and etype2 == "Psychic"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

#Steel
elif (type1 == "Steel" and etype1 == "Steel" or type1 == "Steel" and etype2 == "Steel") or (type2 == "Steel" and etype1 == "Steel" or type2 == "Steel" and etype2 == "Steel"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Steel" and etype1 == "Fire" or type1 == "Steel" and etype2 == "Fire") or (type2 == "Steel" and etype1 == "Fire" or type2 == "Steel" and etype2 == "Fire"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Steel" and etype1 == "Water" or type1 == "Steel" and etype2 == "Water") or (type2 == "Steel" and etype1 == "Water" or type2 == "Steel" and etype2 == "Water"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Steel" and etype1 == "Electric" or type1 == "Steel" and etype2 == "Electric") or (type2 == "Steel" and etype1 == "Electric" or type2 == "Steel" and etype2 == "Electric"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Steel" and etype1 == "Rock" or type1 == "Steel" and etype2 == "Rock") or (type2 == "Steel" and etype1 == "Rock" or type2 == "Steel" and etype2 == "Rock"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Steel" and etype1 == "Ice" or type1 == "Steel" and etype2 == "Ice") or (type2 == "Steel" and etype1 == "Ice" or type2 == "Steel" and etype2 == "Ice"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Steel" and etype1 == "Fairy" or type1 == "Steel" and etype2 == "Fairy") or (type2 == "Steel" and etype1 == "Fairy" or type2 == "Steel" and etype2 == "Fairy"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

#Fire
elif (type1 == "Fire" and etype1 == "Rock" or type1 == "Fire" and etype2 == "Rock") or (type2 == "Fire" and etype1 == "Rock" or type2 == "Fire" and etype2 == "Rock"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Fire" and etype1 == "Fire" or type1 == "Fire" and etype2 == "Fire") or (type2 == "Fire" and etype1 == "Fire" or type2 == "Fire" and etype2 == "Fire"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Fire" and etype1 == "Water" or type1 == "Fire" and etype2 == "Water") or (type2 == "Fire" and etype1 == "Water" or type2 == "Fire" and etype2 == "Water"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Fire" and etype1 == "Dragon" or type1 == "Fire" and etype2 == "Dragon") or (type2 == "Fire" and etype1 == "Dragon" or type2 == "Fire" and etype2 == "Dragon"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Fire" and etype1 == "Bug" or type1 == "Fire" and etype2 == "Bug") or (type2 == "Fire" and etype1 == "Bug" or type2 == "Fire" and etype2 == "Bug"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Fire" and etype1 == "Steel" or type1 == "Fire" and etype2 == "Steel") or (type2 == "Fire" and etype1 == "Steel" or type2 == "Fire" and etype2 == "Steel"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0
        
elif (type1 == "Fire" and etype1 == "Grass" or type1 == "Fire" and etype2 == "Grass") or (type2 == "Fire" and etype1 == "Grass" or type2 == "Fire" and etype2 == "Grass"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0
        
elif (type1 == "Fire" and etype1 == "Ice" or type1 == "Fire" and etype2 == "Ice") or (type2 == "Fire" and etype1 == "Ice" or type2 == "Fire" and etype2 == "Ice"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

#Water
elif (type1 == "Water" and etype1 == "Water" or type1 == "Water" and etype2 == "Water") or (type2 == "Water" and etype1 == "Water" or type2 == "Water" and etype2 == "Water"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Water" and etype1 == "Grass" or type1 == "Water" and etype2 == "Grass") or (type2 == "Water" and etype1 == "Grass" or type2 == "Water" and etype2 == "Grass"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Water" and etype1 == "Dragon" or type1 == "Water" and etype2 == "Dragon") or (type2 == "Water" and etype1 == "Dragon" or type2 == "Water" and etype2 == "Dragon"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5
elif (type1 == "Water" and etype1 == "Ground" or type1 == "Water" and etype2 == "Ground") or (type2 == "Water" and etype1 == "Ground" or type2 == "Water" and etype2 == "Ground"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Water" and etype1 == "Rock" or type1 == "Water" and etype2 == "Rock") or (type2 == "Water" and etype1 == "Rock" or type2 == "Water" and etype2 == "Rock"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Water" and etype1 == "Fire" or type1 == "Water" and etype2 == "Fire") or (type2 == "Water" and etype1 == "Fire" or type2 == "Water" and etype2 == "Fire"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

#Grass
elif (type1 == "Grass" and etype1 == "Flying" or type1 == "Grass" and etype2 == "Flying") or (type2 == "Grass" and etype1 == "Flying" or type2 == "Grass" and etype2 == "Flying"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Grass" and etype1 == "Poison" or type1 == "Grass" and etype2 == "Poison") or (type2 == "Grass" and etype1 == "Poison" or type2 == "Grass" and etype2 == "Poison"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Grass" and etype1 == "Bug" or type1 == "Grass" and etype2 == "Bug") or (type2 == "Grass" and etype1 == "Bug" or type2 == "Grass" and etype2 == "Bug"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Grass" and etype1 == "Steel" or type1 == "Grass" and etype2 == "Steel") or (type2 == "Grass" and etype1 == "Steel" or type2 == "Grass" and etype2 == "Steel"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Grass" and etype1 == "Fire" or type1 == "Grass" and etype2 == "Fire") or (type2 == "Grass" and etype1 == "Fire" or type2 == "Grass" and etype2 == "Fire"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Grass" and etype1 == "Grass" or type1 == "Grass" and etype2 == "Grass") or (type2 == "Grass" and etype1 == "Grass" or type2 == "Grass" and etype2 == "Grass"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Grass" and etype1 == "Dragon" or type1 == "Grass" and etype2 == "Dragon") or (type2 == "Grass" and etype1 == "Dragon" or type2 == "Grass" and etype2 == "Dragon"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Grass" and etype1 == "Ground" or type1 == "Grass" and etype2 == "Ground") or (type2 == "Grass" and etype1 == "Ground" or type2 == "Grass" and etype2 == "Ground"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Grass" and etype1 == "Rock" or type1 == "Grass" and etype2 == "Rock") or (type2 == "Grass" and etype1 == "Rock" or type2 == "Grass" and etype2 == "Rock"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Grass" and etype1 == "Water" or type1 == "Grass" and etype2 == "Water") or (type2 == "Grass" and etype1 == "Water" or type2 == "Grass" and etype2 == "Water"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

#Electric
elif (type1 == "Electric" and etype1 == "Rock" or type1 == "Electric" and etype2 == "Rock") or (type2 == "Electric" and etype1 == "Rock" or type2 == "Electric" and etype2 == "Rock"):
    typeadvdmg = 0

elif (type1 == "Electric" and etype1 == "Grass" or type1 == "Electric" and etype2 == "Grass") or (type2 == "Electric" and etype1 == "Grass" or type2 == "Electric" and etype2 == "Grass"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Electric" and etype1 == "Electric" or type1 == "Electric" and etype2 == "Electric") or (type2 == "Electric" and etype1 == "Electric" or type2 == "Electric" and etype2 == "Electric"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Electric" and etype1 == "Dragon" or type1 == "Electric" and etype2 == "Dragon") or (type2 == "Electric" and etype1 == "Dragon" or type2 == "Electric" and etype2 == "Dragon"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5


elif (type1 == "Electric" and etype1 == "Flying" or type1 == "Electric" and etype2 == "Flying") or (type2 == "Electric" and etype1 == "Flying" or type2 == "Electric" and etype2 == "Flying"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Electric" and etype1 == "Water" or type1 == "Electric" and etype2 == "Water") or (type2 == "Electric" and etype1 == "Water" or type2 == "Electric" and etype2 == "Water"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

#Psychic
elif (type1 == "Psychic" and etype1 == "Dark" or type1 == "Psychic" and etype2 == "Dark") or (type2 == "Psychic" and etype1 == "Dark" or type2 == "Psychic" and etype2 == "Dark"):
    typeadvdmg = 0

elif (type1 == "Psychic" and etype1 == "Steel" or type1 == "Psychic" and etype2 == "Steel") or (type2 == "Psychic" and etype1 == "Steel" or type2 == "Psychic" and etype2 == "Steel"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Psychic" and etype1 == "Psychic" or type1 == "Psychic" and etype2 == "Psychic") or (type2 == "Psychic" and etype1 == "Psychic" or type2 == "Psychic" and etype2 == "Psychic"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Psychic" and etype1 == "Fight" or type1 == "Psychic" and etype2 == "Fight") or (type2 == "Psychic" and etype1 == "Fight" or type2 == "Psychic" and etype2 == "Fight"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Psychic" and etype1 == "Poison" or type1 == "Psychic" and etype2 == "Poison") or (type2 == "Psychic" and etype1 == "Poison" or type2 == "Psychic" and etype2 == "Poison"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

#Ice
elif (type1 == "Ice" and etype1 == "Steel" or type1 == "Ice" and etype2 == "Steel") or (type2 == "Ice" and etype1 == "Steel" or type2 == "Ice" and etype2 == "Steel"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Ice" and etype1 == "Fire" or type1 == "Ice" and etype2 == "Fire") or (type2 == "Ice" and etype1 == "Fire" or type2 == "Ice" and etype2 == "Fire"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Ice" and etype1 == "Water" or type1 == "Ice" and etype2 == "Water") or (type2 == "Ice" and etype1 == "Water" or type2 == "Ice" and etype2 == "Water"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Ice" and etype1 == "Ice" or type1 == "Ice" and etype2 == "Ice") or (type2 == "Ice" and etype1 == "Ice" or type2 == "Ice" and etype2 == "Ice"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Ice" and etype1 == "Flying" or type1 == "Ice" and etype2 == "Flying") or (type2 == "Ice" and etype1 == "Flying" or type2 == "Ice" and etype2 == "Flying"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Ice" and etype1 == "Ground" or type1 == "Ice" and etype2 == "Ground") or (type2 == "Ice" and etype1 == "Ground" or type2 == "Ice" and etype2 == "Ground"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Ice" and etype1 == "Grass" or type1 == "Ice" and etype2 == "Grass") or (type2 == "Ice" and etype1 == "Grass" or type2 == "Ice" and etype2 == "Grass"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Ice" and etype1 == "Dragon" or type1 == "Ice" and etype2 == "Dragon") or (type2 == "Ice" and etype1 == "Dragon" or type2 == "Ice" and etype2 == "Dragon"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

#Dragon
elif (type1 == "Dragon" and etype1 == "Fairy" or type1 == "Dragon" and etype2 == "Fairy") or (type2 == "Dragon" and etype1 == "Fairy" or type2 == "Dragon" and etype2 == "Fairy"):
    typeadvdmg = 0

elif (type1 == "Dragon" and etype1 == "Steel" or type1 == "Dragon" and etype2 == "Steel") or (type2 == "Dragon" and etype1 == "Steel" or type2 == "Dragon" and etype2 == "Steel"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Dragon" and etype1 == "Dragon" or type1 == "Dragon" and etype2 == "Dragon") or (type2 == "Dragon" and etype1 == "Dragon" or type2 == "Dragon" and etype2 == "Dragon"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

#Dark
elif (type1 == "Dark" and etype1 == "Fight" or type1 == "Dark" and etype2 == "Fight") or (type2 == "Dark" and etype1 == "Fight" or type2 == "Dark" and etype2 == "Fight"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Dark" and etype1 == "Dark" or type1 == "Dark" and etype2 == "Dark") or (type2 == "Dark" and etype1 == "Dark" or type2 == "Dark" and etype2 == "Dark"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Dark" and etype1 == "Fairy" or type1 == "Dark" and etype2 == "Fairy") or (type2 == "Dark" and etype1 == "Fairy" or type2 == "Dark" and etype2 == "Fairy"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Dark" and etype1 == "Ghost" or type1 == "Dark" and etype2 == "Ghost") or (type2 == "Dark" and etype1 == "Ghost" or type2 == "Dark" and etype2 == "Ghost"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Dark" and etype1 == "Psychic" or type1 == "Dark" and etype2 == "Psychic") or (type2 == "Dark" and etype1 == "Psychic" or type2 == "Dark" and etype2 == "Psychic"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

#Fairy
elif (type1 == "Fairy" and etype1 == "Posion" or type1 == "Fairy" and etype2 == "Posion") or (type2 == "Fairy" and etype1 == "Posion" or type2 == "Fairy" and etype2 == "Posion"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Fairy" and etype1 == "Steel" or type1 == "Fairy" and etype2 == "Steel") or (type2 == "Fairy" and etype1 == "Steel" or type2 == "Fairy" and etype2 == "Steel"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Fairy" and etype1 == "Fire" or type1 == "Fairy" and etype2 == "Fire") or (type2 == "Fairy" and etype1 == "Fire" or type2 == "Fairy" and etype2 == "Fire"):
    if targets == "Yes":
        typeadvdmg = 0.25
    else:
        typeadvdmg = 0.5

elif (type1 == "Fairy" and etype1 == "Fight" or type1 == "Fairy" and etype2 == "Fight") or (type2 == "Fairy" and etype1 == "Fight" or type2 == "Fairy" and etype2 == "Fight"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Fairy" and etype1 == "Dragon" or type1 == "Fairy" and etype2 == "Dragon") or (type2 == "Fairy" and etype1 == "Dragon" or type2 == "Fairy" and etype2 == "Dragon"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

elif (type1 == "Fairy" and etype1 == "Dark" or type1 == "Fairy" and etype2 == "Dark") or (type2 == "Fairy" and etype1 == "Dark" or type2 == "Fairy" and etype2 == "Dark"):
    if targets == "Yes":
        typeadvdmg = 2.0
    else:
        typeadvdmg = 4.0

#Weather Damage Multiplier
if weather == "Normal":
    weatherdmg = 1

elif weather == "Harsh Sunlight":

    if type1 == "Fire" or type2 == "Fire":
    	weatherdmg = 1.5

    elif type1 == "Water" or type2 == "Water":
	    weatherdmg = 0.5

elif weather == "Rain" or weather == "Heavy Rain":

    if type1 == "Water" or type2 == "Water":
	    weatherdmg = 1.5

    elif type1 == "Fire" or type2 == "Fire":
	    weatherdmg = 0.5

elif weather == "Sandstorm":

    if type1 == "Rock" or type2 == "Rock" or type1 == "Steel" or type2 == "Steel" or type1 == "Ground" or type2 == "Ground":
        weatherdmg = 1.5

    else:
        weatherdmg = 0.5

elif weather == "Hail" or weather == "Diamond Dust":

    if type1 == "Ice" or type2 == "Ice":
        weatherdmg = 1.5
    else:
        weatherdmg = 0.5

elif weather == "Shadowy Aura":

    if type1 == "Ghost" or type2 == "Ghost" or type1 == "Dark" or type2 == "Dark":
        weatherdmg = 1.5
    else:
        weatherdmg = 0.5

elif weather == "Fog":

    if type1 == "Fairy" or type2 == "Fairy" or type1 == "Ghost" or type2 == "Ghost":
        weatherdmg = 1.5

    elif type1 == "Psychic" or type2 == "Psychic":
        weatherdmg = 0.5


elif weather == "Strong Winds":

    if type1 == "Flying" or type2 == "Flying": #<-- If receiving attack is Super Effective turn in Normal Effective.
        weatherdmg = 1.5













#Atk Modifier Computation
mod = targetdmg * weatherdmg * badgedmg * critdmg * randomdmg * stabdmg * typeadvdmg

#Grand Damage Total Computation
totdmg = ((2 * level / 5 + 2) * pwr * patk / pdef / 50 + 2) * mod



#Damage Output
print(atkname,('a Lvl.'),level,('('),type1,('/'),type2,(')'),('pokemon'),('dealt a total damage of'),format(totdmg,".2f"),('to a'),('a Lvl.'),level,defname)

#Effectiveness Note
if typeadvdmg == 0:
	print('and its not effective.')
elif typeadvdmg <= 0.5:
	print('and its not very effective.')
elif typeadvdmg <= 1:
    print('which is a normal effective')
else:
	print('and its very effective!')

#Computation Checker
#print('Weather Multiplier:',weatherdmg)
#print('Badge Multiplier:',badgedmg)
#print('Critical Multiplier:',critdmg)
#print('RNG Multiplier:',randomdmg)
#print('STAB Multiplier:',stabdmg)
#print('Type Multiplier:',typeadvdmg)
#print('Burn Multiplier:',burneddmg)
#print('Target Multiplier:',targetdmg)