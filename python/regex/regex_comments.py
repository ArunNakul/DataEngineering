import re

while True:

    text = input ("Enter the String : ")

    pattern = r"(?#Arun)"  # comment session

    match = re.findall(pattern,text)

    print("match : ",match)