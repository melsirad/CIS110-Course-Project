print("Hello there! This is a story about a dog's world getting shaken up by a cat.")
print("I'll need to ask you a few questions before we get started!")
print("After typing your response, please press enter.")
input("\nPress the enter key to continue...")
print("\n")

catname = input("\nWhat is the cat's name?  ")
dogname = input("\nWhat is the dog's name?  ")
favfood = input("\nWhat is your favorite food?  ")
favbird = input("\nWhat is your favorite bird?  ")
number = input("\nWhat is your favorite number?  ")
ownername = input("\nWhat is your name?  ")



print("\nHere we go...")

print("\nThere once lived a happy dog named", dogname + ".")
print("Then one day", ownername, "brought home something small and furry in a box.")
print("Apparently it was what they call a 'cat' and it's name was", catname + ".")
print(catname, "got into everything!")
print(dogname, "could not get any peace from", catname, "and just wanted it to go away.")
print("Then, an opportunity arose when", ownername, "left the back door unlocked.")
print(dogname, "knew it could open the door easily enough.")
print(dogname, "saw there was a", favbird, "outside that", catname, "could chase and be gone forever.")

keepGoing = "yes"
    while keepGoing.lower() == "yes":
    openDoor = input("\nShould the dog open the back door? Type yes or no: ")
    while openDoor != "yes" and openDoor != "no":
            openDoor = input("\nInvalid value. Please enter yes or no:  ")
    if openDoor == "yes":
        print (dogname, "opened the back door so", catname, "got outside.")
        print (catname, "heard a noise from", favbird, "and decided to chase after it.")
        print (catname, "spent about", number, "minutes running around outside before giving up on catching the bird.")
        print (dogname, "watched as", catname, "waltzed right back inside disinterested in anything but licking itself.")
        print ("Upset,", dogname, "sniffed around the house looking for some crumbs on the ground and came across", favfood, "sitting on the counter.")
    else:
        print (dogname, "decided to it would be wrong to let the cat outside and instead sulked around the house.")
        print (dogname, "noticed there was a wonderful smell coming from the kitchen.")
        print ("Upon further inspection, it was found that", favfood, "which is the favorite food of", dogname, "was sitting right there on the counter for the taking.")
        print (ownername, "was nowhere to be found.")
 

    getFood = input("\nShould the dog try to get the food off the counter? Type yes or no: ")
    if getFood == "yes":
        print(dogname, "has seen", catname, "jump on top of the counter before and that was the only shot", dogname, "had.")
        print(dogname, "found", catname, "laying on the bed that was meant for dogs only, but", dogname, "brushed it off for the sake of", favfood + ".")
        print(dogname, "told", catname, "'Get up on the counter and get that", favfood, "down so we can both enjoy it because", ownername, "left it for us but forgot to put it in my bowl!'")
        print(catname, "didn't question it at all and with one swipe the", favfood, "was on the ground.")
        print("The loud crash got the attention of", ownername, "who came running down into the kitchen.")
        print(ownername, "saw", dogname, "eating the", favfood, "off the floor and", catname, "was nowhere to be found.")
        print(ownername, "scolded", dogname, "and punished it with", number, "days of no dog treats.")
    else: 
        print(dogname, "decided not to interact with the cat at all since he did not want to be friends.")
        print(dogname, "continued to day dream of ways to destroy the cat but never acted on anything.")
        print(dogname, "wanted to remain a good dog and not jepordize the daily treats given by", ownername + ".")
    

keepGoing = input ("Do you want to try again? Enter yes or no:  ")

