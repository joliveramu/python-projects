#Quiz Game
#Contains numerous questions to be answered. Questions will be thrown to you in random order.
#Every correct questions give you 1 point but if in case that it is incorrect, you'll be deducted by 1 point


import random
import time
questions = [
"Founder of Java",
"Year Python was created",
"file extension of SQL",
"C with classes.",
"Command used to compile java programs in command line",
"Unix/Linux's administrative command",
"ILOVEYOU virus was developed in what platform?",
"One of the Microsoft's Founder",
"Current version of Windows OS",
"Dennis Ritchie's programming language creation",
"Idea for a new iteration of the World Wide Web based on blockchain technology",
"Anders Hejlsberg first programming language ever created",
"Operating System of Apple",
"First female programmer"
]
answers = ["C","James Gosling","Ada Lovelace","C#","macOS","1991","Web3",".sql","3","javac","sudo","c++", "vbscript","Paul Allen","Bill Gates","Windows 11"]



loopCount = 0
points = 0
#Will continuously loop until the loopCount < len(questions) became false
while loopCount < len(questions):
    #Randomize question
    randomizer = random.randint(0, len(questions)-1)
    print(f"Question: {questions[randomizer]}")
    answer = input("Response: ")
    #if answer is found the answers list, you will be given one point
    #else you'll be deducted by 1 point
    if answer in answers:
        points = points + 1
    else:
        points = points - 1
    loopCount = loopCount + 1

print("Calculating results..")
time.sleep(5)
if points / len(questions) >= .50:
    print(f"Out of {len(questions)} questions asked, you got {points} correct of them. Nice knowledge!")
else:
    print(f"Out of {len(questions)} questions asked, you got {points} correct of them. You need to study more!")
