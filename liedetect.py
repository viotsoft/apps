import random

#Define list of questions

questions = [
    "Did you steal my pen?",
    "Did you eat the last cookie?",
    "Did you break my phone?",
    "Did you forget to take out the trash?",
    "Did you forget to feed the dog?",
    "you are lying"
]

#Loop through the questions and ask the user
for question in questions:
    response = input(question + " (yes or no): ").lower()
    if response == "yes":
        user_answer = True
    else:
        user_answer = False
    
    #Generate a random answer
    random_answer = bool(random.getrandbits(1))
    if user_answer == random_answer:
        print("You are telling the truth")
    else:
        print("You are lying")   