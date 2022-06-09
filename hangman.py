import random #Random to generate random questions
from timeit import default_timer as timer #Timer library
#Displaying different phases of how the kangaroo would be killed.
decider = [
    ["=","\t","\t","\t","\t","Kangaroo"],
    ["=","=","\t","\t","\t","Kangaroo"],
    ["=","=","=","\t","\t","Kangaroo"],
    ["=","=","=","=","\t","Kangaroo"],
    ["=","=","=","=","=","Kangaroo"],
    ["=","=","=","=","=","Kangaroo is Dead"],
]
#No of Trial
trial = len(decider)
#No of trials used to solve the problem
trialCount = 0
#Hint or Questions
hint=["First Color in RGB", "Where is this developed?","Database is?","Year python is born"]
#Answers
words = ["Red","Python","SQL","1991"]
isTrue = True
#Random number generator
selector = random.randint(0, len(hint)-1)
while isTrue:
    #The program will end once trialCount has reached the trial
    while trialCount < trial:
        print(f"You have {trialCount} out of {trial} to work on. 30 seconds to answer.")
        print(hint[selector])
        start = timer()
        answer = input()
        end = timer()
        timeUsed = int(end - start)
        if answer in words and timeUsed <= 30:
            print(f"You have done it! in {trialCount} tries in {timeUsed} seconds")
            itTrue = False
            trialCount = 10
            break
        elif trialCount == trial:
            print("Kangaroo died.")
            isTrue = False
            break
        elif timeUsed >= 30:
            print("You have thought a lot in 30 seconds!")
            decidingPart = decider[trialCount]
            print("".join(i for i in decidingPart))
        else:
            decidingPart = decider[trialCount]
            print("".join(i for i in decidingPart))
            
        trialCount = trialCount + 1

