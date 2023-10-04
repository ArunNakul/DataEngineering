import re

while True:
    text = input("Enter the String :")

    pattern = r"\Z" # doubt
    pattern = r"\A" # doubt

    match = re.findall(pattern,text)

    print("match : ",match)