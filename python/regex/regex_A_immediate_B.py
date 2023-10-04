import re

while True:

    text = input("Enter the String : ")

    #pattern = r"(?<=B)A" # Success only when 'BA'
    #pattern = r"(?<!B)A" # Success only when 'AB'

    pattern = r"(?P=name)"   # doubt
    match = re.findall(pattern,text)

    print("match :", match)