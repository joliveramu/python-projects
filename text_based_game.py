#The Decisions - Game
#In this game, you will be asked numerous questions, some situational questions but your response would be "Yes" or "No" only. There would be 10 stages of this game
#After all the stages, the outcome would rely on how you have responded on the questions given to you.
#No matter how good or bad your result is, be as you are.
import time

questions = ["You were being scolded by the society, is it okay to Rebel?",
"You saw a crime, a mass murder, would you be the catalyst of revolt?",
"Would you agree that, Nothing ever goes as planned in this world. The longer you live, the more you realize that in this reality, only pain, suffering, and futility exist.",
"Is it good to normalize things that is not morally good?",
"A world war has happened, you are being required to protect your country, will you do this Crusade?",
"Many people objected the idea of using plastics in our things, they offer natural products which is would cause more problem as we could not protect our planet. Isn't it ironic?",
"Do you still believe there is hope for us in the upcoming future?",
"Is abortion a crime for you who believe on a certain sect/religion?",
"Are you willing to murder/eradicate someone who have opposed your views?"
]

#The outcome will rely on your responses..
outcome = ["Chaotic Evil", "Neutral Evil","Lawful Evil", "Chaotic Neutral","True Neutral","Lawful Neutral","Chaotic Good","Neutral Good","Lawful Good"]
yesCount = 0
noCount = 0

iterator = 0

while iterator < len(questions):
    print(questions[iterator])
    response = input("Your Response: Yes/No: ")

    if response == "Yes":
        yesCount = yesCount + 1
        iterator = iterator + 1
    elif response == "No":
        noCount = noCount + 1
        iterator = iterator + 1
    else:
        print("Again, we'll ask once more..")

    

print(f"As a human being, you are..")
#Results would be tabulated in 10 seconds
time.sleep(10)
#Print out come
print(f"{outcome[len(questions) % int((yesCount - noCount))]}")

