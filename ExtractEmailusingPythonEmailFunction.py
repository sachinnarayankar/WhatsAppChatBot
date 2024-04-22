import re

# Custom function to extract email addresses from text
def extract_emails(text):
    # Define a regular expression pattern for extracting emails
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    
    # Find all email addresses in the text using the pattern
    email_addresses = re.findall(email_pattern, text)
    
    return email_addresses

# Open yet another text file for reading
with open('D:\\JobApplicationBot\\WhatsAppReadMessageBot\\Whatsapp Group HR Messages.txt', 'r') as file:
    text = file.read()

# Extract email addresses using the custom function
email_addresses = extract_emails(text)

# Print the extracted email addresses
for email in email_addresses:
    print(email)