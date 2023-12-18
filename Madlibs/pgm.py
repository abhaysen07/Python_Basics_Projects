# String representation
# suppose we want to create a string that says "Subscribe to ______"
# youtuber = "Kylie Ying" some string variable

# # a few ways to do this
# print("Subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")

adj = input("Adjacent: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer Programming is so {adj}! It makes me so excited all the time because \
    I love to {verb1}. Stay hyderated and {verb2} like you are {famous_person}!"

print(madlib)