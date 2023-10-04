import re

while True:

    text = input ("Enter the string : ")

    pattern = r"A(?!B)"  # Doubt

    match = re.findall(pattern,text)

    print ("match : ",match)