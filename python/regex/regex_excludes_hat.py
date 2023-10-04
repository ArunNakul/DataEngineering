import re

while True:

    text = input("Enter the String : ")

    pattern = r"[^ab5]"  # other than ab5 will match

    match = re.findall(pattern,text)

    print ("match : ",match)