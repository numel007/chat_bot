from random import choice


def get_bot_response(user_response):
    respond_hungry = ["I'm sure I can pick a great burger for you.", "Sounds like you could use a good burger.", "Hunger is best solved with a burger to the facehole."]
    respond_full = ["You're full? No such thing. You could easily stuff down another small cheeseburger.", "You're lying. You get a burger.", "You're not full. You're just weak. A burger it is."]

    if user_response_1 == "hungry":
        return choice(respond_hungry)
    elif user_response_1 == "full":
        return choice(respond_full)
    else:
        return "I don't understand. Are you hungry or full? "


def get_bot_response_2(user_response_2):
    respond_patty = ["That's a lot of meat. Are you sure about this?", "You might get the meat sweats. Is that alright with you?", "For reasons of legality I must confirm you actually want another patty."]
    respond_other = ["Wrong answer. I'm assuming you mistyped and meant to write 'patty.'", "Close but no cigar. More meat is a better idea.", "That's a strange well to spell 'patty.'"]

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


print("Hello, I am here to help you decide on your nutritional needs.")
print("Enter 'stop' or 'done' at any time to exit.")

user_response_1 = ""
user_response_2 = ""
user_response_3 = ""

while True:
    user_response_1 = str.lower(input("How are you currently feeling? Hungry or full? "))

    if user_response_1 == "stop" or user_response_1 == "done":
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
    user_response_2 = str.lower(input("Now that we know you're ordering something, what topping do you want on your burger? "))

    if user_response_2 == "stop" or user_response_2 == "done":
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
        exit()
    elif user_response_3 == "yes":
        bot_response_3 = get_bot_response_3(user_response_3)
        print(bot_response_3)
        break
    else:
        bot_response_3 = get_bot_response_3(user_response_3)
        print(bot_response_3)
        continue