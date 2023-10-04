import re

while True:

    text = input("Enter the string : ")

    pattern = r"\b"  #DOUBT

    match = re.findall(pattern,text)

    print ("match : ",match)