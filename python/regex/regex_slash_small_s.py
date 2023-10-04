import re

while True:

    text = input("Enter the string : ")
    pattern = r"\s"  # it matches if it occurs tab or space or enter ie., all whitespace characters

    match = re.findall(pattern,text)

    print("match : ", match)