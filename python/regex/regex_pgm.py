
import re
while True:
    text = input("Input the email id")
    #pattern = input("pattern to be searched")
    #text = " hello Ajay"
    pattern = r"^arun$"
    match = re.findall(pattern, text)

    print ("match :",match)

''' This program checks only 'arun' in text
Input the email idarun     
match : ['arun']
Input the email id324arunerwerw
match : []
Input the email id
'''