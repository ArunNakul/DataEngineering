import re

while True:

    text = input("Enter the String :")

    pattern = r"A(?=B)"  # it is similar like condition, its satify only when 'AB' finds in the string

    match = re.findall(pattern,text)

    print("match : ",match)