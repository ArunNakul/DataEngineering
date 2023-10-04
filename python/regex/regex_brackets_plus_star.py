import re

while True:

    text = input ("Enter the String : ")

    pattern = r"[(+*)]" # Checks only the brackets and + sign or * sign

    match = re.findall(pattern,text)

    print ("Match : ", match)