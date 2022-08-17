# run me in your terminal
# by typing "pypet.py"
# and pressing enter

#This project was built using Tatiana Tylosky's pypet tutorial on python.org

##############

import random

py_cat = {
    'photo': "((=^o.o^=))",
    'name': 'Nix',
    'age': 5,
    'weight': 5.5,
    'hungry': True,
    'phrases': ["You're my bff!", "meooow", "I <3 You" ]
}

def startup_pypet():
    print ("Welcome to Pypet!")
    print ("Enter 'stats' to view your pypet.")
    print ("Enter 'feed' to feed your pypet.")
    print ("Enter'chat' to chat with your pypet")
    print ("Enter 'quit' to exit.")

def pypet_stats():
    print ("Hi, it's " + py_cat['name'] + " " + py_cat['photo'])
    print (py_cat['name'] + " weighs " + str(py_cat['weight']) + " pounds ")

    if py_cat['hungry']:
        print ("Your pypet is hungry!")
    else:
        print (" Your pypet *BURPS* loudly")    

startup_pypet()
   
terminate = False

while not terminate:
    print ("###########################")

    user_input = input('> ')

    if user_input == "quit":
       terminate = True   

    elif user_input == "stats":
        pypet_stats()

    elif user_input == "chat":
        print(random.choice(py_cat['phrases']))

    elif user_input == "feed":
        print ("Omnomnonm, you fed your Pypet!")
        py_cat['weight'] = py_cat['weight'] + 1
        py_cat['hungry'] = False   

    else:  
        print ("Sorry, there was an error")   

print ("Goodbye!")            


