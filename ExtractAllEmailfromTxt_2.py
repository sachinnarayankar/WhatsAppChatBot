import re
in_file = open("D:\\JobApplicationBot\\WhatsAppReadMessageBot\\Whatsapp Group HR Messages.txt","rt")


for line in in_file:
    if re.match(r'[\w\.-]+@[\w\.-]+',  line):
        print(line)