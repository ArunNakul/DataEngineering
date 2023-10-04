import re

while True:

    text = input ("Enter the string : ")

    pattern = r"\d"
    pattern = r"^\d$"
    pattern = r"^\d+$"
    pattern = r"^\d{6}$"  # Checking Pincode, eg: 123456
    pattern = r"^[0-9]{6}$"  # Checking Pincode eg: 123456
    pattern = r"^[0-9]{3}[\s][0-9]{3}$"  # Checking Pincode , eg: 123 456
    pattern = r"^([0-9]{6})|([0-9]{3}[\s][0-9]{3})$"  # Checking Pincode , for eg: 123456 or 123 456
    

    match = re.findall(pattern,text)

    print("match : ", match )
    print(" \n count : ",len(match))