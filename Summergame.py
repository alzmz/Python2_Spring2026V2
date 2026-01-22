# 18 July
# I refreshed myself on the use of the "f" string. ex:
from idlelib.configdialog import font_sample_text

#dashes = "-----------------------------"
#print(dashes)
# print("These are dashes {dashes}") - I need to add the "f" string to this becasue I added text
# unless it won't print what is in the variable
#print(f"These are dashes {dashes}")

#practice IDENTIFICATION CARD
#dashes = "--------------------------------------------"
#id = "IDENTIFICATION CARD"
#name = input("What is your first name: ")
#lname = input("What is your last name: ")
#occup = input("What is your occupation: ")

#print(dashes)
#print(id)
#print(dashes)

#print(f"First Name: {name}")
#print(f"Last Name: {lname}")
#print(f"Occupation: {occup}")

#print(dashes)


#TRIVIA GAME BY ZE GOAT ALEXIO

dashes = "/------------------------------------------/"
title = "TRIVIA! CAN U REVEAL THE ANSWER?!"

print(dashes)
print(title)
print(dashes)

question_one = input("Who is the GOAT of football?:")
if question_one == "Ronaldo" or question_one == "ronaldo" or question_one == " ronaldo" or question_one == " Ronaldo":
    print("Response: You do know ball after all...SUUUUUUI 😲")
else:
    print("Response: Your Breaking my heart!!! 😩")


question_two = input("What is an anime that u love the most?:")
if question_two == "Solo Leveling" or question_two == "solo leveling" or question_two == "Attack On Titan":
    print("Response: ARISE!... You got good taste MA DUDE! 🤔")
else:
    print("Response: GO WATCH SOLO LEVELLING IDIOT! 😭")

if question_two == "kurokus basketball" or "Kurokus Basketball":
    print("Response: Thats a very good anime!")

question_three = input("Do you feel safe where you're at?:")
if question_three == "No" or question_three == "no" or question_three == "nah":
    print("Response: I knew it.... 🤭")
else:
    print("Response: Liar... I'll make you pay for that... 😡")

    question_four = input("Are you enjoying this Trivia?:")
    if question_four == "Yes" or question_four == "yes" or question_four == "Yep" or question_four == "yep":
        print("Response: I knew it! I'm so funny right? 😆")
    else:
        print("Response: that's so mean... Why are you even playing then? 😢")

    question_five = input("I'm at your door...?")
    if question_five == "Yes" or question_five == "yes":
        print("Open it up then... 😈")
    else:
        print("Yes I am... your address is #####################... Now let me in! 😈")














