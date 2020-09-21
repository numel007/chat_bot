# Import choice function from Python's random module
from random import choice


# First line of questions. Decides which response to return. Recognized inputs are "hungry", "full", and other text.
def get_bot_response(user_response_1):
    respond_hungry = ["I'm sure I can pick a great burger for you.", "Sounds like you could use a good burger.", "Hunger is best solved with a burger to the facehole."]
    respond_full = ["You're full? No such thing. You must consume another burger.", "You're lying. You get a burger. No, there are no other options.", "You're not full. You're just weak. A burger it is."]

    if user_response_1 == "hungry":
        # Returns random choice from respond_hungry list
        return choice(respond_hungry)
    elif user_response_1 == "full":
        # Returns random choice from respond_full list
        return choice(respond_full)
    else:
        return "I don't understand."


# Second line of questions. Decides which response to return. Recognized inputs are "patty", "meat", "burger", and other text. 
def get_bot_response_2(user_response_2):
    respond_patty = ["That's a lot of meat. Are you sure about this?", "You might get the meat sweats. Is that alright with you?", "For legal reasons I must confirm you actually want more protein."]
    respond_other = ["Wrong answer. I'm assuming that was a typo and you meant to write 'patty.'", "Close but no cigar. More meat is a better idea.", "That's a strange way to spell 'patty.'"]

    if user_response_2 == "patty" or user_response_2 == "meat" or user_response_2 == "burger":
        # Returns random choice from respond_patty list
        return choice(respond_patty)
    else:
        return choice(respond_other)


# Third line of questions. Decides which response to return. Recognized inputs are "yes" and other text.
def get_bot_response_3(user_response_3):
    respond_yes = ["Hell yeah brother, welcome to the American dream.", "There was honestly no other acceptable answer. Well done.", "You passed the test. Proceed to the next window to collect your burger."]
    respond_other_2 = ["That's not how you spell 'yes.'", "Imagine being this wrong. Try again.", "It's not opposite day today. Try again."]

    if user_response_3 == "yes":
        # Returns random choice from yes list
        return choice(respond_yes)
    else:
        return choice(respond_other_2)


# Startup text
print("Hello, Personal_Nutritionist here. I am to assist you with your dietary needs.")
print("Enter 'stop' or 'done' at any time to exit.")

# Initialize user response storages with no content.
user_response_1 = ""
user_response_2 = ""
user_response_3 = ""


# Questions user on how full they are. Continues to loop until either "hungry" or "full" is entered. Input of "stop" or "done" exits the entire script.
# I did not use break on the "stop" and "done" inputs since there are multiple while loops and the user would have to manually break out of each loop if attempting to end the entire program.
while True:

    # Stores input in user_response_1 and converts input into lowercase for better handling of responses.
    user_response_1 = str.lower(input("How are you currently feeling? Hungry or full? "))

    if user_response_1 == "stop" or user_response_1 == "done":
        print("Well you win some, you lose some.")
        # Exits program
        exit()
    elif user_response_1 == "hungry":
        # Calls get_bot_response using user_response_1 as argument. Prints returned value from choice(respond_hungry).
        bot_response = get_bot_response(user_response_1)
        print(bot_response)
        break
    elif user_response_1 == "full":
        # Calls get_bot_response using user_response_1 as argument. Prints returned value from choice(respond_full).
        bot_response = get_bot_response(user_response_1)
        print(bot_response)
        break
    else:
        # Continue to loop until a valid response is entered.
        bot_response = get_bot_response(user_response_1)
        print(bot_response)
        continue

    
# Questions user on their topping choice. Continues to loop until either "patty", "meat" or "burger" is entered.
# Inputting "stop" or "done" kills the program.
while True:

    # Stores input in user_response_1 and converts input into lowercase for better handling of responses.
    user_response_2 = str.lower(input("So you're getting a burger. What topping do you want on it? "))

    if user_response_2 == "stop" or user_response_2 == "done":
        # Exits program
        print("I didn't want to talk to you anyways.")
        exit()
    elif user_response_2 == "patty" or user_response_2 == "meat" or user_response_2 == "burger":
        # Calls get_bot_response_2 using user_response_2 as argument. Prints returned value from choice(respond_patty).
        bot_response_2 = get_bot_response_2(user_response_2)
        print(bot_response_2)
        break     
    else:
        # Calls get_bot_response_2 using user_response_2 as argument. Prints returned value from choice(respond_other).
        # Continues loop until if or elif is satisified.
        bot_response_2 = get_bot_response_2(user_response_2)
        print(bot_response_2)
        continue


# Confirms previous choice. Continues to loop until either "yes" or "no" is entered.
# Inputting "stop" or "done" kills the program.
while True:

    # Stores input in user_response_1 and converts input into lowercase for better handling of responses.
    user_response_3 = str.lower(input("Yes or no? "))

    if user_response_3 == "stop" or user_response_3 == "done":
        # Exits program
        print("What a tease.")
        exit()
    elif user_response_3 == "yes":
        # Calls get_bot_response_3 using user_response_3 as argument. Prints returned value from choice(respond_yes).
        bot_response_3 = get_bot_response_3(user_response_3)
        print(bot_response_3)
        break
    else:
        # Calls get_bot_response_3 using user_response_3 as argument. Prints returned value from choice(respond_other_2).
        # Continues loop until if or elif is satisified.
        bot_response_3 = get_bot_response_3(user_response_3)
        print(bot_response_3)
        continue


# Summarizes all of the user's choices. Explains what happened during the "hungry or full?" question and answer process.
if user_response_1 == "full":
    print(f"When asked if you were hungry, you responded {user_response_1}. This was the wrong answer so we took the liberty of correcting your answer to 'hungry' for you.")
else:
    print(f"When asked if you were hungry, you responded {user_response_1}.")

print(f"When asked what topping you wanted, you responsed {user_response_2}.")
print(f"When asked to confirm your topping, you responded {user_response_3}.")