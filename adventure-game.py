# Michael Becker - adventure-game.py

from random import *
import datetime
today = datetime.date.today()

# Use Gold to upgrade your weapon or buy Med Packs to increase depleted health
charGold = 200
# You lose the game when Health reaches 0
charHealth = 100
# Med Packs increase your Health by 50 and are a one-time use
charMedPacks = 3
# Weapon is a multiplier for random attack values
charWeapon = 1
# Goal is to gather as many artifacts as possible for the Library of Alexandria
charArtifacts = 0

print("Alexandria, Egypt - the year 325 BC\n-----")

charName = input("Enter your character's name: ")
print("Hello",charName + ". You have been appointed by Queen Cleopatra to sail the Nile River and gather artifacts for the Library of Alexandria.")
print("It will be a dangerous journey: aggressive animals, bandits, unforgiving nature, and more...\nYou may also encounter trading posts, medics, and weapon shops along the way.\n")

print("Your character will begin this journey with gold, health packs, and weapons based on the character attribute you select below:")
print("(C)onqueror: You don't allow anyone to stand in your way. You begin with a strong weapon but less gold.")
print("(S)cout: You are a strong navigator with medium amounts of gold and a decent weapon.")
print("(D)efender: You have excellent health endurance and your weapon is okay, but not great.")
print("(N)egotiator: You have a weak weapon that can be quickly improved because of your large amount of gold.")
print()
charAtt = (input("Select your preferred attribute: ")).lower()

if charAtt == "c":
    charGold = 150
    charWeapon = 2
if charAtt == "s":
    charMedPacks = 4
    charWeapon = 1.5
if charAtt == "d":
    charHealth = 200
    charMedPacks = 4
elif charAtt == "n":
    charGold = 300
    charWeapon = 0.75
else:
    charAtt = (input("ERROR - Select (C), (S), (D), or (N): ")).lower()
    if charAtt == "c":
        charGold = 150
        charWeapon = 2
    if charAtt == "s":
        charMedPacks = 4
        charWeapon = 1.5
    if charAtt == "d":
        charHealth = 200
        charMedPacks = 4
    elif charAtt == "n":
        charGold = 300
        charWeapon = 0.75
if charAtt == "c":
    print("You have selected Conqueror!")
    charProfile = "Conqueror"
if charAtt == "s":
    print("You have selected Scout!")
    charProfile = "Scout"
if charAtt == "d":
    print("You have selected Defender!")
    charProfile = "Defender"
elif charAtt == "n":
    print("You have selected Negotiator!")
    charProfile = "Negotiator"

print()
print("Your starting attributes are : {} Gold, {} Health, {} Med Packs, {} Weapon Strength".format(charGold,charHealth,charMedPacks,charWeapon))
input("Hit enter to begin your journey...")
print()

print("--- Day One ---")
input("It is early in the morning. The sun has not even began to rise. Begin boarding your felucca (sail boat) at the docks of Alexandria.")
print()
randomEvent = randrange(1,5)
if randomEvent == 1:
    charGold = charGold - 10
    print("Your felucca had a tear in the sail. After only a slight delay, your sail was repaired by a local seamstress. (-10 Gold)\nYou now have {} Gold.".format(charGold))
    input("Hit enter to finish loading your felucca and depart up the Nile.")
else:
    input("Your felucca is fully loaded with your gold, med packs, and weapon! You begin sailing down the Nile River.")
