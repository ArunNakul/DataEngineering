import re

while True:

    text = input("Enter the String : ")

    pattern = r"[a-]"

    match = re.findall(pattern,text)

    print ("match : ",match)