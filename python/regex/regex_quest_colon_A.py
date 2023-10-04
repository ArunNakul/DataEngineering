import re

while True:

    text = input ("Enter the string : ")

    pattern = r"(a?:A)"  # doubt , some discrepancy in cheatsheet with output

    match = re.findall(pattern,text)

    print("match : ",match)