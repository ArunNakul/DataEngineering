import re

while True:

    text = input("Enter the string : ")

    pattern = r"[\w*0]"

    match = re.findall(pattern,text)

    print("match : ", match)