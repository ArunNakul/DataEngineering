import re

while True:

    text = input("Enter the string : ")

    pattern = r"[a-z0-9]"  # check only the a to z or 0 to 9

    match = re.findall(pattern,text)

    print("match : ",match)