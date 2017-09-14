# Stephen Randall
# 09/13/17
# Unit2proj
# This code makes a ChatBot that you can interact with.

print("Hi there, My name is ChatBot, What is your name?")
person = input("Enter your name: ")
print("Hello", person, "That's a really nice name! I wish my name was that interesting!")
# Greeting

print("Where abouts are your from", person, "?")
location = input("Where are you from:")
print("Really? I've heard great things about", location, "!")
# Ask about where they're from
print("Do you like math? Its my favourite subject! What's your favourite number?")
my_fave_number = 78
fave_number = input("Whats your favourite number:")
relate_numbers = int(my_fave_number) / int(fave_number) * 0.25
print("That's cool! My favourite number divided by yours times .25 is:", relate_numbers)
print("See told you I was good at math!")
# Ask fave number relate it to mine
subject_we_talk = input("What subject should we talk about now?")
print("Blegh, I'll pass on that! Let's talk about cars :")
print("What's your favourite car/dream car?")
fave_car = input("What's your favourite car:")
price = input("Nice! How much does the car cost:")
years = input("WoW that's expensive! How many years are you paying that off for:")
interest = input("Annual interest?:")
print("Step back and watch the magic happen")
months = 12 * float(years)
monthly_interest = float(interest) / 100 / 12
monthly_payment = (float(monthly_interest) * float(price)) / (1 - (1 + monthly_interest) ** -months)
print("Processing...")
print("Your Monthly Payment is:", monthly_payment)