print()
charChoice = (input("Shortly after departure, you notice a small abandoned hut on the shoreline. Would you like to stop and explore it? (y/n): ")).lower()
if charChoice == "y":
    randomEvent = randrange(1,4)
    if randomEvent == 1:
        charArtifacts = charArtifacts + 1
        input("You have discovered a canopic jar. Wonder what's inside?? (+1 Artifact)\nYou now have {} Artifacts.".format(charArtifacts))
    if randomEvent == 2:
        print("You have encountered Pirate Amsu who was counting his stolen gold from the nearby city of Giza.")
        pirateHealth = 30
        pirateWeapon = 1
        print("Amsu's Health: {}, Weapon Level: {}".format(pirateHealth,pirateWeapon))
        print()
        input("Hit enter to begin your attack!")
        attackCount = 1
        while pirateHealth > 0:
            charAttack = randrange(1,11) * charWeapon
            pirateHealth = pirateHealth - charAttack
            if pirateHealth > 0:
                print("Attack {}: You caused {} damage. Remaining enemy health: {}.".format(attackCount,charAttack,pirateHealth))
            if pirateHealth <= 0:
                break
            print("Pirate Amsu attacks back!")
            pirateAttack = randrange(1,11) * pirateWeapon
            charHealth = charHealth - pirateAttack
            if charHealth > 0:
                print("Pirate Amsu caused {} damage. Remaining health: {}.".format(pirateAttack,charHealth))
            if charHealth <= 0:
                print("Your health has been depleted. You have lost the game.")
                exit()
            print()
            useMedPack = (input("Use a Med Pack (restores 50 Health)? (y/n) ").lower())
            if useMedPack == "y":
                if charMedPacks > 0:
                    charHealth = charHealth + 50
                    charMedPacks = charMedPacks - 1
                    print("Your health is now {}. You have {} med packs remaining.".format(charHealth,charMedPacks))
                else:
                    print("You do not have any Med Packs!")
            input("Hit enter to attack again!")
            print()
            attackCount = attackCount + 1
        print("You have defeated Pirate Amsu! Your remaining health is {}. You also gain an Artifact and 50 Gold as a token of your victory!".format(charHealth))
        charGold = charGold + 50
        useMedPack = (input("Do you need to use a Med Pack (restores 50 Health)? (y/n) ")).lower()
        if useMedPack == "y":
            if charMedPacks > 0:
                charHealth = charHealth + 50
                charMedPacks = charMedPacks - 1
                print("Your health is now {}. You have {} med packs remaining.".format(charHealth,charMedPacks))
            else:
                print("You do not have any Med Packs!")
    if randomEvent == 3:
        print("It was empty... Hopefully we will find something soon!")
else:
    print("You skipped this investigation. You may have missed out on an artifact or gold, but you also may have avoided conflict.")
input("Hit enter to continue to the next day...")
print()

