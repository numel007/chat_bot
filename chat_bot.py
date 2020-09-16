from random import choice


def get_bot_response(user_response):
    respond_hungry = ["I'm sure I can pick a great burger for you.", "Sounds like you could use a good burger.", "Hunger is best solved with a burger to the facehole."]
    respond_full = ["You're full? No such thing. You must consume another burger.", "You're lying. You get a burger. No, there are no other options.", "You're not full. You're just weak. A burger it is."]

    if user_response_1 == "hungry":
        return choice(respond_hungry)
    elif user_response_1 == "full":
        return choice(respond_full)
    else:
        return "I don't understand. Are you hungry or full? "


def get_bot_response_2(user_response_2):
    respond_patty = ["That's a lot of meat. Are you sure about this?", "You might get the meat sweats. Is that alright with you?", "For legal reasons I must confirm you actually want more protein."]
    respond_other = ["Wrong answer. I'm assuming that was a type and you meant to write 'patty.'", "Close but no cigar. More meat is a better idea.", "That's a strange well to spell 'patty.'"]

    if user_response_2 == "patty" or user_response_2 == "meat":
        return choice(respond_patty)
    else:
        return choice(respond_other)


def get_bot_response_3(user_response_3):
    respond_yes = ["Hell yeah brother. Welcome to the American dream.", "There was honestly no other acceptable answer. Well done.", "You passed the test. Proceed to the next window to collect your burger."]
    respond_other_2 = ["That's not how you spell 'yes.'", "Imagine being this wrong. Try again.", "It's not opposite day today. Try again."]

    if user_response_3 == "yes":
        return choice(respond_yes)
    else:
        return choice(respond_other_2)


print("Hello, xXRealHumanBeingXx here. I am to assist you with your dietary needs.")
print("Enter 'stop' or 'done' at any time to exit.")

user_response_1 = ""
user_response_2 = ""
user_response_3 = ""

while True:
    user_response_1 = str.lower(input("How are you currently feeling? Hungry or full? "))

    if user_response_1 == "stop" or user_response_1 == "done":
        print("Well you win some, you lose some.")
        exit()
    elif user_response_1 == "hungry":
        bot_response = get_bot_response(user_response_1)
        print(bot_response)
        break
    elif user_response_1 == "full":
        bot_response = get_bot_response(user_response_1)
        print(bot_response)
        break
    else:
        bot_response = get_bot_response(user_response_1)
        print(bot_response)
        continue

    

while True:
    user_response_2 = str.lower(input("So you're getting a burger. But what topping do you want on it? "))

    if user_response_2 == "stop" or user_response_2 == "done":
        print("I didn't want to talk to you anyways.")
        exit()
    elif user_response_2 == "patty" or user_response_2 == "meat":
        bot_response_2 = get_bot_response_2(user_response_2)
        print(bot_response_2)
        break
    else:
        bot_response_2 = get_bot_response_2(user_response_2)
        print(bot_response_2)
        continue



while True:
    user_response_3 = str.lower(input("Yes or no? "))

    if user_response_3 == "stop" or user_response_3 == "done":
        print("What a tease.")
        exit()
    elif user_response_3 == "yes":
        bot_response_3 = get_bot_response_3(user_response_3)
        print(bot_response_3)
        break
    else:
        bot_response_3 = get_bot_response_3(user_response_3)
        print(bot_response_3)
        continue