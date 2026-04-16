from validator_collection import validators

input = input("What is your email address? ")
try:
    validators.email(input)
except:
    print("Invalid")
else:
    print("Valid")