print("--- Day Two ---")
print("You arrive in Giza and explore the local markets around the Great Pyramids and Sphinx. You meet Seth, a blacksmith, who offers to improve your weapon for a steep price. He is up to negotiation though!")
negotiation = (input("Enter negotiations? (y/n) ")).lower()
print()
if negotiation == "y":
    sethOffer = 100
    print("Seth offers weapon enhancements (+ 0.25 weapon level) for 100 Gold. Your current gold is {}".format(charGold))
    initialOffer = int(input("Enter your proposed amount to negotiate: "))
    if initialOffer >= 50:
        sethOffer = randrange(initialOffer+5,100,5)
        print("Seth thinks about it but rejects your proposals. He offers a counter: {}".format(sethOffer))
        counterAccept = (input("Do you accept his counter offer? (y/n) ")).lower()
        if counterAccept == "y":
            charWeapon = charWeapon + 0.25
            charGold = charGold - sethOffer
            if charGold > 0:
                input("Thank you for your purchase. Weapon strength: {}, Gold: {}".format(charWeapon,charGold))
            else:
                input("You do not have enough gold. You miss out on the chance to upgrade your weapon!")
        else:
            print("You can negotiate one more time.")
            nextOffer = int(input("What is your next offer? "))
            if nextOffer > initialOffer:
                charWeapon = charWeapon + 0.25
                charGold = charGold - nextOffer
                if charGold > 0:
                    input("Seth accepts your offer of {} Gold. Your weapon is now at {} strength! Remaining gold is {}.".format(nextOffer,charWeapon,charGold))
                    print()
                else:
                    input("You do not have enough gold. You miss out on the chance to upgrade your weapon!")
                    print()
            else:
                input("You do not know how to negotiate! Seth has rejected your offer and invites you to leave his shop.")
                print()
    if initialOffer < 50:
        print("Seth is not happy with your offer.  You must not trust his blacksmith skills!")
        input("His sword is suddenly drawn and a battle has begun!")
        sethHealth = 50
        sethWeapon = 1.5
        print("Seth's Health: {}, Weapon Level: {}".format(sethHealth,sethWeapon))
        print()
        input("Hit enter to attack!")
        attackCount = 1
        while sethHealth > 0:
            charAttack = randrange(1,11) * charWeapon
            sethHealth = sethHealth - charAttack
            if sethHealth > 0:
                print("Attack {}: You caused {} damage. Remaining enemy health: {}.".format(attackCount,charAttack,sethHealth))
            if sethHealth <= 0:
                break
            print("Seth counters your attack!")
            sethAttack = randrange(1,11) * sethWeapon
            charHealth = charHealth - sethAttack
            if charHealth > 0:
                print("Seth caused {} damage. Remaining health: {}.".format(sethAttack,charHealth))
            if charHealth <= 0:
                print("Your health has been depleted. You have lost the game.")
                exit()
            print()
            useMedPack = (input("Use a Med Pack (restores 50 Health)? (y/n) ").lower())
            if useMedPack == "y":
                if charMedPacks > 0:
                    charHealth = charHealth + 50
                    charMedPacks = charMedPacks - 1
                    print("Your health is now {}. You have {} med packs remaining.".format(charHealth,charMedPacks))
                else:
                    print("You do not have any Med Packs!")
            input("Hit enter to attack again!")
            print()
            attackCount = attackCount + 1
        print("You have defeated Seth! Your remaining health is {}. You also steal his most prized weapon enhancement, mounted on the wall!".format(charHealth))
        charWeapon = charWeapon + 0.5
        print("Your new weapon level is {}.".format(charWeapon))
        useMedPack = (input("Use a Med Pack (restores 50 Health)? (y/n) ").lower())
        if useMedPack == "y":
            if charMedPacks > 0:
                charHealth = charHealth + 50
                charMedPacks = charMedPacks - 1
                print("Your health is now {}. You have {} med packs remaining.".format(charHealth,charMedPacks))
            else:
                print("You do not have any Med Packs!")
else:
    print("You save your gold and continue to explore Giza. Your weapon level is {}.".format(charWeapon))
print()

print("--- Later That Night... ---")
print("You decide to sneak over to the pyramids while everyone is sleeping. The entrance door is locked and requires a three-digit code to get in.")
print("The code uses the numbers 1 and 0 in any sort of combination. Both numbers do not have to be used.\n")
secretCodeOne = randrange(0,2)
secretCodeTwo = randrange(0,2)
secretCodeThree = randrange(0,2)

secretCode = "{}{}{}".format(secretCodeOne,secretCodeTwo,secretCodeThree)

