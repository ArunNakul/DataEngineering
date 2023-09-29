import re
while True:
    text = input("Enter the string: ")
    pattern = r"^a?$"  # left character occurs 0 or 1 times for eg: ' ' , 'a'
    match = re.findall(pattern, text)
    print ("match :", match)
