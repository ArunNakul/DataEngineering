import re

while True:

    text = input ("Enter the string : ")

    pattern = r"[a\-z]"  # match with characters 'a','-' or 'z'

    match = re.findall(pattern,text)

    print("match : ",match)