userCode = str(input("Enter your three-digit code using only 1's and 0's: "))
print()
while userCode != "q":
    while userCode != secretCode:
        print("Your code is incorrect.")
        userCode = str(input("Enter another code or type q to quit: " ))
        if userCode == "q":
            break
    if userCode != "q":
        print("You have guessed the correct code! The door suddenly opens and you venture inside the pyramid.\nYou begin stepping down the dark, winding stairs and reach a large open room.  There is a small light in the middle of the room.")
        approachLight = (input("Do you want to approach the small light? (y/n) ")).lower()
        if approachLight == "y":
            randomEvent = randrange(1,4)
            if randomEvent == 3:
                print("You take a few steps forward and suddenly Anubis the Jackal darts out of the shadows towards you!")
                jackalHealth = 75
                jackalWeapon = 1.5
                print("Anubis the Jackal's Health: {}, Weapon Level: {}".format(jackalHealth,jackalWeapon))
                print()
                input("Hit enter to attack!")
                attackCount = 1
                while jackalHealth > 0:
                    charAttack = randrange(1,11) * charWeapon
                    jackalHealth = jackalHealth - charAttack
                    if jackalHealth > 0:
                        print("Attack {}: You caused {} damage. Remaining enemy health: {}.".format(attackCount,charAttack,jackalHealth))
                    if jackalHealth <= 0:
                        break
                    print("Anubis the Jackal strikes back!")
                    jackalAttack = randrange(1,11) * jackalWeapon
                    charHealth = charHealth - jackalAttack
                    if charHealth > 0:
                        print("Anubis the Jackal caused {} damage. Remaining health: {}.".format(jackalAttack,charHealth))
                    if charHealth <= 0:
                        print("Your health has been depleted. You have lost the game.")
                        exit()
                    print()
                    useMedPack = (input("Use a Med Pack (restores 50 Health)? (y/n) ").lower())
                    if useMedPack == "y":
                        if charMedPacks > 0:
                            charHealth = charHealth + 50
                            charMedPacks = charMedPacks - 1
                            print("Your health is now {}. You have {} med packs remaining.".format(charHealth,charMedPacks))
                        else:
                            print("You do not have any Med Packs!")
                    input("Hit enter to attack again!")
                    print()
                    attackCount = attackCount + 1
                input("You have defeated Anubis the Jackal! Your remaining health is {}. You also find his guarded treasure: the Pharoah's golden mask (+1 Artifact)".format(charHealth))
                charArtifacts = charArtifacts + 1
                useMedPack = (input("Do you need to use a Med Pack (restores 50 Health)? (y/n) ")).lower()
                if useMedPack == "y":
                    if charMedPacks > 0:
                        charHealth = charHealth + 50
                        charMedPacks = charMedPacks - 1
                        print("Your health is now {}. You have {} med packs remaining.".format(charHealth,charMedPacks))
                    else:
                        print("You do not have any Med Packs!")
            else:
                print("You found the Pharoah's golden mask! (+1 Artifact)")
                charArtifacts = charArtifacts + 1
        userCode = "q"
input("You make it back to your campsite and get some rest for the journey to continue in the morning.")
print()
print("--- Day Three ---")
print("You have {} artifacts and are hoping to find a few more before you return to Alexandria!".format(charArtifacts))
input("Your current attributes are : {} Gold, {} Health, {} Med Packs, {} Weapon Strength".format(charGold,charHealth,charMedPacks,charWeapon))
print()
print("You continue sailing the Nile and notice a step pyramid off in the distance at the top of some sand dunes. You must be at Saqqara.\n")
userChoice = (input("Would you like to stop and explore the pyramid? (y/n) ")).lower()
if userChoice == "y":
    randomEvent = randrange(1,5)
    if randomEvent == 4:
        input("You wander the dunes for a while and are unable to find any artifacts. It is getting to be dark and you need to return to your felucca.")
        print()
    else:
        input("You wander the dunes for a while and find a chest full of amulets at the base of the step pyramid! (+1 Artifact)")
        charArtifacts = charArtifacts + 1
        print("You now have {} artifacts!".format(charArtifacts))
        print()
print("You return to your felucca and are about to begin a long journey to Luxor and the Valley of the Kings.")
input("Because this is a long trip, you can pay a local navigator to pilot your felucca (costs 25 gold) while you get much needed rest or you can pilot it yourself overnight but you risk losing health from exhaustion.")
print()
print("You currently have {} gold.".format(charGold))
userChoice = (input("Use a local navigator? (y/n) ")).lower()
if userChoice == "y":
    if charGold > 24:
        charGold = charGold - 25
        charHealth = charHealth + 25
        input("You trust the local navigator, pay him his fee, and get some much needed rest. (-25 gold, +25 health)")
    else:
        print("You do not have enough gold. You only have {} gold.".format(charGold))
        input("You will have to pilot the felucca yourself.")
