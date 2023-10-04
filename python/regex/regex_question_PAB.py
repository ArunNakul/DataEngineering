import re

while True:

    text = input("Enter the String : ")

    pattern = r"(A?PAB)"  # doubt

    match = re.findall(pattern,text)

    print("match : ", match)