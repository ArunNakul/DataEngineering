import re

while True:

    text = input ("Enter the string : ")

    pattern = r"[arun]"

    match = re.findall(pattern,text)

    print("match : ",match)