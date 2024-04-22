import email
from email import policy
from email.parser import BytesParser

# Open a text file for reading
with open('D:\\JobApplicationBot\\WhatsAppReadMessageBot\\Whatsapp Group HR Messages.txt', 'rb') as file:
    text = file.read()

# Parse the email content
message = BytesParser(policy=policy.default).parsebytes(text)

# Extract email addresses from the parsed email
email_addresses = [part for part in email.iterators.body_line_iterator(message)]



# Print the extracted email addresses
for email_address in email_addresses:
    try:
        if 'HR' in email_address or 'Hr' in email_address or 'hr' in email_address: 
            print(email_address)
            file1 = open("D:\\JobApplicationBot\\WhatsAppReadMessageBot\\emails.txt","a")#append mode
            #file1.write(email_address + " \n")
            file1.write(email_address)
            file1.close()
    except:
        print("SomeException for :" + email_address)