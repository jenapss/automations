import requests
from bs4 import BeautifulSoup
import hashlib
import sys
import os
import argparse
import gspread


# Initialize parser
parser = argparse.ArgumentParser()
 

# Adding optional argument
parser.add_argument("first", action='store')

# Read arguments from command line
args = parser.parse_args()



#Reading file from developers website
webpage_response = requests.get(args.first)
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")



#print(str(soup))
text_from_website = str(soup) #converting the "soup" to the string
print("Web File type",type(text_from_website)) #printing the type of information we got from developers website
#print(text_from_website)

f = open("new_text.txt", "w")   # 'r' for reading and 'w' for writing
f.write(text_from_website)    # Write inside file the "text_from_website" to the "new_text_file.txt" file
f.close() #closing the file 

cool_doc2 = open("another_app_ads.txt",'r')
local_text_file = cool_doc2.read() #reading the standart app-ads.txt text file that should compared with text file we received from developers website
cool_doc2.close()
print("Local File type",type(local_text_file)) #check the file type of "local_text_file"




cool_doc = open("new_text.txt",'r')
downloaded_text = cool_doc.read()
cool_doc.close()
print("Downloaded File type",type(downloaded_text))
if downloaded_text == local_text_file:
    print ('Files are the same. File from: '+ args.first+ " and app-ads.txt file are the same." )
else:
    print('Files are not the same')

#print(downloaded_text)


'''
with open("app_ads.txt",'r') as text:
    cool_doc = text.read()
    print('-----------')
    #print(cool_doc)
    if cool_doc == soup.string:
        print("equal") 
    else:
        print('not equal')
'''

'''if os.path.exists("new_text.txt"):
    os.remove("new_text.txt")'''

