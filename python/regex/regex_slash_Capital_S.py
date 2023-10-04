import re

while True:

    text = input(" Enter the String : ")
    pattern = r"\S" # match all non-whitespace characters for eg: "arun"


    match = re.findall(pattern,text)

    print("match : ",match)