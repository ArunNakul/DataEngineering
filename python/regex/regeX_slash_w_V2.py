import re

while True:
    text = input("enter the input string : ")
    pattern = r"\w" # text can be 0 to 9 / a - z / A to Z

    match = re.findall(pattern,text)

    print ("match : ",match)