else:
    print("You chose to pilot the felucca yourself.")
    useMedPack = (input("Would you like to use a Med Pack before departing (restores 50 Health)? (y/n) ")).lower()
    if useMedPack == "y":
        if charMedPacks > 0:
            charHealth = charHealth + 50
            charMedPacks = charMedPacks - 1
            print("Your health is now {}. You have {} med packs remaining.".format(charHealth,charMedPacks))
        else:
            print("You do not have any Med Packs!")
    randomEvent = randrange(1,4)
    if randomEvent == 3:
        charHealth = charHealth - 25
        if charHealth > 0:
            print()
            print("After piloting all night, you feel exhausted and have to spend extra time resting during the hot Egyptian day. (-25 health)")
            print("Your health is now at {}.".format(charHealth))
            useMedPack = (input("Do you need to use a Med Pack (restores 50 Health)? (y/n) ")).lower()
            if useMedPack == "y":
                if charMedPacks > 0:
                    charHealth = charHealth + 50
                    charMedPacks = charMedPacks - 1
                    print("Your health is now {}. You have {} med packs remaining.".format(charHealth,charMedPacks))
                else:
                    print("You do not have any Med Packs!")
        else:
            print("Your health has been depleted. You have lost the game. Be sure to utilize your med packs next time before departing!")
            exit()
print()
print("--- Day Four ---")
input("The Temple of Luxor is a bustling place full of local village peoples and other sailors like you. ")
print()
print("You have {} gold, {} health, and {} med packs.".format(charGold,charHealth,charMedPacks))
charChoice = (input("You visit a local merchant who sells med packs for 25 gold. Do you need to purchase any? (y/n) ")).lower()
if charChoice == "y":
    qtyToPurchase = int(input("How many med packs would you like to purchase? "))
    quote = 25 * qtyToPurchase
    if quote > charGold:
        input("You do not have enough gold to purchase the med packs.")
    else:
        charGold = charGold - quote
        charMedPacks = charMedPacks + qtyToPurchase
        print("The merchant thanks you for your purchase. You now have {} med packs and {} gold.".format(charMedPacks,charGold))
print()
input("As the sun sets, it casts long, dark shadows through the Temple of Luxor.\nYou need to find more artifacts and take advantage of the quiet village to explore on your own.")
print()
randomEvent = randrange(1,3)
if randomEvent == 2:
    print("Sitting on top of the temple is Horus the Falcon, a quick and agile beast who swoops down towards you!")
    falconHealth = 100
    falconWeapon = 1.5
    print("Horus the Falcon's Health: {}, Weapon Level: {}".format(falconHealth,falconWeapon))
    print()
    input("Hit enter to attack!")
    attackCount = 1
    while falconHealth > 0:
        charAttack = randrange(1,11) * charWeapon
        falconHealth = falconHealth - charAttack
        if falconHealth > 0:
            print("Attack {}: You caused {} damage. Remaining enemy health: {}.".format(attackCount,charAttack,falconHealth))
        if falconHealth <= 0:
            break
        print("Horus the Falcon swoops around for another attack!")
        falconAttack = randrange(1,11) * falconWeapon
        charHealth = charHealth - falconAttack
        if charHealth > 0:
            print("Horus the Falcon caused {} damage. Remaining health: {}.".format(falconAttack,charHealth))
        if charHealth <= 0:
            print("Your health has been depleted. You have lost the game.")
            exit()
        print()
        useMedPack = (input("Use a Med Pack (restores 50 Health)? (y/n) ").lower())
        if useMedPack == "y":
            if charMedPacks > 0:
                charHealth = charHealth + 50
                charMedPacks = charMedPacks - 1
                print("Your health is now {}. You have {} med packs remaining.".format(charHealth,charMedPacks))
            else:
                print("You do not have any Med Packs!")
        input("Hit enter to attack again!")
        print()
        attackCount = attackCount + 1
    input("You have defeated Horus the Falcon! Your remaining health is {}.".format(charHealth))
    useMedPack = (input("Do you need to use a Med Pack (restores 50 Health)? (y/n) ")).lower()
    if useMedPack == "y":
        if charMedPacks > 0:
            charHealth = charHealth + 50
            charMedPacks = charMedPacks - 1
            print("Your health is now {}. You have {} med packs remaining.".format(charHealth,charMedPacks))
        else:
            print("You do not have any Med Packs!")
