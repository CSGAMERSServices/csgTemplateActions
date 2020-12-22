import os
import re

token = os.environ['INPUT_TOKEN']
cardNote = os.environ['INPUT_CARDNOTE']
issueUrl = os.environ['INPUT_ISSUEURL']

print('Token')
print(token)

# Extract all email addresses from the Issue Note, store the last one
#emailAddresses = re.findall(r'[\w\.-]+@[\w\.-]+', cardNote)
#developer = emailAddresses[-1]

# Print developer as output
#print(f"::set-output name=developer::{developer}")