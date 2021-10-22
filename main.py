import random

print("welcome to guess the number game! ")
name = input("pls lets us know ur name: ")
print("hello, ", name, "there are some things you need tp know before we begin..")
print("1) you have to guess a number so the number u think type only that number and nothing else")
print("2) you will get three chances to guess the number")
print("3) you have to guess the number between 1 and 10")
print("3) if you guess the number you win!!!")
play = input("if you agree to the rules and wanna play type 'yes' ")


if play == "yes":
    print("great lets begin!!")
else: print("ok, then bye till next time :)"); exit()

rn = random.randint(0, 10)

guess1 = int(input("pls guess a number: "))

if guess1 == rn:
    print("correct! great job!! :)")
    exit()
if guess1 > rn:
    print("the number is smaller than this")
if guess1 < rn:
    print("the number is bigger than this")

guess2 = int(input("try again!!: "))
if guess2 == rn:
    print("correct! great job!! :)")
    exit()
if guess2 > rn:
    print("the number is smaller than this")
if guess2 < rn:
    print("the number is bigger than this")

guess3 = int(input("try again!!: "))
if guess3 == rn:
    print("correct! great job!! :)")
    exit()
if guess3 > rn:
    print("the number is smaller than this")
if guess3 < rn:
    print("the number is greater than this")

guess4 = int(input("try again!!: "))
if guess4 == rn:
    print("correct! great job!! :)")
    exit()
if guess4 > rn:
    print("sorry but you lost, better luck next time :)")
if guess4 < rn:
    print("sorry but you lost, better luck next time :)")
