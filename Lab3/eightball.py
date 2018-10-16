import random

def Magic_Eight():
    question=input("Ask Magic 8 your deepest desires: (Press enter to end session)  ")
    answers=["Don't count on that.","It will happen soon.","Go with your gut!","I am having trouble forseeing.","The stars are pointing to yes!","My heart says no.","Maybe the answer should wait.","It will happen"]
    
    if question == "":
        print("Game is Exiting....")
    else:
        print (random(answers))
        Magic_Eight()
