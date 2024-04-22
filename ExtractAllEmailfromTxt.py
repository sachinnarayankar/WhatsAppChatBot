import re
pat = re.compile(r'[a-zA-Z0-9\._]+@[a-zA-Z\.]') # regex pattern
f = open("D:\\JobApplicationBot\\WhatsAppReadMessageBot\\Whatsapp Group HR Messages.txt", "rt")
#f.write('walkup@cs.washington.edu, geb@cs.pitt.edu, walkup@cs.washington.edu \n')
mails = re.findall(r"[a-z]+@[a-z\.]+", f.read())
print(list(set(mails)))