print()
print("You peek into a dark room and notice a lit candle and a stack of papyrus, full of hieroglyphics.\nYou grab the papyrus and dart out of the room before being caught! (+1 Artifact)")
charArtifacts = charArtifacts + 1
print("You now have {} artifacts.".format(charArtifacts))
print()
userChoice = (input("Do you want to explore the temple a bit longer? (y/n) ")).lower()
if userChoice == "y":
    randomEvent = randrange(1,3)
    if randomEvent == 2:
        charGold = charGold + 100
        input("You head through a winding hallway and find a chest with 100 gold in it! (+100 Gold)")
    if randomEvent == 1:
        charArtifacts = charArtifacts + 1
        input("You head through a winding hallway and find a crook, a well known symbol of power! (+1 Artifact)")
print("You return to your felucca and admire your artifacts, ready for a good night's sleep.")
input("You have {} artifacts, {} gold, {} health, and {} med packs.".format(charArtifacts,charGold,charHealth,charMedPacks))
print()
print("--- Day Five ---")
print("You are on the final day of your journey and you reach the Temple of Ramesses near Abu Simbel!")
input("You are in search of the sarcophagus to complete your artifact collection.")
print()
print("Your remaining health is {}.".format(charHealth))
useMedPack = (input("Before entering the temple, do you need to use a Med Pack (restores 50 Health)? (y/n) ")).lower()
if useMedPack == "y":
    if charMedPacks > 0:
        charHealth = charHealth + 50
        charMedPacks = charMedPacks - 1
        print("Your health is now {}. You have {} med packs remaining.".format(charHealth,charMedPacks))
    else:
        print("You do not have any Med Packs!")
print("You enter the temple and are immediately attacked by the Osiris clan, protectors of the temple and all within!")
clanHealth = 100
clanWeapon = 2
print("Osiris clan's Health: {}, Weapon Level: {}".format(clanHealth,clanWeapon))
print()
input("Hit enter to attack!")
attackCount = 1
while clanHealth > 0:
    charAttack = randrange(1,11) * charWeapon
    clanHealth = clanHealth - charAttack
    if clanHealth > 0:
        print("Attack {}: You caused {} damage. Remaining enemy health: {}.".format(attackCount,charAttack,clanHealth))
    if clanHealth <= 0:
        break
    print("The Osiris clan must defend the temple and strikes back at you!")
    clanAttack = randrange(1,11) * clanWeapon
    charHealth = charHealth - clanAttack
    if charHealth > 0:
        print("The clan caused {} damage. Remaining health: {}.".format(clanAttack,charHealth))
    if charHealth <= 0:
        print("Your health has been depleted. You have lost the game.")
        exit()
    print()
    useMedPack = (input("Use a Med Pack (restores 50 Health)? (y/n) ").lower())
    if useMedPack == "y":
        if charMedPacks > 0:
            charHealth = charHealth + 50
            charMedPacks = charMedPacks - 1
            print("Your health is now {}. You have {} med packs remaining.".format(charHealth,charMedPacks))
        else:
            print("You do not have any Med Packs!")
    input("Hit enter to attack again!")
    print()
    attackCount = attackCount + 1
input("You have defeated the Osiris clan! Your remaining health is {}.".format(charHealth))
print()
print("The sarcophagus has been discovered because of your victory! (+1 Artifact)")
charArtifacts = charArtifacts + 1
input("You board your felucca and set sail back towards Alexandria with {} artifacts on board!".format(charArtifacts))
print()
print()
print("--- You have completed the game! ---")

finalScore = (charArtifacts * 1000) + (charGold * 10) + (charHealth * 10) + (charMedPacks * 100)
print("You completed the game with {} artifacts, {} gold, {} health, {} med packs, and a {} weapon strength.".format(charArtifacts,charGold,charHealth,charMedPacks,charWeapon))
print("Your final score is {}!".format(finalScore))
print()
print("Final Results:")
print("{:12} Score: {:6}   Date: {:14}   Character Type: {:10}".format(charName,finalScore,today.strftime("%b %d, %Y"),charProfile))
print()
print("Open the EgyptGameScoreboard.txt file to check out your past scores!")

scoreboardFile = open("EgyptGameScoreboard.txt","a")
print("{:12} Score: {:8}   Date: {:14}   Character Type: {:10}".format(charName,finalScore,today.strftime("%b %d, %Y"),charProfile), file=scoreboardFile)
scoreboardFile.close()