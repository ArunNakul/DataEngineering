import re

while True:
    text = input("Enter the string: ")

    pattern = r"\d"

    match = re.findall(pattern,text)

    print ("match : ",match)