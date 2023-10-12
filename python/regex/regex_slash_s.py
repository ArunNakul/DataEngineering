import re

while True:

    text = input("Enter the String : ")
    file1 = open("myfile.txt","r+")

    print(file1)
    text2 = file1.read()

    pattern = r"\s+" # it will check tab and space , \n and \r           # both are same as below
    pattern = r"[ \n\t\r\f]+" # it will check tab and space , \n and \r  # both are same as above
    # \t is working in while giving input 
    # \r is not working
    # \n is working in file

    match = re.findall(pattern,text2)

    print (" match : ", match)
    print ("count : " ,len(match))