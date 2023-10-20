import re

while True:

    text = input("Enter the string : ")

    pattern = r"\D" # first character can be any letter or digits or _ second character can be non-digit ie, charachter or symbol
    pattern = r"^\D\w*" # First character should be alphanumeric and remaining character can be anything
    pattern = r"\D\w*" # it won't check first character is non-numeric (D), ^ - needed for check the first character.
    pattern = r"\w*\D$" # it will check last character is non-digit or not.

    match = re.findall(pattern, text)

    print("match : ",match)