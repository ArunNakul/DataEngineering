import re

while True:

    text = input("Enter the String  : ")

    pattern = r"[a\-z]"

    match = re.findall(pattern,text)

    print(" match : ",match)