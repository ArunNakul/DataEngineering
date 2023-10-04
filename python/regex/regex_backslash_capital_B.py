import re

while True:

    text = input("enter the input string : ")

    pattern = r"\B"  # doubt

    match = re.findall(pattern,text)

    print("match : ",match)
